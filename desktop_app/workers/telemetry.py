"""
AVAGuard Desktop - Performance Telemetry and Profiling
Instruments check executions, database store/retrieval, queue scheduling, and operational health.
"""

import os
import time
import json
import csv
import logging
import math
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Generator
from contextlib import contextmanager

# Try importing tracemalloc for memory tracking
try:
    import tracemalloc
except ImportError:
    tracemalloc = None

# PyQt6 imports for signals/slots with safe headless/pytest overrides
import sys
_force_headless = (
    "pytest" in sys.modules or 
    "unittest" in sys.modules or 
    os.environ.get("AVAGUARD_HEADLESS") == "1" or
    getattr(sys, "is_mocked_qt", False)
)

if _force_headless:
    class QObject:
        def __init__(self, *args, **kwargs): pass
    def pyqtSignal(*args, **kwargs):
        class DummySignal:
            def emit(self, *args, **kwargs): pass
            def connect(self, *args, **kwargs): pass
            def disconnect(self, *args, **kwargs): pass
        return DummySignal()
else:
    try:
        from PyQt6.QtCore import QObject, pyqtSignal
    except ImportError:
        # Fallback for headless/CLI environments
        class QObject:
            def __init__(self, *args, **kwargs): pass
        def pyqtSignal(*args, **kwargs):
            class DummySignal:
                def emit(self, *args, **kwargs): pass
                def connect(self, *args, **kwargs): pass
                def disconnect(self, *args, **kwargs): pass
            return DummySignal()

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Bounded Queue Defaults
# ---------------------------------------------------------------------------
# These caps bound memory growth in long-running/SaaS scenarios.
# All caps are runtime-configurable via PerformanceProfiler.set_queue_caps().
_DEFAULT_TIMELINE_CAP = 500      # Max timeline events in memory
_DEFAULT_HISTOGRAM_CAP = 2000    # Max values per named histogram
_DEFAULT_TIMING_CAP = 5000       # Max duration samples per timing context


class EMACalculator:
    """Exponential Moving Average calculator."""
    def __init__(self, alpha: float = 0.1, initial_value: float = 0.0):
        self.alpha = alpha
        self.value = initial_value
        self.initialized = False

    def update(self, new_value: float) -> float:
        if not self.initialized:
            self.value = new_value
            self.initialized = True
        else:
            self.value = (self.alpha * new_value) + ((1.0 - self.alpha) * self.value)
        return self.value


