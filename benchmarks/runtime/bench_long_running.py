#!/usr/bin/env python
"""
AVAGuard Long-Running Stability & Resource Leak Benchmark
Monitors thread counts, open handles, heap growth, WAL growth, and queue depth over
a continuous loop, asserting leak thresholds and storing historical runs for trend tracking.
Enhanced with GC pressure metrics, SQL operation timing (store/retrieve p50/p95/p99),
retry simulation, and enriched historical trend persistence.
"""

import os
import sys
import time
import json
import threading
import tempfile
import gc  # Built-in GC instrumentation — zero external dependency
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Resolve absolute paths
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "desktop_app"))
sys.path.insert(0, str(project_root / "avaguard-core"))

# PyQt6 Headless Mocking to prevent silent Windows process crashes
from unittest.mock import MagicMock
import unittest.mock

class MockQObject:
    def __init__(self, *args, **kwargs): pass
    def parent(self): return None
    def setParent(self, parent): pass

class MockPyqtSignal:
    def __init__(self, *args, **kwargs): pass
    def emit(self, *args, **kwargs): pass
    def connect(self, *args, **kwargs): pass
    def disconnect(self, *args, **kwargs): pass

mock_qtcore = MagicMock()
mock_qtcore.QObject = MockQObject
mock_qtcore.pyqtSignal = lambda *args, **kwargs: MockPyqtSignal()
mock_qtcore.QThread = MagicMock
mock_qtcore.QRunnable = object
mock_qtcore.QTimer = MagicMock
mock_qtcore.QSize = MagicMock
mock_qtcore.QUrl = MagicMock

sys.modules['PyQt6'] = MagicMock()
sys.modules['PyQt6.QtWidgets'] = MagicMock()
sys.modules['PyQt6.QtCore'] = mock_qtcore
sys.modules['PyQt6.QtGui'] = MagicMock()

# Optional dependencies import with safe fallbacks
try:
    import psutil
except ImportError:
    psutil = None

from desktop_app.models.evidence_store import EvidenceStore
from desktop_app.workers.scan_queue import ScanQueueManager, QueueItem
from desktop_app.workers.telemetry import PerformanceProfiler


# ---------------------------------------------------------------------------
# GC Pressure Instrumentation
# ---------------------------------------------------------------------------

class GCMetricsCollector:
    """
    Tracks Python garbage collector pressure across all three generations.
    Uses built-in `gc` module — zero runtime overhead in production builds.
    """

    def __init__(self):
        self.baseline_counts = list(gc.get_count())
        self.baseline_stats = list(gc.get_stats()) if hasattr(gc, "get_stats") else []
        self.collection_events: List[Dict[str, Any]] = []

    def snapshot(self, label: str) -> Dict[str, Any]:
        """Captures current GC collection counts and object pressure per generation."""
        counts = gc.get_count()
        stats = gc.get_stats() if hasattr(gc, "get_stats") else [{}, {}, {}]
        snap = {
            "label": label,
            "timestamp": datetime.now().isoformat(),
            "gen0_count": counts[0],
            "gen1_count": counts[1],
            "gen2_count": counts[2],
            "gen0_collections": stats[0].get("collections", 0) if stats else 0,
            "gen1_collections": stats[1].get("collections", 0) if len(stats) > 1 else 0,
            "gen2_collections": stats[2].get("collections", 0) if len(stats) > 2 else 0,
            "gen0_collected": stats[0].get("collected", 0) if stats else 0,
            "gen1_collected": stats[1].get("collected", 0) if len(stats) > 1 else 0,
            "gen2_collected": stats[2].get("collected", 0) if len(stats) > 2 else 0,
        }
        self.collection_events.append(snap)
        return snap

    def delta_from_baseline(self) -> Dict[str, int]:
        """Returns the GC unreachable object count delta from baseline snapshot."""
        current = gc.get_count()
        return {
            "gen0_delta": current[0] - self.baseline_counts[0],
            "gen1_delta": current[1] - self.baseline_counts[1],
            "gen2_delta": current[2] - self.baseline_counts[2],
        }

    def summarize(self) -> Dict[str, Any]:
        """Returns a consolidated GC pressure summary over the entire benchmark run."""
        if not self.collection_events:
            return {}
        last = self.collection_events[-1]
        return {
            "total_snapshots": len(self.collection_events),
            "final_gen0_count": last["gen0_count"],
            "final_gen1_count": last["gen1_count"],
            "final_gen2_count": last["gen2_count"],
            "total_gen0_collected": last["gen0_collected"],
            "total_gen1_collected": last["gen1_collected"],
            "total_gen2_collected": last["gen2_collected"],
            "total_gen0_collections": last["gen0_collections"],
            "total_gen1_collections": last["gen1_collections"],
            "delta": self.delta_from_baseline(),
        }


