"""
Tests for ScanQueueManager, Concurrency Controllers, Priority Scorer, and Backpressure Circuit Breaker.
"""

import os
import json
import time
import pytest
from pathlib import Path
from collections import deque

from workers.scan_queue import (
    AIMDConcurrencyController,
    ScanPriorityScorer,
    BackpressurePolicy,
    QueueItem,
    ScanQueueManager,
    decorrelated_jitter_delay
)


def test_queue_item_serialization():
    item = QueueItem(
        check_id="1.1.1",
        check_class_name="CheckMFAEnabled",
        provider_id="azure",
        severity="HIGH",
        manual_boost=1.5,
        estimated_duration_ms=120.0
    )
    
    d = item.to_dict()
    assert d["check_id"] == "1.1.1"
    assert d["provider_id"] == "azure"
    assert d["severity"] == "HIGH"
    assert d["manual_boost"] == 1.5
    assert d["estimated_duration_ms"] == 120.0

    restored = QueueItem.from_dict(d)
    assert restored.check_id == item.check_id
    assert restored.check_class_name == item.check_class_name
    assert restored.provider_id == item.provider_id
    assert restored.severity == item.severity
    assert restored.manual_boost == item.manual_boost
    assert restored.estimated_duration_ms == item.estimated_duration_ms


def test_aimd_concurrency_controller():
    controller = AIMDConcurrencyController(floor=1, ceiling=6, beta=0.5, additive_step=1)
    
    # Start value should be within limits
    assert 1 <= controller.current_limit() <= 6
    
    # Successful execution should add to limit
    # AIMD adds fractional step per success: additive_step / current_limit
    limit_start = controller.current_limit()
    # We perform success ticks to force increase by 1
    for _ in range(limit_start):
        controller.on_success(150.0)
        
    assert controller.current_limit() == limit_start + 1

    # Cap ceiling check
    for _ in range(50):
        controller.on_success(100.0)
    assert controller.current_limit() == 6

    # Throttling event drops concurrency multiplicatively
    controller.on_throttle(2.0)
    assert controller.current_limit() == 3  # 6 * 0.5 = 3

    # Error reduces limit by 1
    controller.on_error()
    assert controller.current_limit() == 2

    # Floor limit check
    controller.on_throttle(1.0)
    controller.on_throttle(1.0)
    assert controller.current_limit() == 1


def test_scan_priority_scorer():
    scorer = ScanPriorityScorer()
    
    # Base check: higher severity yields lower min-heap score (priority pop)
    score_critical = scorer.compute_score(severity="CRITICAL", time_in_queue_s=0, retry_count=0)
    score_high = scorer.compute_score(severity="HIGH", time_in_queue_s=0, retry_count=0)
    score_low = scorer.compute_score(severity="LOW", time_in_queue_s=0, retry_count=0)
    
    # Critical should be popped before High, High before Low (more negative is prioritized first)
    assert score_critical < score_high
    assert score_high < score_low

    # Time-decay (aging) check: older items have lower score (higher priority)
    score_fresh = scorer.compute_score(severity="HIGH", time_in_queue_s=0, retry_count=0)
    score_aged = scorer.compute_score(severity="HIGH", time_in_queue_s=600, retry_count=0) # 10 mins old
    assert score_aged < score_fresh

    # Retry penalty check: items that have failed are penalized (less priority)
    score_no_retry = scorer.compute_score(severity="HIGH", time_in_queue_s=0, retry_count=0)
    score_retried = scorer.compute_score(severity="HIGH", time_in_queue_s=0, retry_count=3)
    assert score_no_retry < score_retried  # score_retried is more positive/less prioritized

    # Manual boost check: manual booster raises priority (lower score)
    score_no_boost = scorer.compute_score(severity="HIGH", time_in_queue_s=0, retry_count=0, manual_boost=0)
    score_boosted = scorer.compute_score(severity="HIGH", time_in_queue_s=0, retry_count=0, manual_boost=5.0)
    assert score_boosted < score_no_boost


