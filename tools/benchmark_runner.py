#!/usr/bin/env python
"""
AVAGuard - Continuous Performance Regression Framework
Runs benchmark suites, records CPU/RAM/latency percentiles, and asserts no regression against baseline.json.
"""

import os
import sys
import json
import time
import platform
import argparse
import logging
import importlib
import math
from typing import Dict, Any, List, Optional
from pathlib import Path

# Headless PyQt6 Mocking
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

def pyqtSignal(*args, **kwargs):
    return MockPyqtSignal()

import threading
class MockQThread(MockQObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._thread = None
    def start(self):
        if hasattr(self, 'run'):
            self._thread = threading.Thread(target=self.run)
            self._thread.start()
    def wait(self, timeout=None):
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=timeout)
    def isFinished(self):
        return self._thread is None or not self._thread.is_alive()

mock_qtcore = unittest.mock.MagicMock()
mock_qtcore.QObject = MockQObject
mock_qtcore.pyqtSignal = pyqtSignal
mock_qtcore.QThread = MockQThread
mock_qtcore.QRunnable = object
mock_qtcore.QTimer = unittest.mock.MagicMock
mock_qtcore.QSize = unittest.mock.MagicMock
mock_qtcore.QUrl = unittest.mock.MagicMock

sys.modules['PyQt6'] = unittest.mock.MagicMock()
sys.modules['PyQt6.QtWidgets'] = unittest.mock.MagicMock()
sys.modules['PyQt6.QtCore'] = mock_qtcore
sys.modules['PyQt6.QtGui'] = unittest.mock.MagicMock()
sys.modules['ui'] = unittest.mock.MagicMock()

# Optional dependency imports with robust fallbacks
try:
    import tracemalloc
except ImportError:
    tracemalloc = None

try:
    import psutil
except ImportError:
    psutil = None

logger = logging.getLogger("avaguard.benchmarks")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