# ---------------------------------------------------------------------------
# SQL Operation Timing Tracker
# ---------------------------------------------------------------------------

class SQLTimingTracker:
    """
    Tracks store/retrieve SQL operation durations with rolling p50/p95/p99 percentile
    calculation, error counters, and retry event instrumentation.
    """

    def __init__(self):
        self.store_durations_ms: List[float] = []
        self.retrieve_durations_ms: List[float] = []
        self.store_errors: int = 0
        self.retrieve_errors: int = 0
        self.retry_count: int = 0  # Tracks simulated retry attempts

    def record_store(self, duration_ms: float, is_retry: bool = False):
        """Records a successful store operation duration."""
        self.store_durations_ms.append(duration_ms)
        if is_retry:
            self.retry_count += 1

    def record_retrieve(self, duration_ms: float):
        """Records a successful retrieve operation duration."""
        self.retrieve_durations_ms.append(duration_ms)

    def record_store_error(self):
        self.store_errors += 1

    def record_retrieve_error(self):
        self.retrieve_errors += 1

    @staticmethod
    def _percentile(data: List[float], pct: float) -> float:
        """Calculates the given percentile from a duration sample list."""
        if not data:
            return 0.0
        sorted_d = sorted(data)
        idx = max(0, min(len(sorted_d) - 1, int(len(sorted_d) * pct / 100.0)))
        return round(sorted_d[idx], 3)

    def summary(self) -> Dict[str, Any]:
        """Returns a full summary of store/retrieve latency with percentile breakdown."""
        store = self.store_durations_ms
        retrieve = self.retrieve_durations_ms
        return {
            "store": {
                "count": len(store),
                "mean_ms": round(sum(store) / len(store), 3) if store else 0.0,
                "p50_ms": self._percentile(store, 50),
                "p95_ms": self._percentile(store, 95),
                "p99_ms": self._percentile(store, 99),
                "errors": self.store_errors,
            },
            "retrieve": {
                "count": len(retrieve),
                "mean_ms": round(sum(retrieve) / len(retrieve), 3) if retrieve else 0.0,
                "p50_ms": self._percentile(retrieve, 50),
                "p95_ms": self._percentile(retrieve, 95),
                "p99_ms": self._percentile(retrieve, 99),
                "errors": self.retrieve_errors,
            },
            "total_retry_events": self.retry_count,
        }


# ---------------------------------------------------------------------------
# Main Stability Monitor
# ---------------------------------------------------------------------------

