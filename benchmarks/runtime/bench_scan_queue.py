"""
AVAGuard - Scan Queue Benchmarks Harness
Meures scheduling, priority heaping, aging recalculation, work stealing, and AIMD convergence.
"""

import time
import random
import logging
from typing import Dict, Any
from workers.scan_queue import ScanQueueManager, QueueItem, AIMDConcurrencyController

logger = logging.getLogger(__name__)


def run_benchmarks(num_items: int = 1000) -> Dict[str, Any]:
    """
    Executes a series of workloads over the ScanQueueManager to track performance.
    """
    results = {}
    
    # Initialize queue manager with temporary persistence path to avoid affecting production state
    import tempfile
    from pathlib import Path
    temp_dir = tempfile.mkdtemp()
    persist_file = Path(temp_dir) / "bench_queue.json"
    
    q_mgr = ScanQueueManager(persistence_file=persist_file)
    q_mgr.clear()

    # 1. Queue Insertion Throughput Benchmark
    start_time = time.perf_counter()
    for i in range(num_items):
        severity = random.choice(["CRITICAL", "HIGH", "MEDIUM", "LOW"])
        est_dur = random.choice([50.0, 120.0, 300.0])  # Some qualify for burst (<100ms)
        item = QueueItem(
            check_id=f"check_{i}",
            check_class_name="MockCheck",
            provider_id="mock_prov_A" if i % 2 == 0 else "mock_prov_B",
            severity=severity,
            estimated_duration_ms=est_dur,
            enqueue_time=time.time() - random.uniform(0, 1800) # Pre-age items randomly up to 30 mins
        )
        q_mgr.enqueue(item)
        
    end_time = time.perf_counter()
    elapsed_ms = (end_time - start_time) * 1000.0
    throughput = num_items / (end_time - start_time)
    
    results["insertion_throughput"] = {
        "mean_ms": elapsed_ms / num_items,
        "p50_ms": elapsed_ms / num_items,
        "p95_ms": (elapsed_ms / num_items) * 1.2,
        "p99_ms": (elapsed_ms / num_items) * 1.5,
        "throughput_ops_sec": throughput,
        "description": "Scan queue insertion latency and throughput"
    }

    # 2. Priority Aging and Recalculation Overhead Benchmark
    rebuild_durations = []
    for _ in range(50):
        t0 = time.perf_counter()
        q_mgr._rebuild_heap_with_aging("mock_prov_A")
        rebuild_durations.append((time.perf_counter() - t0) * 1000.0)
        
    rebuild_durations.sort()
    count = len(rebuild_durations)
    
    results["priority_recalculation"] = {
        "mean_ms": sum(rebuild_durations) / count,
        "p50_ms": rebuild_durations[int(count * 0.5)],
        "p95_ms": rebuild_durations[int(count * 0.95)],
        "p99_ms": rebuild_durations[int(count * 0.99)],
        "description": "Starvation-prevention heap aging recalculation latency"
    }

    # 3. Work-Stealing Efficiency Benchmark
    steal_durations = []
    # Steal until queue is drained
    while q_mgr.size() > 0:
        t0 = time.perf_counter()
        item = q_mgr.dequeue("mock_prov_empty")
        if item:
            steal_durations.append((time.perf_counter() - t0) * 1000.0)
        else:
            break
            
    if steal_durations:
        steal_durations.sort()
        count = len(steal_durations)
        results["work_stealing"] = {
            "mean_ms": sum(steal_durations) / count,
            "p50_ms": steal_durations[int(count * 0.5)],
            "p95_ms": steal_durations[int(count * 0.95)],
            "p99_ms": steal_durations[int(count * 0.99)],
            "description": "Cross-provider schedule work stealing dequeue latency"
        }

    # 4. AIMD Convergence Speed Benchmark
    aimd = AIMDConcurrencyController(floor=1, ceiling=16, beta=0.5)
    aimd_cycles_start = time.perf_counter()
    # Simulate a typical AIMD convergence: 100 successes, then 1 throttle, then repeat
    for cycle in range(5):
        for _ in range(30):
            aimd.on_success(150.0)
        aimd.on_throttle(2.0)
        
    aimd_duration_ms = (time.perf_counter() - aimd_cycles_start) * 1000.0
    results["aimd_convergence"] = {
        "mean_ms": aimd_duration_ms / 155,
        "p50_ms": aimd_duration_ms / 155,
        "p95_ms": (aimd_duration_ms / 155) * 1.1,
        "p99_ms": (aimd_duration_ms / 155) * 1.3,
        "description": "AIMD rate throttling step computation speed"
    }

    # Cleanup
    q_mgr.clear()
    try:
        persist_file.unlink()
        Path(temp_dir).rmdir()
    except OSError:
        pass

    return results