class PerformanceProfiler(QObject):
    """
    Hierarchical performance instrumentation with HdrHistogram-like percentile calculations,
    EMA throughput smoothing, timeline tracking, and database metrics.
    """
    metrics_updated = pyqtSignal(dict)  # Emits real-time metrics dictionary

    _profiles = {
        "development": {
            "sampling_rate": 1.0,      # Profile 100% of events
            "memory_tracking": True,
            "histogram_precision": 3,
        },
        "balanced": {
            "sampling_rate": 0.1,      # Sample 10%
            "memory_tracking": False,
            "histogram_precision": 2,
        },
        "performance": {
            "sampling_rate": 0.01,     # Sample 1%
            "memory_tracking": False,
            "histogram_precision": 1,
        },
    }

    _instance = None


    def __init__(self, profile_name: str = "development"):
        super().__init__()
        if getattr(self, "_initialized", False):
            return
        self._initialized = True
        self.profile_name = profile_name
        self.config = self._profiles.get(profile_name, self._profiles["development"])
        
        # Timing storage: context_name -> list of durations (seconds)
        self.timings: Dict[str, List[float]] = {}
        # Memory delta storage: context_name -> list of RAM changes (bytes)
        self.memory_deltas: Dict[str, List[int]] = {}
        # Operation counts for throughput
        self.op_counts: Dict[str, int] = {}
        # Throughput EMAs
        self.throughput_emas: Dict[str, EMACalculator] = {}
        # Thread/context stacks
        self.context_stack: List[str] = []
        
        # Expanded operational telemetry (Phase 3 requirements)
        self.timeline_events: List[Dict[str, Any]] = []
        self.gauges: Dict[str, float] = {}
        self.histograms: Dict[str, List[float]] = {}

        # Bounded queue caps — protect against unbounded memory growth in long-running processes
        self._timeline_cap: int = _DEFAULT_TIMELINE_CAP
        self._histogram_cap: int = _DEFAULT_HISTOGRAM_CAP
        self._timing_cap: int = _DEFAULT_TIMING_CAP

        # Drop counters — backpressure visibility surface (not silently discarding without telemetry)
        self._drops: Dict[str, int] = {
            "timeline": 0,
            "histogram": 0,
            "timing": 0,
        }
        
        self.perf_log_dir = Path.home() / ".avaguard" / "perf"
        self.perf_log_dir.mkdir(parents=True, exist_ok=True)
        
        if self.config["memory_tracking"] and tracemalloc and not tracemalloc.is_tracing():
            try:
                tracemalloc.start()
            except Exception as e:
                logger.warning(f"Failed to start tracemalloc: {e}")

    @classmethod
    def get_instance(cls) -> "PerformanceProfiler":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def set_queue_caps(self, timeline_cap: int = _DEFAULT_TIMELINE_CAP,
                       histogram_cap: int = _DEFAULT_HISTOGRAM_CAP,
                       timing_cap: int = _DEFAULT_TIMING_CAP):
        """
        Runtime-configurable queue size caps for bounded memory growth.
        Call this from desktop settings or enterprise deployment configs.
        """
        self._timeline_cap = timeline_cap
        self._histogram_cap = histogram_cap
        self._timing_cap = timing_cap
        logger.info(f"Telemetry caps updated: timeline={timeline_cap}, histogram={histogram_cap}, timing={timing_cap}")

    def set_profile(self, profile_name: str):
        if profile_name in self._profiles:
            self.profile_name = profile_name
            self.config = self._profiles[profile_name]
            logger.info(f"PerformanceProfiler profile set to: {profile_name}")
            
            # Start/stop tracemalloc based on profile setting
            if self.config["memory_tracking"] and tracemalloc:
                if not tracemalloc.is_tracing():
                    try:
                        tracemalloc.start()
                    except Exception as e:
                        logger.warning(f"Failed to start tracemalloc: {e}")
            elif not self.config["memory_tracking"] and tracemalloc and tracemalloc.is_tracing():
                try:
                    tracemalloc.stop()
                except Exception as e:
                    logger.warning(f"Failed to stop tracemalloc: {e}")

    @contextmanager
    def context(self, name: str, **metadata) -> Generator[None, None, None]:
        """Hierarchical context manager to profile time and memory."""
        # Check sampling rate based on seed or simple counter
        import random
        sampled = random.random() <= self.config["sampling_rate"]
        
        if not sampled:
            yield
            return

        full_name = "/".join(self.context_stack + [name])
        self.context_stack.append(name)
        
        start_time = time.perf_counter()
        
        start_mem = 0
        if self.config["memory_tracking"] and tracemalloc and tracemalloc.is_tracing():
            try:
                start_mem, _ = tracemalloc.get_traced_memory()
            except Exception:
                pass
                
        try:
            yield
        finally:
            end_time = time.perf_counter()
            duration = end_time - start_time
            
            self.context_stack.pop()
            
            # Save duration — enforce timing cap (drop oldest sample to preserve recency)
            if full_name not in self.timings:
                self.timings[full_name] = []
            bucket = self.timings[full_name]
            if len(bucket) >= self._timing_cap:
                bucket.pop(0)  # FIFO eviction: remove oldest sample
                self._drops["timing"] += 1
                self.set_gauge("backpressure.timing_drops_total", float(self._drops["timing"]))
            bucket.append(duration)
            
            # Track memory delta if enabled
            if self.config["memory_tracking"] and tracemalloc and tracemalloc.is_tracing():
                try:
                    end_mem, _ = tracemalloc.get_traced_memory()
                    mem_delta = end_mem - start_mem
                    if full_name not in self.memory_deltas:
                        self.memory_deltas[full_name] = []
                    self.memory_deltas[full_name].append(mem_delta)
                except Exception:
                    pass

            # Update op count & throughput
            self.op_counts[full_name] = self.op_counts.get(full_name, 0) + 1
            
            if full_name not in self.throughput_emas:
                self.throughput_emas[full_name] = EMACalculator(alpha=0.1)
                
            # Instant throughput is 1 / duration
            inst_throughput = 1.0 / duration if duration > 0 else 0.0
            avg_throughput = self.throughput_emas[full_name].update(inst_throughput)
            
            # Emit live metrics
            stats = self._get_stats_for_key(full_name)
            stats["context"] = full_name
            stats["timestamp"] = datetime.now().isoformat()
            self.metrics_updated.emit(stats)

    def record_event(self, event_name: str, details: Optional[Dict[str, Any]] = None):
        """Records an operational timeline event. Enforces bounded timeline cap."""
        if len(self.timeline_events) >= self._timeline_cap:
            self.timeline_events.pop(0)  # FIFO eviction
            self._drops["timeline"] += 1
            self.set_gauge("backpressure.timeline_drops_total", float(self._drops["timeline"]))
        self.timeline_events.append({
            "timestamp": datetime.now().isoformat(),
            "event": event_name,
            "details": details or {}
        })

    def set_gauge(self, name: str, value: float):
        """Sets a real-time operational gauge."""
        self.gauges[name] = value

    def record_histogram(self, name: str, value: float):
        """Records a value into a named histogram bucket. Enforces bounded cap."""
        if name not in self.histograms:
            self.histograms[name] = []
        bucket = self.histograms[name]
        if len(bucket) >= self._histogram_cap:
            bucket.pop(0)  # FIFO eviction
            self._drops["histogram"] += 1
            self.set_gauge("backpressure.histogram_drops_total", float(self._drops["histogram"]))
        bucket.append(value)

    def calculate_eta(self, remaining_checks: int, current_concurrency: int, provider_tracker: "ProviderMetricsTracker", provider_id: str) -> float:
        """
        Calculates remaining execution ETA based on exponentially-smoothed throughput
        and concurrent checks execution times.
        """
        if remaining_checks <= 0:
            return 0.0
        
        metrics = provider_tracker.get_metrics(provider_id)
        est_duration_ms = metrics.get("estimated_check_duration_ms", 150.0)
        
        # ETA = (remaining_checks * estimated_check_duration) / (current_concurrency)
        effective_concurrency = max(1, current_concurrency)
        eta_seconds = (remaining_checks * (est_duration_ms / 1000.0)) / effective_concurrency
        return eta_seconds

    def _get_stats_for_key(self, key: str) -> Dict[str, Any]:
        """Calculate statistics for a specific key."""
        durations = self.timings.get(key, [])
        if not durations:
            return {}
            
        sorted_durs = sorted(durations)
        count = len(sorted_durs)
        
        # Calculate percentiles
        def get_percentile(p: float) -> float:
            idx = max(0, min(count - 1, int(math.ceil((count * p) / 100.0)) - 1))
            return sorted_durs[idx] * 1000.0  # Convert to milliseconds

        p50 = get_percentile(50.0)
        p95 = get_percentile(95.0)
        p99 = get_percentile(99.0)
        p99_9 = get_percentile(99.9)
        mean_val = (sum(sorted_durs) / count) * 1000.0
        
        # Memory stats
        mem_deltas = self.memory_deltas.get(key, [])
        avg_mem_delta = sum(mem_deltas) / len(mem_deltas) if mem_deltas else 0.0
        max_mem_delta = max(mem_deltas) if mem_deltas else 0
        
        avg_tp = self.throughput_emas.get(key).value if key in self.throughput_emas else 0.0

        return {
            "count": count,
            "mean_ms": mean_val,
            "p50_ms": p50,
            "p95_ms": p95,
            "p99_ms": p99,
            "p99_9_ms": p99_9,
            "avg_throughput_ops_sec": avg_tp,
            "avg_mem_delta_bytes": avg_mem_delta,
            "max_mem_delta_bytes": max_mem_delta
        }

    def generate_report(self) -> Dict[str, Any]:
        """Generates a complete operational performance report."""
        report = {
            "profile": self.profile_name,
            "generated_at": datetime.now().isoformat(),
            "metrics": {},
            "gauges": self.gauges,
            "timeline": self.timeline_events,
            "backpressure": {
                "timeline_drops": self._drops["timeline"],
                "histogram_drops": self._drops["histogram"],
                "timing_drops": self._drops["timing"],
                "timeline_cap": self._timeline_cap,
                "histogram_cap": self._histogram_cap,
                "timing_cap": self._timing_cap,
            }
        }
        for key in self.timings.keys():
            report["metrics"][key] = self._get_stats_for_key(key)
        return report

    def export_to_json(self, filepath: str) -> bool:
        """Exports metrics report as JSON."""
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.generate_report(), f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Failed to export JSON metrics: {e}")
            return False

    def export_to_csv(self, filepath: str) -> bool:
        """Exports metrics as CSV file."""
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Context", "Count", "Mean (ms)", "p50 (ms)", "p95 (ms)", "p99 (ms)", "Throughput (ops/sec)", "Avg Memory Delta (bytes)"])
                for key in self.timings.keys():
                    stats = self._get_stats_for_key(key)
                    writer.writerow([
                        key,
                        stats.get("count", 0),
                        f"{stats.get('mean_ms', 0.0):.2f}",
                        f"{stats.get('p50_ms', 0.0):.2f}",
                        f"{stats.get('p95_ms', 0.0):.2f}",
                        f"{stats.get('p99_ms', 0.0):.2f}",
                        f"{stats.get('avg_throughput_ops_sec', 0.0):.2f}",
                        f"{stats.get('avg_mem_delta_bytes', 0.0):.2f}"
                    ])
            return True
        except Exception as e:
            logger.error(f"Failed to export CSV metrics: {e}")
            return False

    def to_prometheus_format(self) -> str:
        """Generates raw Prometheus openmetrics formatted payload string."""
        lines = []
        # Gauges
        for name, val in self.gauges.items():
            prom_name = name.replace(".", "_").replace("/", "_")
            lines.append(f"# HELP avaguard_{prom_name} Telemetry gauge metric")
            lines.append(f"# TYPE avaguard_{prom_name} gauge")
            lines.append(f"avaguard_{prom_name} {val}")
            
        # Timings (Summary format)
        for key in self.timings.keys():
            stats = self._get_stats_for_key(key)
            prom_name = key.replace(".", "_").replace("/", "_")
            lines.append(f"# HELP avaguard_{prom_name}_latency_ms Context timing metric in milliseconds")
            lines.append(f"# TYPE avaguard_{prom_name}_latency_ms summary")
            lines.append(f"avaguard_{prom_name}_latency_ms{{quantile=\"0.50\"}} {stats.get('p50_ms', 0.0)}")
            lines.append(f"avaguard_{prom_name}_latency_ms{{quantile=\"0.95\"}} {stats.get('p95_ms', 0.0)}")
            lines.append(f"avaguard_{prom_name}_latency_ms{{quantile=\"0.99\"}} {stats.get('p99_ms', 0.0)}")
            lines.append(f"avaguard_{prom_name}_latency_ms_sum {stats.get('mean_ms', 0.0) * stats.get('count', 0)}")
            lines.append(f"avaguard_{prom_name}_latency_ms_count {stats.get('count', 0)}")

        # Backpressure / drop counters
        for drop_key, drop_val in self._drops.items():
            lines.append(f"# HELP avaguard_backpressure_{drop_key}_drops_total Telemetry {drop_key} eviction drop counter")
            lines.append(f"# TYPE avaguard_backpressure_{drop_key}_drops_total counter")
            lines.append(f"avaguard_backpressure_{drop_key}_drops_total {drop_val}")

        return "\n".join(lines)

    def save_report(self) -> Path:
        """Saves current telemetry report to file."""
        report = self.generate_report()
        filename = f"telemetry_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = self.perf_log_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        logger.info(f"Saved performance report to: {filepath}")
        return filepath

    def clear(self):
        """Clears accumulated profiles and resets drop counters."""
        self.timings.clear()
        self.memory_deltas.clear()
        self.op_counts.clear()
        self.throughput_emas.clear()
        self.context_stack.clear()
        self.timeline_events.clear()
        self.gauges.clear()
        self.histograms.clear()
        self._drops = {"timeline": 0, "histogram": 0, "timing": 0}


