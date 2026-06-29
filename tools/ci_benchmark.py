#!/usr/bin/env python
"""
AVAGuard CI Retrieval Benchmark Automation
Re-builds the FAISS index conditionally (only if corpus changes are detected)
and runs retrieval benchmarks to prevent performance regression.
Fails (exits non-zero) if the Full Pipeline Top-5 accuracy drops below the 55.0% threshold.
"""

import os
import sys
import subprocess
import re
import pickle
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PYTHON_EXE = REPO_ROOT / ".venv" / "Scripts" / "python.exe"
if not PYTHON_EXE.exists():
    PYTHON_EXE = Path(sys.executable)  # Fallback to current python interpreter

BUILD_INDEX_PY = REPO_ROOT / "rag-train" / "ll-finetuning" / "rag" / "build_index.py"
RUN_BENCHMARK_PY = REPO_ROOT / "rag-train" / "ll-finetuning" / "benchmark" / "run_benchmark.py"
RESULTS_MD = REPO_ROOT / "rag-train" / "ll-finetuning" / "benchmark" / "benchmark_results.md"
INDEX_DIR = REPO_ROOT / "rag-train" / "ll-finetuning" / "rag" / "faiss_index"
CORPUS_DIR = REPO_ROOT / "rag-train" / "ll-finetuning" / "rag" / "corpus"

BASELINE_TOP5 = 60.0
ALLOWED_DROP = 5.0
THRESHOLD_TOP5 = BASELINE_TOP5 - ALLOWED_DROP

def run_command(args, cwd):
    print(f"Running command: {' '.join(str(a) for a in args)}")
    result = subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command. Exit code: {result.returncode}")
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)
        sys.exit(result.returncode)
    print(result.stdout)
    return result.stdout

def check_rebuild_needed():
    meta_path = INDEX_DIR / "meta.pkl"
    index_path = INDEX_DIR / "faiss.index"
    
    if not meta_path.exists() or not index_path.exists():
        print("Index or metadata not found. Rebuild required.")
        return True
        
    try:
        with open(meta_path, "rb") as f:
            meta = pickle.load(f)
        built_at_str = meta.get('built_at')
        if not built_at_str:
            print("Built timestamp not found in metadata. Rebuild required.")
            return True
        # Parse ISO timestamp
        built_at = datetime.fromisoformat(built_at_str)
    except Exception as e:
        print(f"Error reading metadata: {e}. Rebuild required.")
        return True

    # Find the latest modification time of any file in corpus
    extensions = {".txt", ".md"}
    latest_mod_time = 0
    latest_file = None
    
    for root, _, files in os.walk(CORPUS_DIR):
        for file in files:
            filepath = Path(root) / file
            if filepath.suffix.lower() in extensions:
                mtime = filepath.stat().st_mtime
                if mtime > latest_mod_time:
                    latest_mod_time = mtime
                    latest_file = filepath
                    
    if latest_mod_time == 0:
        print("No corpus files found. Rebuild required.")
        return True
        
    latest_mod_dt = datetime.fromtimestamp(latest_mod_time, tz=timezone.utc)
    print(f"Latest corpus modification: {latest_file.name} at {latest_mod_dt}")
    print(f"Index built at: {built_at}")
    
    if latest_mod_dt > built_at:
        print("Corpus modifications detected. Rebuild required.")
        return True
        
    print("Index is up-to-date. Skipping rebuild.")
    return False

def main():
    print("=" * 80)
    print("AVAGUARD CI RETRIEVAL BENCHMARK AUTOMATION")
    print("=" * 80)

    # 1. Rebuild FAISS index conditionally
    print("\n--- STEP 1: Checking RAG Index Status ---")
    if check_rebuild_needed():
        print("Index rebuild started...")
        run_command([str(PYTHON_EXE), str(BUILD_INDEX_PY), "--force-rebuild"], REPO_ROOT / "rag-train" / "ll-finetuning" / "rag")
    else:
        print("Skipping index rebuild.")

    # 2. Run benchmark suite
    print("\n--- STEP 2: Running Retrieval Benchmarks ---")
    run_command([str(PYTHON_EXE), str(RUN_BENCHMARK_PY)], REPO_ROOT / "rag-train" / "ll-finetuning" / "benchmark")

    # 3. Parse benchmark results
    print("\n--- STEP 3: Evaluating Performance Against Baseline ---")
    if not RESULTS_MD.exists():
        print(f"Error: Benchmark results file not found at: {RESULTS_MD}")
        sys.exit(1)

    with open(RESULTS_MD, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for the Full Pipeline (Hybrid+Reranker) row
    # Example: | Full Pipeline (Hybrid+Reranker) | 38.0% | 60.0% | 60.0% | 0.483 | 3862.0ms |
    pattern = r"\|\s*Full Pipeline \(Hybrid\+Reranker\)\s*\|\s*([\d\.]+)%\s*\|\s*([\d\.]+)%\s*\|\s*([\d\.]+)%\s*\|"
    match = re.search(pattern, content)

    if not match:
        print("Error: Could not parse Full Pipeline results from benchmark_results.md")
        sys.exit(1)

    top1 = float(match.group(1))
    top3 = float(match.group(2))
    top5 = float(match.group(3))

    print(f"Full Pipeline Retrieval Results:")
    print(f"  Top-1 Accuracy: {top1}%")
    print(f"  Top-3 Accuracy: {top3}%")
    print(f"  Top-5 Accuracy: {top5}%")
    print(f"  Baseline Top-5: {BASELINE_TOP5}%")
    print(f"  Fail Threshold: {THRESHOLD_TOP5}%")

    if top5 < THRESHOLD_TOP5:
        print(f"\n[FAIL] Performance regression detected! Top-5 accuracy ({top5}%) dropped below threshold ({THRESHOLD_TOP5}%).")
        sys.exit(1)

    print(f"\n[PASS] Retrieval quality is within acceptable bounds ({top5}% >= {THRESHOLD_TOP5}%).")
    sys.exit(0)

if __name__ == "__main__":
    main()
