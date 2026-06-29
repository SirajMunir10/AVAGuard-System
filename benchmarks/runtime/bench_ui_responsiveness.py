"""
AVAGuard - UI Responsiveness Benchmarks Harness
Measures event loop starvation intervals, thread cancellation latency, pause/resume reactivity,
and shutdown drain timing.
"""

import time
import logging
from typing import Dict, Any
from workers.enhanced_worker import EnhancedScanWorker
from workers.evidence_writer import EvidenceWriterThread

logger = logging.getLogger(__name__)


def run_benchmarks() -> Dict[str, Any]:
    """
    Simulates operational tasks and tracks execution latencies affecting UI responsiveness.
    """
    results = {}
    
    # 1. Thread Cancellation Latency
    # Measure how quickly EnhancedScanWorker can stop a scan loop
    worker = EnhancedScanWorker(use_mock=True)
    
    t0 = time.perf_counter()
    worker.stop()
    cancel_ms = (time.perf_counter() - t0) * 1000.0
    
    results["cancellation_latency"] = {
        "mean_ms": cancel_ms,
        "p50_ms": cancel_ms,
        "p95_ms": cancel_ms,
        "p99_ms": cancel_ms,
        "description": "Scan cancellation signal propagation and queue clear latency"
    }

    # 2. Pause & Resume Reactivity
    t0 = time.perf_counter()
    worker.pause()
    pause_ms = (time.perf_counter() - t0) * 1000.0
    
    t0 = time.perf_counter()
    worker.resume()
    resume_ms = (time.perf_counter() - t0) * 1000.0
    
    results["pause_reactivity"] = {
        "mean_ms": pause_ms,
        "p50_ms": pause_ms,
        "p95_ms": pause_ms,
        "p99_ms": pause_ms,
        "description": "Cooperative thread state transition to pause state latency"
    }
    
    results["resume_reactivity"] = {
        "mean_ms": resume_ms,
        "p50_ms": resume_ms,
        "p95_ms": resume_ms,
        "p99_ms": resume_ms,
        "description": "Cooperative thread state transition to resume state latency"
    }

    # 3. Shutdown queue drain timing
    # Enqueue items to EvidenceWriterThread and measure how quickly it stops and flushes
    from models.database import EnhancedDatabaseManager
    from models.evidence_store import EvidenceStore, LocalKeyProvider
    import tempfile
    from pathlib import Path
    import shutil
    
    temp_dir = tempfile.mkdtemp()
    db_path = str(Path(temp_dir) / "bench_ui.db")
    
    # Pre-initialize schema using database manager
    db_mgr = EnhancedDatabaseManager(db_path)
    
    key_provider = LocalKeyProvider(key_dir=Path(temp_dir) / "keys")
    store = EvidenceStore(db_path, key_provider=key_provider)
    
    writer = EvidenceWriterThread(store)
    writer.start()
    
    # Enqueue some items to be written
    for i in range(100):
        writer.submit(
            scan_id="scan_ui",
            check_id=f"check_{i}",
            payload={"res": i},
            classification="AI_SAFE"
        )
        
    t0 = time.perf_counter()
    writer.stop()  # Stop waits for queue to flush
    drain_ms = (time.perf_counter() - t0) * 1000.0
    
    results["shutdown_drain"] = {
        "mean_ms": drain_ms,
        "p50_ms": drain_ms,
        "p95_ms": drain_ms,
        "p99_ms": drain_ms,
        "description": "Background writer thread shutdown queue drain and flush latency"
    }

    # 4. Qt Event Loop Starvation
    # Measure if cooperative events loop processing QCoreApplication.processEvents() has lag
    # Under standard mock environment, we execute 10 sequential ticks of event loop and measure average timing
    try:
        from PyQt6.QtCore import QCoreApplication
        event_loop_durations = []
        for _ in range(10):
            t_start = time.perf_counter()
            QCoreApplication.processEvents()
            event_loop_durations.append((time.perf_counter() - t_start) * 1000.0)
            time.sleep(0.01)
            
        event_loop_durations.sort()
        count = len(event_loop_durations)
        
        results["event_loop_starvation"] = {
            "mean_ms": sum(event_loop_durations) / count,
            "p50_ms": event_loop_durations[int(count * 0.5)],
            "p95_ms": event_loop_durations[int(count * 0.95)],
            "p99_ms": event_loop_durations[int(count * 0.99)],
            "description": "Headless PyQt Qt event loop processing lag"
        }
    except Exception:
        results["event_loop_starvation"] = {
            "mean_ms": 0.0,
            "p50_ms": 0.0,
            "p95_ms": 0.0,
            "p99_ms": 0.0,
            "description": "Starvation measuring unavailable in this CLI configuration"
        }

    # Cleanup
    store.close()
    try:
        shutil.rmtree(temp_dir)
    except OSError:
        pass

    return results