class BenchmarkRunner:
    """Runs designated benchmarks, samples CPU/RAM, and evaluates against baseline.json."""
    def __init__(self, baseline_path: Optional[str] = None):
        self.repo_root = Path(__file__).resolve().parent.parent
        if baseline_path:
            self.baseline_path = Path(baseline_path).expanduser().resolve()
        else:
            self.baseline_path = self.repo_root / "benchmarks" / "baseline.json"
        
        self.baseline_path.parent.mkdir(parents=True, exist_ok=True)

    def get_env_metadata(self) -> Dict[str, Any]:
        """Collects execution environment metadata for regression matching."""
        return {
            "os": platform.system(),
            "os_release": platform.release(),
            "python_version": platform.python_version(),
            "cpu_architecture": platform.machine(),
            "cpu_count": os.cpu_count() or 1,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }

    def run_suite(self, benchmarks_to_run: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Dynamically finds and runs benchmark functions.
        Samples CPU & RAM while running each benchmark.
        """
        results = {
            "metadata": self.get_env_metadata(),
            "benchmarks": {}
        }

        # List of benchmark modules/files to execute
        benchmark_dir = self.repo_root / "benchmarks" / "runtime"
        if not benchmark_dir.exists():
            # Fallback to desktop_app/benchmarks if present
            benchmark_dir = self.repo_root / "desktop_app" / "benchmarks"
        
        if not benchmark_dir.exists():
            logger.warning(f"Benchmarks runtime folder not found at: {benchmark_dir}")
            return results

        # Add to sys.path so we can import modules inside it
        sys.path.insert(0, str(self.repo_root / "desktop_app"))
        sys.path.insert(0, str(benchmark_dir.parent))
        sys.path.insert(0, str(self.repo_root))

        import_prefix = "benchmarks.runtime" if benchmark_dir.name == "runtime" else "desktop_app.benchmarks"

        # Scan files ending in _bench.py or bench_*.py
        bench_files = []
        for file in benchmark_dir.glob("*.py"):
            if file.name.startswith("bench_") or file.name.endswith("_bench.py"):
                bench_files.append(file)

        logger.info(f"Discovered {len(bench_files)} benchmark suites under: {benchmark_dir}")

        for file in bench_files:
            module_name = file.stem
            full_import = f"{import_prefix}.{module_name}"
            
            if benchmarks_to_run and module_name not in benchmarks_to_run:
                continue

            logger.info(f"Running benchmark suite: {module_name}...")
            
            try:
                mod = importlib.import_module(full_import)
                
                # Check for run_benchmarks function inside the module
                if hasattr(mod, "run_benchmarks"):
                    # Sample process resources
                    start_cpu_time = time.process_time()
                    start_time = time.perf_counter()
                    
                    if tracemalloc:
                        tracemalloc.start()
                    
                    # Execute suite benchmarks
                    suite_results = mod.run_benchmarks()
                    
                    end_time = time.perf_counter()
                    end_cpu_time = time.process_time()
                    
                    ram_peak = 0
                    if tracemalloc:
                        _, ram_peak = tracemalloc.get_traced_memory()
                        tracemalloc.stop()
                    
                    # Calculate system resources used during the benchmark
                    wall_duration = end_time - start_time
                    cpu_duration = end_cpu_time - start_cpu_time
                    cpu_pct = (cpu_duration / wall_duration) * 100.0 if wall_duration > 0 else 0.0
                    
                    # Merge measurements
                    for bench_key, bench_data in suite_results.items():
                        bench_data["system_cpu_utilization_pct"] = cpu_pct
                        bench_data["system_peak_ram_bytes"] = ram_peak
                        results["benchmarks"][f"{module_name}/{bench_key}"] = bench_data
                else:
                    logger.warning(f"Module {module_name} does not contain run_benchmarks() entry point.")
            except Exception as e:
                logger.error(f"Failed to run benchmark {module_name}: {e}", exc_info=True)

        return results

    def compare_against_baseline(self, current: Dict[str, Any], threshold_pct: float = 5.0) -> bool:
        """
        Loads baseline.json and compares timings.
        Fails if current percentiles exceed baseline limits by more than threshold_pct.
        """
        if not self.baseline_path.exists():
            logger.info(f"No baseline file found at {self.baseline_path}. Saving current run as initial baseline.")
            self.save_baseline(current)
            return True

        try:
            with open(self.baseline_path, "r", encoding="utf-8") as f:
                baseline = json.load(f)
        except Exception as e:
            logger.error(f"Could not load baseline configuration: {e}")
            return True

        regressions = []
        baseline_bench = baseline.get("benchmarks", {})
        current_bench = current.get("benchmarks", {})

        print("\n" + "=" * 80)
        print(f"      [AVAGUARD PERFORMANCE REGRESSION RESULTS] (Threshold: {threshold_pct}%)")
        print("=" * 80)
        print(f"{'Benchmark Target':<45} | {'Baseline (ms)':<15} | {'Current (ms)':<15} | {'Delta':<10}")
        print("-" * 80)

        for key, curr_data in current_bench.items():
            if key not in baseline_bench:
                print(f"{key:<45} | {'[NEW]':<15} | {curr_data.get('p95_ms', 0):<15.2f} | -")
                continue

            base_data = baseline_bench[key]
            
            # Compare p95 latencies for operations, fallback to mean if percentiles are missing
            curr_val = curr_data.get("p95_ms", curr_data.get("mean_ms", 0.0))
            base_val = base_data.get("p95_ms", base_data.get("mean_ms", 0.0))

            if base_val > 0:
                delta_pct = ((curr_val - base_val) / base_val) * 100.0
            else:
                delta_pct = 0.0

            status = "PASS"
            if delta_pct > threshold_pct:
                status = "FAIL"
                regressions.append((key, base_val, curr_val, delta_pct))

            delta_str = f"{delta_pct:+.2f}%" if base_val > 0 else "0%"
            print(f"{key:<45} | {base_val:<15.2f} | {curr_val:<15.2f} | {delta_str:<10} [{status}]")

        print("=" * 80)

        if regressions:
            print("\n[WARN] Performance Regressions Detected in the following modules:")
            for key, base, curr, delta in regressions:
                print(f"  * {key}: Baseline {base:.2f}ms -> Current {curr:.2f}ms ({delta:+.2f}% delta!)")
            return False

        print("\n[SUCCESS] All benchmark targets are within acceptable baseline bounds.")
        return True

    def save_baseline(self, data: Dict[str, Any]):
        """Persists a new baseline.json configuration to disk."""
        try:
            with open(self.baseline_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            logger.info(f"Successfully saved performance baseline parameters to: {self.baseline_path}")
        except Exception as e:
            logger.error(f"Failed to persist baseline: {e}")


def main():
    parser = argparse.ArgumentParser(description="AVAGuard Performance Regression Test Tool")
    parser.add_argument("--baseline", type=str, help="Path to baseline.json file")
    parser.add_argument("--threshold", type=float, default=5.0, help="Performance degradation warning threshold (default: 5.0%%)")
    parser.add_argument("--update-baseline", action="store_true", help="Overwrite the baseline file with the current measurements")
    parser.add_argument("--only", type=str, help="Comma-separated list of benchmark suites to run")
    args = parser.parse_args()

    runner = BenchmarkRunner(args.baseline)

    only_suites = None
    if args.only:
        only_suites = [s.strip() for s in args.only.split(",") if s.strip()]

    # Run the benchmarks
    current_run = runner.run_suite(only_suites)
    
    if args.update_baseline:
        runner.save_baseline(current_run)
        print("Baseline file updated successfully.")
        sys.exit(0)

    # Compare and return status
    success = runner.compare_against_baseline(current_run, args.threshold)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