def test_backpressure_policy():
    policy = BackpressurePolicy(base_cooldown_s=0.2, max_cooldown_s=1.0)
    
    assert policy.state == policy.CLOSED
    assert policy.can_dispatch() is True

    # Trip the circuit breaker
    policy.record_throttle(retry_after_s=0.1)
    assert policy.state == policy.OPEN
    assert policy.can_dispatch() is False

    # Check cooldown blocks dispatches
    time.sleep(0.05)
    assert policy.can_dispatch() is False

    # Cooldown finishes, moves to HALF_OPEN probe phase
    time.sleep(0.06)
    assert policy.can_dispatch() is True
    assert policy.state == policy.HALF_OPEN
    assert policy.probe_active is True

    # Additional requests should block while probe is outstanding
    assert policy.can_dispatch() is False

    # Probe success resets to CLOSED
    policy.record_success()
    assert policy.state == policy.CLOSED
    assert policy.can_dispatch() is True
    assert policy.probe_active is False


def test_backpressure_probe_failure():
    policy = BackpressurePolicy(base_cooldown_s=0.1)
    policy.record_throttle()
    
    # Transition to half open
    time.sleep(0.12)
    assert policy.can_dispatch() is True
    assert policy.state == policy.HALF_OPEN
    
    # Probe fails, trips back to OPEN
    policy.reject_probe()
    assert policy.state == policy.OPEN


def test_scan_queue_manager_basic_operations(tmp_path):
    persistence_file = tmp_path / "test_queue.json"
    queue = ScanQueueManager(persistence_file=persistence_file)
    
    item_crit = QueueItem(check_id="1.1", check_class_name="C1", provider_id="azure", severity="CRITICAL", estimated_duration_ms=150.0)
    item_low = QueueItem(check_id="1.2", check_class_name="C2", provider_id="azure", severity="LOW", estimated_duration_ms=150.0)
    
    queue.enqueue(item_low)
    queue.enqueue(item_crit)
    
    assert queue.size() == 2
    
    # Priority dequeue should return CRITICAL check first
    dequeued_1 = queue.dequeue("azure")
    assert dequeued_1.check_id == "1.1"
    
    dequeued_2 = queue.dequeue("azure")
    assert dequeued_2.check_id == "1.2"
    
    assert queue.size() == 0


def test_scan_queue_manager_burst_bypass(tmp_path):
    persistence_file = tmp_path / "test_queue_burst.json"
    queue = ScanQueueManager(persistence_file=persistence_file)
    
    # Item with < 100ms should skip priority queue and enter burst deque
    item_heavy = QueueItem(check_id="heavy", check_class_name="C1", provider_id="azure", severity="CRITICAL", estimated_duration_ms=250.0)
    item_burst = QueueItem(check_id="burst", check_class_name="C2", provider_id="azure", severity="LOW", estimated_duration_ms=50.0)
    
    queue.enqueue(item_heavy)
    queue.enqueue(item_burst)
    
    # Dequeue should prioritize native burst deque over priority heap even though heavy is CRITICAL
    first = queue.dequeue("azure")
    assert first.check_id == "burst"
    
    second = queue.dequeue("azure")
    assert second.check_id == "heavy"


def test_scan_queue_manager_work_stealing(tmp_path):
    persistence_file = tmp_path / "test_queue_steal.json"
    queue = ScanQueueManager(persistence_file=persistence_file)
    
    # Enqueue multiple heavy items to azure queue
    for i in range(5):
        queue.enqueue(QueueItem(
            check_id=f"az_{i}",
            check_class_name="C",
            provider_id="azure",
            severity="HIGH",
            estimated_duration_ms=200.0
        ))
        
    # aws queue is empty, aws thread dequeues
    stolen = queue.dequeue("aws")
    assert stolen is not None
    assert stolen.provider_id == "aws"  # Stolen item gets remapped to AWS executor
    assert stolen.check_id.startswith("az_")
    
    # AWS queue now has 4 left in Azure heap
    assert queue.size() == 4


def test_scan_queue_persistence_and_recovery(tmp_path):
    persistence_file = tmp_path / "test_queue_persist.json"
    queue = ScanQueueManager(persistence_file=persistence_file)
    
    item1 = QueueItem(check_id="1", check_class_name="C", provider_id="azure", severity="HIGH", estimated_duration_ms=150.0)
    item2 = QueueItem(check_id="2", check_class_name="C", provider_id="azure", severity="LOW", estimated_duration_ms=50.0)  # burst
    
    queue.enqueue(item1)
    queue.enqueue(item2)
    
    assert persistence_file.exists()
    
    # Create new manager pointing to same recovery file
    recovered_queue = ScanQueueManager(persistence_file=persistence_file)
    assert recovered_queue.size() == 2
    
    # Burst pops first
    assert recovered_queue.dequeue("azure").check_id == "2"
    assert recovered_queue.dequeue("azure").check_id == "1"
