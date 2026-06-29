"""
AVAGuard Desktop - Adaptive Scan Queue and Concurrency Control
Implements prioritized scheduling, AIMD concurrency throttling, and backpressure circuit breakers.
"""

import os
import json
import logging
import heapq
import time
import random
from typing import Dict, List, Any, Optional, Tuple, Protocol, runtime_checkable
from collections import deque
from pathlib import Path
from dataclasses import dataclass, field

try:
    from PyQt6.QtCore import QObject, pyqtSignal
except ImportError:
    # Headless/CLI fallback
    class QObject:
        def __init__(self, *args, **kwargs): pass
    def pyqtSignal(*args, **kwargs):
        class DummySignal:
            def emit(self, *args, **kwargs): pass
        return DummySignal()

logger = logging.getLogger(__name__)


@runtime_checkable
class ConcurrencyStrategy(Protocol):
    """Pluggable concurrency control interface."""
    def on_success(self, check_duration_ms: float) -> int: ...
    def on_throttle(self, retry_after_s: float) -> int: ...
    def on_error(self) -> int: ...
    def current_limit(self) -> int: ...


class AIMDConcurrencyController:
    """
    Additive Increase Multiplicative Decrease (AIMD) concurrency controller.
    Proven safe and resilient under burst and high-scale cloud execution environments.
    """
    def __init__(self, floor: int = 1, ceiling: int = 8, beta: float = 0.5, additive_step: int = 1):
        self.floor = floor
        self.ceiling = ceiling
        self.beta = beta
        self.additive_step = additive_step
        self.concurrency = max(floor, min(4, ceiling))  # Start conservative (e.g., 4 or floor)
        self.concurrency_fraction = 0.0  # Accumulates success steps for integer increases

    def on_success(self, check_duration_ms: float) -> int:
        # Gradually increase concurrency on success (Additive Increase)
        # We add a fraction based on current limit so it takes roughly the limit-number of successes
        # to increase the limit by 1 (similar to TCP congestion avoidance).
        self.concurrency_fraction += self.additive_step / float(self.concurrency)
        if self.concurrency_fraction >= 1.0:
            increase = int(self.concurrency_fraction)
            self.concurrency = min(self.ceiling, self.concurrency + increase)
            self.concurrency_fraction -= increase
            logger.debug(f"AIMD Concurrency increased to: {self.concurrency}")
        return self.concurrency

    def on_throttle(self, retry_after_s: float) -> int:
        # Halve concurrency instantly on rate limits (Multiplicative Decrease)
        self.concurrency = max(self.floor, int(self.concurrency * self.beta))
        self.concurrency_fraction = 0.0
        logger.warning(f"AIMD Throttled! Concurrency reduced to: {self.concurrency}")
        return self.concurrency

    def on_error(self) -> int:
        # Standard execution errors reduce limit slightly slower (decrease by 1)
        self.concurrency = max(self.floor, self.concurrency - 1)
        self.concurrency_fraction = 0.0
        logger.debug(f"AIMD Error fallback! Concurrency reduced to: {self.concurrency}")
        return self.concurrency

    def current_limit(self) -> int:
        return self.concurrency