class LongRunningStabilityMonitor:
    """
    Monitors resource metrics across a sustained iteration loop.
    Tracks thread counts, open handles, heap growth, WAL size,
    GC generation pressure, and SQL timing with percentile resolution.
    """
    
    def __init__(self, db_path: str, iterations: int = 50):
        self.db_path = Path(db_path)
        self.iterations = iterations
        self.profiler = PerformanceProfiler.get_instance()
        self.queue_manager = ScanQueueManager()
        
        # Initialize compliance database schema
        from desktop_app.models.database import EnhancedDatabaseManager
        self.db_mgr = EnhancedDatabaseManager(db_path)
        
        self.evidence_store = EvidenceStore(db_path=str(db_path))
        
        # Benchmarking directories
        self.history_dir = project_root / "benchmarks" / "history"
        self.history_dir.mkdir(parents=True, exist_ok=True)
        self.trend_file = self.history_dir / "long_running_trend.json"
        
        # Process context
        self.process = psutil.Process(os.getpid()) if psutil else None
        
        # Instrumentation helpers
        self.gc_monitor = GCMetricsCollector()
        self.sql_tracker = SQLTimingTracker()
        
        # Baseline snapshots
        self.baseline_threads = threading.active_count()
        self.baseline_memory = self._get_memory_mb()
        self.baseline_handles = self._get_handle_count()

    def _get_memory_mb(self) -> float:
        """Returns heap Resident Set Size (RSS) in Megabytes."""
        if self.process:
            return self.process.memory_info().rss / 1024.0 / 1024.0
        return 0.0

    def _get_handle_count(self) -> int:
        """Returns active system handle count (file descriptors / Windows handles)."""
        if self.process:
            try:
                # Windows handle count
                if os.name == 'nt':
                    return self.process.num_handles()
                # Posix file descriptors
                return self.process.num_fds()
            except Exception:
                pass
        return 0

    def _get_wal_size_bytes(self) -> int:
        """Returns size of the database WAL file in bytes."""
        wal_path = Path(str(self.db_path) + "-wal")
        if wal_path.exists():
            return wal_path.stat().st_size
        return 0

    def execute_stability_loop(self) -> Dict[str, Any]:
        """Runs continuous scanning iterations and monitors metrics over time."""
        print(f"Starting Long-Running Stability Benchmark for {self.iterations} iterations...")
        print(f"Baselines: Threads={self.baseline_threads} | Memory={self.baseline_memory:.2f}MB | Handles={self.baseline_handles}")
        print("-" * 80)
        
        metrics_history: List[Dict[str, Any]] = []
        record_id: Optional[str] = None
        
        for i in range(1, self.iterations + 1):
            # 1. Simulate scan queue enqueue
            item = QueueItem(
                check_id=f"check_leak_{i}",
                check_class_name=f"CheckClass_{i}",
                provider_id="azure",
                severity="LOW"
            )
            self.queue_manager.enqueue(item)
            
            # 2. Timed evidence store with retry simulation (every 7th iteration is marked as retry)
            payload = {
                "iteration": i,
                "timestamp": time.time(),
                "metadata": {f"field_{k}": f"value_{k}" for k in range(20)}
            }
            is_retry_attempt = (i % 7 == 0)
            store_start = time.perf_counter()
            try:
                record_id = self.evidence_store.store_evidence(
                    scan_id=f"scan-stability-{i}",
                    check_id=f"check_leak_{i}",
                    payload=payload,
                    classification="confidential",
                    retention_days=1
                )
                store_ms = (time.perf_counter() - store_start) * 1000.0
                self.sql_tracker.record_store(store_ms, is_retry=is_retry_attempt)
            except Exception as store_exc:
                self.sql_tracker.record_store_error()
                print(f"  [WARN] Store error at iteration {i}: {store_exc}")
                record_id = None

            # 3. Timed evidence retrieve
            if record_id:
                retrieve_start = time.perf_counter()
                try:
                    self.evidence_store.retrieve_evidence(record_id)
                    retrieve_ms = (time.perf_counter() - retrieve_start) * 1000.0
                    self.sql_tracker.record_retrieve(retrieve_ms)
                except Exception as retr_exc:
                    self.sql_tracker.record_retrieve_error()

            # 4. Dequeue scan item
            self.queue_manager.dequeue("replay_engine")
            
            # 5. WAL checkpoint + GC snapshot at every 10th iteration
            if i % 10 == 0:
                self.evidence_store.checkpoint_wal()
                self.gc_monitor.snapshot(f"iter_{i}")
                
            # 6. Collect iteration-level resource metrics
            current_threads = threading.active_count()
            current_memory = self._get_memory_mb()
            current_handles = self._get_handle_count()
            current_wal = self._get_wal_size_bytes()
            current_queue = self.queue_manager.size()
            
            metrics = {
                "iteration": i,
                "thread_count": current_threads,
                "memory_mb": round(current_memory, 2),
                "handle_count": current_handles,
                "wal_size_bytes": current_wal,
                "queue_depth": current_queue
            }
            metrics_history.append(metrics)
            
            if i % 10 == 0 or i == self.iterations:
                gc_delta = self.gc_monitor.delta_from_baseline()
                print(
                    f"  Iteration {i:03d}/{self.iterations:03d} -> "
                    f"Threads={current_threads:2d} | Memory={current_memory:5.2f}MB | "
                    f"Handles={current_handles:4d} | WAL={current_wal:7d} B | "
                    f"GC_g0Δ={gc_delta['gen0_delta']}"
                )
                
            time.sleep(0.01)  # Light throttle to prevent CPU thrashing
            
        # Complete shutdown of instances before final leak measurement
        self.evidence_store.close()
        
        # 7. Final resource snapshot
        time.sleep(0.1)  # Brief yield for Python thread GC
        final_threads = threading.active_count()
        final_memory = self._get_memory_mb()
        final_handles = self._get_handle_count()
        
        thread_leak = max(0, final_threads - self.baseline_threads)
        memory_leak = max(0.0, final_memory - self.baseline_memory)
        handle_leak = max(0, final_handles - self.baseline_handles)
        
        # Aggregate GC and SQL summaries
        gc_summary = self.gc_monitor.summarize()
        sql_summary = self.sql_tracker.summary()

        results = {
            "timestamp": datetime.now().isoformat(),
            "iterations": self.iterations,
            "leak_summary": {
                "thread_leak": thread_leak,
                "memory_leak_mb": round(memory_leak, 2),
                "handle_leak": handle_leak
            },
            "gc_summary": gc_summary,
            "sql_timing": sql_summary,
            "metrics": metrics_history
        }

        # Print extended GC diagnostics
        print("\n--- GC Pressure Summary ---")
        delta = gc_summary.get("delta", {})
        print(f"  gen0 object delta:   {delta.get('gen0_delta', 'N/A')}")
        print(f"  gen1 object delta:   {delta.get('gen1_delta', 'N/A')}")
        print(f"  gen2 object delta:   {delta.get('gen2_delta', 'N/A')}")
        print(f"  gen0 collected:      {gc_summary.get('total_gen0_collected', 'N/A')}")
        print(f"  gen1 collected:      {gc_summary.get('total_gen1_collected', 'N/A')}")
        print(f"  gen2 collected:      {gc_summary.get('total_gen2_collected', 'N/A')}")
        print(f"  gen0 collections:    {gc_summary.get('total_gen0_collections', 'N/A')}")

        print("\n--- SQL Operation Timing ---")
        s = sql_summary["store"]
        r = sql_summary["retrieve"]
        print(f"  Store    — n={s['count']:4d}  mean={s['mean_ms']:7.2f}ms  p50={s['p50_ms']:7.2f}ms  p95={s['p95_ms']:7.2f}ms  p99={s['p99_ms']:7.2f}ms  errors={s['errors']}")
        print(f"  Retrieve — n={r['count']:4d}  mean={r['mean_ms']:7.2f}ms  p50={r['p50_ms']:7.2f}ms  p95={r['p95_ms']:7.2f}ms  p99={r['p99_ms']:7.2f}ms  errors={r['errors']}")
        print(f"  Retry events simulated: {sql_summary['total_retry_events']}")
        
        self.save_historical_trend(results)
        return results

    def save_historical_trend(self, results: Dict[str, Any]):
        """Persists enriched run record to historical JSON file for trend analysis."""
        trend_data: List[Dict[str, Any]] = []
        if self.trend_file.exists():
            try:
                with open(self.trend_file, "r") as f:
                    trend_data = json.load(f)
            except Exception:
                pass
                
        # Append enriched record with key aggregates for fast longitudinal queries
        sql = results.get("sql_timing", {})
        gc_sum = results.get("gc_summary", {})
        trend_data.append({
            "timestamp": results["timestamp"],
            "iterations": results["iterations"],
            # Resource leak indicators
            "thread_leak": results["leak_summary"]["thread_leak"],
            "memory_leak_mb": results["leak_summary"]["memory_leak_mb"],
            "handle_leak": results["leak_summary"]["handle_leak"],
            # SQL latency percentiles (store)
            "store_mean_ms": sql.get("store", {}).get("mean_ms", 0.0),
            "store_p95_ms": sql.get("store", {}).get("p95_ms", 0.0),
            "store_p99_ms": sql.get("store", {}).get("p99_ms", 0.0),
            "store_errors": sql.get("store", {}).get("errors", 0),
            # SQL latency percentiles (retrieve)
            "retrieve_mean_ms": sql.get("retrieve", {}).get("mean_ms", 0.0),
            "retrieve_p95_ms": sql.get("retrieve", {}).get("p95_ms", 0.0),
            "retrieve_p99_ms": sql.get("retrieve", {}).get("p99_ms", 0.0),
            "retrieve_errors": sql.get("retrieve", {}).get("errors", 0),
            # Retry simulation counter
            "retry_events": sql.get("total_retry_events", 0),
            # GC pressure indicators
            "gc_gen0_delta": gc_sum.get("delta", {}).get("gen0_delta", 0),
            "gc_gen1_delta": gc_sum.get("delta", {}).get("gen1_delta", 0),
            "gc_gen2_delta": gc_sum.get("delta", {}).get("gen2_delta", 0),
            "gc_gen0_collected": gc_sum.get("total_gen0_collected", 0),
            "gc_gen1_collected": gc_sum.get("total_gen1_collected", 0),
            "gc_gen0_collections": gc_sum.get("total_gen0_collections", 0),
        })
        
        # Cap at 50 historical records to bound file growth
        trend_data = trend_data[-50:]
        
        try:
            with open(self.trend_file, "w") as f:
                json.dump(trend_data, f, indent=2)
            print(f"\nHistorical trend updated: {self.trend_file}")
        except Exception as e:
            print(f"[WARN] Failed to save trend historical snapshots: {e}")

    def assert_stability_boundaries(self, results: Dict[str, Any]) -> bool:
        """Asserts resource safety and latency thresholds to enforce CI gating checks."""
        leak = results["leak_summary"]
        sql = results.get("sql_timing", {})
        success = True
        
        print("-" * 80)
        print("Stability Gating Threshold Assertions:")
        
        # 1. Thread Leak (allow small drift of ≤2 for Python's delayed GC)
        if leak["thread_leak"] > 2:
            print(f"  [FAIL] Thread Leak: {leak['thread_leak']} threads leaked (Max: 2)")
            success = False
        else:
            print(f"  [PASS] Thread Count: {leak['thread_leak']} leaked (Max: 2)")
            
        # 2. File Handle Leak
        if leak["handle_leak"] > 5:
            print(f"  [FAIL] Handle Leak: {leak['handle_leak']} handles leaked (Max: 5)")
            success = False
        else:
            print(f"  [PASS] System Handles: {leak['handle_leak']} leaked (Max: 5)")
            
        # 3. Heap Growth (allow ≤10MB for SQLite metadata overhead)
        if leak["memory_leak_mb"] > 10.0:
            print(f"  [FAIL] Memory Leak: {leak['memory_leak_mb']:.2f} MB expansion (Max: 10.0 MB)")
            success = False
        else:
            print(f"  [PASS] Heap Expansion: {leak['memory_leak_mb']:.2f} MB (Max: 10.0 MB)")

        # 4. SQL Store p99 latency gate
        store_p99 = sql.get("store", {}).get("p99_ms", 0.0)
        if store_p99 > 500.0:
            print(f"  [FAIL] SQL Store p99: {store_p99:.2f}ms (Max: 500ms)")
            success = False
        else:
            print(f"  [PASS] SQL Store p99: {store_p99:.2f}ms (Max: 500ms)")

        # 5. SQL Retrieve p99 latency gate
        retrieve_p99 = sql.get("retrieve", {}).get("p99_ms", 0.0)
        if retrieve_p99 > 500.0:
            print(f"  [FAIL] SQL Retrieve p99: {retrieve_p99:.2f}ms (Max: 500ms)")
            success = False
        else:
            print(f"  [PASS] SQL Retrieve p99: {retrieve_p99:.2f}ms (Max: 500ms)")

        # 6. SQL error zero-tolerance gate
        store_errors = sql.get("store", {}).get("errors", 0)
        retrieve_errors = sql.get("retrieve", {}).get("errors", 0)
        if store_errors > 0 or retrieve_errors > 0:
            print(f"  [FAIL] SQL Errors: store={store_errors}, retrieve={retrieve_errors} (Max: 0 each)")
            success = False
        else:
            print(f"  [PASS] SQL Error Count: store={store_errors}, retrieve={retrieve_errors}")
            
        print("-" * 80)
        return success


def main():
    fd, temp_db = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    
    monitor = LongRunningStabilityMonitor(db_path=temp_db, iterations=50)
    try:
        results = monitor.execute_stability_loop()
        success = monitor.assert_stability_boundaries(results)
        
        # Clean up temp database
        if os.path.exists(temp_db):
            os.remove(temp_db)
            
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"Stability benchmark failed with exception: {e}")
        if os.path.exists(temp_db):
            try:
                os.remove(temp_db)
            except Exception:
                pass
        sys.exit(1)


if __name__ == "__main__":
    main()