class ProviderMetricsTracker:
    """
    Tracks cloud provider endpoint performance with EMA smoothing, error rate monitoring,
    throttling tracking, and estimated durations.
    """
    def __init__(self, alpha: float = 0.15):
        self.alpha = alpha
        # provider -> metric_name -> value
        self.metrics: Dict[str, Dict[str, Any]] = {}

    def get_or_create_provider(self, provider_id: str) -> Dict[str, Any]:
        if provider_id not in self.metrics:
            self.metrics[provider_id] = {
                "response_time_ema_ms": EMACalculator(alpha=self.alpha, initial_value=200.0),
                "error_rate_ema": EMACalculator(alpha=0.05, initial_value=0.0),
                "throttle_count": 0,
                "success_count": 0,
                "error_count": 0,
                "estimated_check_duration_ms": 150.0  # Seed value
            }
        return self.metrics[provider_id]

    def record_success(self, provider_id: str, duration_ms: float):
        p = self.get_or_create_provider(provider_id)
        p["success_count"] += 1
        p["response_time_ema_ms"].update(duration_ms)
        p["error_rate_ema"].update(0.0)
        
        # Smoothed estimated check duration
        current_est = p["estimated_check_duration_ms"]
        p["estimated_check_duration_ms"] = (0.2 * duration_ms) + (0.8 * current_est)

    def record_error(self, provider_id: str):
        p = self.get_or_create_provider(provider_id)
        p["error_count"] += 1
        p["error_rate_ema"].update(1.0)

    def record_throttle(self, provider_id: str):
        p = self.get_or_create_provider(provider_id)
        p["throttle_count"] += 1
        p["error_rate_ema"].update(1.0)

    def get_metrics(self, provider_id: str) -> Dict[str, Any]:
        p = self.get_or_create_provider(provider_id)
        return {
            "response_time_ema_ms": p["response_time_ema_ms"].value,
            "error_rate": p["error_rate_ema"].value,
            "throttle_count": p["throttle_count"],
            "success_count": p["success_count"],
            "error_count": p["error_count"],
            "estimated_check_duration_ms": p["estimated_check_duration_ms"]
        }
