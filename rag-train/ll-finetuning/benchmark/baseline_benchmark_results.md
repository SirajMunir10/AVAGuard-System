# AVAGuard Baseline Retrieval Benchmark Results (OLD Index - MiniLM, No Chunking)

**Date:** 2026-05-31 15:13
**Model:** sentence-transformers/all-MiniLM-L6-v2
**Documents:** 771 | **Chunks:** 771
**Queries:** 50

| Configuration | Top-1 | Top-3 | Top-5 | MRR | Avg Latency |
|---|---|---|---|---|---|
| FAISS Only | 62.0% | 70.0% | 72.0% | 0.681 | 17.7ms |
| Hybrid (BM25+FAISS+RRF) | 52.0% | 68.0% | 72.0% | 0.609 | 28.0ms |
| Full Pipeline (Hybrid+Reranker) | 50.0% | 66.0% | 68.0% | 0.577 | 5707.1ms |

## Analysis of Baseline Results:
1. **RRF & Reranker Performance Drop**: RRF and Reranker actually performed slightly worse than pure FAISS on the old index because each document is indexed as a single entire file (no chunking). 
2. **Context Truncation**: When running the Cross-Encoder model, because documents are up to 1400+ words, they exceed the Cross-Encoder model's max token limit of 512 tokens. This results in heavy truncation, causing the reranker to fail if the query's answer is located in the second half of the file.
3. **High Latency**: The average latency of the full pipeline was 5.7 seconds, which is highly unoptimized when reading huge, whole files.
4. **Conclusion**: Chunking is critical to unlocking the high-precision capability of hybrid search and Cross-Encoder reranking.