class PIDConcurrencyController:
    """PID controller stub for smoother concurrency convergence (future swap-in)."""
    def __init__(self, kp: float = 0.5, ki: float = 0.1, kd: float = 0.05, target_latency_ms: float = 200.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target_latency_ms = target_latency_ms
        self.concurrency = 4
        
    def on_success(self, check_duration_ms: float) -> int:
        return self.concurrency
        
    def on_throttle(self, retry_after_s: float) -> int:
        return self.concurrency
        
    def on_error(self) -> int:
        return self.concurrency
        
    def current_limit(self) -> int:
        return self.concurrency


class ScanPriorityScorer:
    """
    Weighted priority scoring with time-decay starvation prevention.
    Returns highly negative scores for high-priority items so they are popped
    first in a standard min-heap priority queue.
    """
    def __init__(self, w_severity: float = 0.4, w_age: float = 0.3, w_retry: float = -0.2, w_manual: float = 0.1):
        self.w_severity = w_severity
        self.w_age = w_age
        self.w_retry = w_retry
        self.w_manual = w_manual

        # Severity ranks mapping
        self.severity_ranks = {
            "CRITICAL": 4,
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1,
            "INFO": 0,
            "UNKNOWN": 0
        }

    def compute_score(self, severity: str, time_in_queue_s: float, retry_count: int, manual_boost: float = 0.0) -> float:
        sev_rank = self.severity_ranks.get(severity.upper(), 0)
        age_minutes = time_in_queue_s / 60.0
        
        # Weighted sum (higher priority = more positive sum)
        # Note: retry_count has a negative weight to penalize failing checks so others can proceed
        priority_sum = (
            (self.w_severity * sev_rank) +
            (self.w_age * age_minutes) +
            (self.w_retry * retry_count) +
            (self.w_manual * manual_boost)
        )
        
        # Invert for min-heap (lowest score pops first)
        return -priority_sum


class BackpressurePolicy:
    """
    Circuit-breaker pattern for provider rate throttling.
    States: CLOSED (normal) -> OPEN (throttled) -> HALF_OPEN (probe)
    """
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

    def __init__(self, base_cooldown_s: float = 2.0, max_cooldown_s: float = 60.0):
        self.state = self.CLOSED
        self.base_cooldown_s = base_cooldown_s
        self.max_cooldown_s = max_cooldown_s
        self.cooldown_s = base_cooldown_s
        self.open_time = 0.0
        self.consecutive_throttles = 0
        self.probe_active = False

    def record_throttle(self, retry_after_s: float = 0.0):
        self.consecutive_throttles += 1
        self.state = self.OPEN
        self.open_time = time.time()
        
        # Determine cooldown: prioritize provider-specified retry_after, fallback to exp backoff
        if retry_after_s > 0.0:
            self.cooldown_s = min(self.max_cooldown_s, retry_after_s)
        else:
            self.cooldown_s = min(self.max_cooldown_s, self.base_cooldown_s * (2 ** (self.consecutive_throttles - 1)))
        
        logger.warning(f"Circuit Breaker TRIPPED to OPEN. Cooldown for {self.cooldown_s:.2f} seconds.")

    def record_success(self):
        if self.state == self.HALF_OPEN:
            logger.info("Circuit Breaker probe SUCCESS. Resetting to CLOSED.")
            self.state = self.CLOSED
            self.cooldown_s = self.base_cooldown_s
            self.consecutive_throttles = 0
            self.probe_active = False
        elif self.state == self.CLOSED:
            self.consecutive_throttles = max(0, self.consecutive_throttles - 1)

    def can_dispatch(self) -> bool:
        if self.state == self.CLOSED:
            return True
            
        if self.state == self.OPEN:
            elapsed = time.time() - self.open_time
            if elapsed >= self.cooldown_s:
                logger.info("Circuit Breaker cooldown elapsed. Transitioning to HALF_OPEN probe.")
                self.state = self.HALF_OPEN
                self.probe_active = True
                return True  # Allow exactly 1 probe task to dispatch
            return False

        if self.state == self.HALF_OPEN:
            # Only allow a single probe task through; other requests block
            return not self.probe_active

    def reject_probe(self):
        """If the probe task fails, trip circuit breaker again."""
        if self.state == self.HALF_OPEN:
            logger.warning("Circuit Breaker probe FAILED. Tripping back to OPEN.")
            self.record_throttle()


def decorrelated_jitter_delay(attempt: int, base_ms: float = 100.0, cap_ms: float = 30000.0) -> float:
    """
    Decorrelated Jitter scheduling algorithm.
    Reduces probability of collision in concurrent retry storms.
    """
    temp = min(cap_ms, base_ms * (3 ** attempt))
    delay_ms = random.uniform(base_ms, temp)
    return delay_ms / 1000.0  # Return seconds


@dataclass
class QueueItem:
    """Structure representing a single pending check in the queue."""
    check_id: str
    check_class_name: str
    provider_id: str
    severity: str = "LOW"
    manual_boost: float = 0.0
    retry_count: int = 0
    enqueue_time: float = field(default_factory=time.time)
    estimated_duration_ms: float = 150.0
    meta: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "check_id": self.check_id,
            "check_class_name": self.check_class_name,
            "provider_id": self.provider_id,
            "severity": self.severity,
            "manual_boost": self.manual_boost,
            "retry_count": self.retry_count,
            "enqueue_time": self.enqueue_time,
            "estimated_duration_ms": self.estimated_duration_ms,
            "meta": self.meta
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "QueueItem":
        return cls(
            check_id=d["check_id"],
            check_class_name=d["check_class_name"],
            provider_id=d["provider_id"],
            severity=d.get("severity", "LOW"),
            manual_boost=d.get("manual_boost", 0.0),
            retry_count=d.get("retry_count", 0),
            enqueue_time=d.get("enqueue_time", time.time()),
            estimated_duration_ms=d.get("estimated_duration_ms", 150.0),
            meta=d.get("meta", {})
        )


class ScanQueueManager(QObject):
    """
    Adaptive enterprise-ready scan queue scheduler.
    Features weighted priority scheduling, starvation prevention, burst-mode bypass,
    AIMD throttling, and persistent state saving.
    """
    queue_updated = pyqtSignal()  # Signal fired when queue state modifications occur
    circuit_breaker_changed = pyqtSignal(str, str)  # provider_id, state

    def __init__(self, persistence_file: Optional[Path] = None):
        super().__init__()
        # Priority queues grouped by provider: provider_id -> list(heap-tuples)
        self.priority_heaps: Dict[str, List[Tuple[float, int, QueueItem]]] = {}
        # Counter to act as tie-breaker in heap comparisons
        self._counter = 0
        
        # Burst-mode fast-path for short checks: provider_id -> deque(QueueItem)
        self.burst_deques: Dict[str, deque] = {}
        
        # AIMD controllers per provider
        self.concurrency_controllers: Dict[str, AIMDConcurrencyController] = {}
        
        # Circuit breakers per provider
        self.circuit_breakers: Dict[str, BackpressurePolicy] = {}
        
        # Priority scorer
        self.scorer = ScanPriorityScorer()
        
        # Setup persistence
        if persistence_file:
            self.persistence_path = persistence_file
        else:
            self.persistence_path = Path.home() / ".avaguard" / "scan_queue.json"
        self.persistence_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Load from disk if present
        self.load_state()

    def get_controller(self, provider_id: str) -> AIMDConcurrencyController:
        if provider_id not in self.concurrency_controllers:
            self.concurrency_controllers[provider_id] = AIMDConcurrencyController()
        return self.concurrency_controllers[provider_id]

    def get_circuit_breaker(self, provider_id: str) -> BackpressurePolicy:
        if provider_id not in self.circuit_breakers:
            self.circuit_breakers[provider_id] = BackpressurePolicy()
        return self.circuit_breakers[provider_id]

    def enqueue(self, item: QueueItem):
        provider = item.provider_id
        
        # Determine if we can route to burst-mode fast-path (<100ms estimation)
        if item.estimated_duration_ms < 100.0:
            if provider not in self.burst_deques:
                self.burst_deques[provider] = deque()
            self.burst_deques[provider].append(item)
            logger.debug(f"Routed check {item.check_id} to burst-mode fast-path.")
        else:
            # Route to priority heap
            if provider not in self.priority_heaps:
                self.priority_heaps[provider] = []
            
            score = self.scorer.compute_score(
                severity=item.severity,
                time_in_queue_s=time.time() - item.enqueue_time,
                retry_count=item.retry_count,
                manual_boost=item.manual_boost
            )
            
            self._counter += 1
            heapq.heappush(self.priority_heaps[provider], (score, self._counter, item))
            logger.debug(f"Enqueued check {item.check_id} to priority heap (Score: {score:.4f}).")

        self.save_state()
        self.queue_updated.emit()

    def dequeue(self, provider_id: str) -> Optional[QueueItem]:
        """
        Dequeues next execution item for specified provider.
        Checks burst queue first (hot fast-path), then priority heap.
        Supports work-stealing when provider queue is empty.
        """
        cb = self.get_circuit_breaker(provider_id)
        if not cb.can_dispatch():
            return None

        # 1. Check native burst-mode deque first
        burst_dq = self.burst_deques.get(provider_id)
        if burst_dq:
            item = burst_dq.popleft()
            self.save_state()
            self.queue_updated.emit()
            return item

        # 2. Check native priority heap
        heap = self.priority_heaps.get(provider_id)
        if heap:
            # We rebuild the heap to apply time-decay aging scores dynamically!
            self._rebuild_heap_with_aging(provider_id)
            heap = self.priority_heaps[provider_id]
            if heap:
                _, _, item = heapq.heappop(heap)
                self.save_state()
                self.queue_updated.emit()
                return item

        # 3. Work-stealing fallback: steal from other busy provider queues
        stolen_item = self._steal_work(provider_id)
        if stolen_item:
            logger.info(f"Provider thread '{provider_id}' STOLE work item '{stolen_item.check_id}' from '{stolen_item.provider_id}'")
            stolen_item.provider_id = provider_id  # Remap to execution provider
            self.save_state()
            self.queue_updated.emit()
            return stolen_item

        return None

    def _rebuild_heap_with_aging(self, provider_id: str):
        """Re-prioritizes the heap applying time-decay scoring."""
        heap = self.priority_heaps.get(provider_id)
        if not heap:
            return

        rebuilt = []
        now = time.time()
        for _, _, item in heap:
            score = self.scorer.compute_score(
                severity=item.severity,
                time_in_queue_s=now - item.enqueue_time,
                retry_count=item.retry_count,
                manual_boost=item.manual_boost
            )
            self._counter += 1
            rebuilt.append((score, self._counter, item))
            
        heapq.heapify(rebuilt)
        self.priority_heaps[provider_id] = rebuilt

    def _steal_work(self, thief_provider_id: str) -> Optional[QueueItem]:
        """Scans other providers' heaps/deques and steals the oldest/most valuable check."""
        for victim_provider, heap in self.priority_heaps.items():
            if victim_provider == thief_provider_id or not heap:
                continue
            # Peek to see if victim has excessive queue backlog (e.g. >2 items)
            if len(heap) > 2:
                # Steal the lowest-priority (best score) item from victim's heap
                self._rebuild_heap_with_aging(victim_provider)
                if self.priority_heaps[victim_provider]:
                    _, _, item = heapq.heappop(self.priority_heaps[victim_provider])
                    return item

        for victim_provider, dq in self.burst_deques.items():
            if victim_provider == thief_provider_id or not dq:
                continue
            if len(dq) > 2:
                # Steal from tail of burst deque (newest burst check)
                return dq.pop()
                
        return None

    def record_success(self, provider_id: str, check_duration_ms: float):
        self.get_controller(provider_id).on_success(check_duration_ms)
        cb = self.get_circuit_breaker(provider_id)
        old_state = cb.state
        cb.record_success()
        if old_state != cb.state:
            self.circuit_breaker_changed.emit(provider_id, cb.state)

    def record_throttle(self, provider_id: str, retry_after_s: float = 0.0):
        self.get_controller(provider_id).on_throttle(retry_after_s)
        cb = self.get_circuit_breaker(provider_id)
        old_state = cb.state
        cb.record_throttle(retry_after_s)
        if old_state != cb.state:
            self.circuit_breaker_changed.emit(provider_id, cb.state)

    def record_error(self, provider_id: str):
        self.get_controller(provider_id).on_error()
        cb = self.get_circuit_breaker(provider_id)
        if cb.state == BackpressurePolicy.HALF_OPEN:
            old_state = cb.state
            cb.reject_probe()
            if old_state != cb.state:
                self.circuit_breaker_changed.emit(provider_id, cb.state)

    def size(self) -> int:
        total = 0
        for heap in self.priority_heaps.values():
            total += len(heap)
        for dq in self.burst_deques.values():
            total += len(dq)
        return total

    def clear(self):
        self.priority_heaps.clear()
        self.burst_deques.clear()
        if self.persistence_path.exists():
            try:
                self.persistence_path.unlink()
            except OSError:
                pass
        self.queue_updated.emit()

    def save_state(self):
        """Saves current state serialize-ready for crash recovery."""
        state = {
            "priority_queues": {},
            "burst_queues": {}
        }
        
        for prov, heap in self.priority_heaps.items():
            state["priority_queues"][prov] = [item.to_dict() for _, _, item in heap]
            
        for prov, dq in self.burst_deques.items():
            state["burst_queues"][prov] = [item.to_dict() for item in dq]

        try:
            with open(self.persistence_path, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to persist scan queue state: {e}")

    def load_state(self):
        """Loads state on startup if recovery JSON exists."""
        if not self.persistence_path.exists():
            return

        try:
            with open(self.persistence_path, "r", encoding="utf-8") as f:
                state = json.load(f)

            priority_queues = state.get("priority_queues", {})
            for prov, items_list in priority_queues.items():
                self.priority_heaps[prov] = []
                for item_dict in items_list:
                    item = QueueItem.from_dict(item_dict)
                    self._counter += 1
                    # Recalculate score on reload
                    score = self.scorer.compute_score(
                        severity=item.severity,
                        time_in_queue_s=time.time() - item.enqueue_time,
                        retry_count=item.retry_count,
                        manual_boost=item.manual_boost
                    )
                    heapq.heappush(self.priority_heaps[prov], (score, self._counter, item))

            burst_queues = state.get("burst_queues", {})
            for prov, items_list in burst_queues.items():
                self.burst_deques[prov] = deque()
                for item_dict in items_list:
                    item = QueueItem.from_dict(item_dict)
                    self.burst_deques[prov].append(item)

            logger.info(f"Restored scan queue state from recovery file ({self.size()} items loaded).")
        except Exception as e:
            logger.error(f"Failed to load scan queue state: {e}. Starting with clean queue.")
            self.clear()
