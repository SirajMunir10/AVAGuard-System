# AVAGuard Retrieval Benchmark Results

**Date:** 2026-06-02 21:21
**Model:** BAAI/bge-base-en-v1.5
**Documents:** 770 | **Chunks:** 1588
**Queries:** 61

| Configuration | Top-1 | Top-3 | Top-5 | MRR | Avg Latency |
|---|---|---|---|---|---|
| FAISS Only | 54.1% | 67.2% | 75.4% | 0.631 | 51.1ms |
| Hybrid (BM25+FAISS+RRF) | 52.5% | 62.3% | 67.2% | 0.610 | 54.2ms |
| Full Pipeline (Hybrid+Reranker) | 49.2% | 70.5% | 77.0% | 0.599 | 2621.9ms |
