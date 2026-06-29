"""
AVAGuard RAG — Retrieval Quality Benchmark

Evaluates retrieval quality across three configurations:
1. FAISS-only (dense search, no BM25, no reranking)
2. Hybrid (BM25 + FAISS + RRF, no reranking)
3. Full pipeline (Hybrid + Cross-Encoder reranking)

Reports: Top-1/3/5 accuracy, MRR, avg score, avg latency.

Usage:
    python run_benchmark.py
    python run_benchmark.py --index-dir ../rag/faiss_index --queries benchmark_queries.csv
"""

import os
import sys
import csv
import time
import pickle
import argparse
from pathlib import Path
from collections import defaultdict

import numpy as np

SCRIPT_DIR = Path(__file__).parent
DEFAULT_INDEX_DIR = SCRIPT_DIR.parent / "rag" / "faiss_index"
DEFAULT_QUERIES = SCRIPT_DIR / "benchmark_queries.csv"


def load_index(index_dir):
    """Load FAISS index and metadata."""
    import faiss
    from sentence_transformers import SentenceTransformer
    from rank_bm25 import BM25Okapi

    meta_path = index_dir / "meta.pkl"
    index_path = index_dir / "faiss.index"

    with open(meta_path, "rb") as f:
        metadata = pickle.load(f)

    index = faiss.read_index(str(index_path))
    model_name = metadata.get("model_name", "sentence-transformers/all-MiniLM-L6-v2")
    model = SentenceTransformer(model_name)

    # Load BM25 Index if serialized on disk, otherwise build from texts
    bm25_path = index_dir / "bm25.pkl"
    if bm25_path.exists():
        try:
            with open(bm25_path, "rb") as f:
                bm25 = pickle.load(f)
            print("  BM25 index loaded from disk")
        except Exception as e:
            print(f"  Failed to load BM25 from disk: {e}. Rebuilding...")
            texts = metadata.get("texts", [])
            tokenized = [t.lower().split() for t in texts]
            bm25 = BM25Okapi(tokenized)
    else:
        texts = metadata.get("texts", [])
        tokenized = [t.lower().split() for t in texts]
        bm25 = BM25Okapi(tokenized)

    is_bge = 'bge' in model_name.lower()

    return index, metadata, model, bm25, is_bge


def faiss_search(query, index, metadata, model, is_bge, k=20):
    """Pure FAISS dense search."""
    if is_bge:
        q = "Represent this sentence for searching relevant passages: " + query
    else:
        q = query
    emb = model.encode([q])
    distances, indices = index.search(emb, k)
    docs = metadata.get("documents", [])
    results = []
    for j, i in enumerate(indices[0]):
        if 0 <= i < len(docs):
            results.append({
                'filename': docs[i].get('filename', ''),
                'score': float(distances[0][j]),
                'rank': j + 1,
                'idx': int(i),
            })
    return results


def bm25_search(query, bm25, metadata, k=20):
    """BM25 keyword search."""
    tokens = query.lower().split()
    scores = bm25.get_scores(tokens)
    top = np.argsort(scores)[-k:][::-1]
    docs = metadata.get("documents", [])
    results = []
    for rank, i in enumerate(top):
        if scores[i] > 0 and i < len(docs):
            results.append({
                'filename': docs[i].get('filename', ''),
                'score': float(scores[i]),
                'rank': rank + 1,
                'idx': int(i),
            })
    return results


def hybrid_search(query, index, metadata, model, bm25, is_bge, k=20, rrf_k=60):
    """BM25 + FAISS + RRF (chunk-level RRF merged to filename-level)."""
    faiss_res = faiss_search(query, index, metadata, model, is_bge, k)
    bm25_res = bm25_search(query, bm25, metadata, k)

    # We do Reciprocal Rank Fusion on the chunk indices (idx)
    scores = {}
    doc_map = {}

    for rank, r in enumerate(bm25_res):
        idx = r['idx']
        scores[idx] = scores.get(idx, 0) + 1 / (rrf_k + rank + 1)
        doc_map[idx] = r

    for rank, r in enumerate(faiss_res):
        idx = r['idx']
        scores[idx] = scores.get(idx, 0) + 1 / (rrf_k + rank + 1)
        if idx not in doc_map:
            doc_map[idx] = r

    # Sort chunks by RRF score descending
    sorted_chunks = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # To group by filename (returning only the top chunk per filename, up to k filenames)
    filename_to_best_chunk = {}
    for idx, rrf_score in sorted_chunks:
        r = doc_map[idx]
        fname = r['filename']
        if fname not in filename_to_best_chunk:
            filename_to_best_chunk[fname] = {
                'filename': fname,
                'score': rrf_score,
                'idx': idx
            }

    # Extract sorted results up to k
    results = []
    seen = set()
    for idx, rrf_score in sorted_chunks:
        r = doc_map[idx]
        fname = r['filename']
        if fname not in seen:
            seen.add(fname)
            best = filename_to_best_chunk[fname]
            results.append({
                'filename': fname,
                'score': best['score'],
                'idx': best['idx'],
                'rank': len(results) + 1
            })
            if len(results) >= k:
                break

    return results


_CE_MODEL = None

def rerank_results(query, results, metadata, k=5, min_score=-0.5):
    """Cross-encoder reranking of hybrid results at chunk level."""
    global _CE_MODEL
    if _CE_MODEL is None:
        from sentence_transformers import CrossEncoder
        _CE_MODEL = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    ce = _CE_MODEL

    texts = metadata.get("texts", [])

    pairs = []
    valid_results = []
    for r in results:
        idx = r.get('idx')
        if idx is not None and idx < len(texts):
            text = texts[idx]
            pairs.append((query, text))
            valid_results.append(r)

    if not pairs:
        return []

    scores = ce.predict(pairs)

    reranked = sorted(zip(valid_results, scores), key=lambda x: x[1], reverse=True)
    final = []
    for rank, (r, score) in enumerate(reranked):
        if float(score) >= min_score:
            r['reranker_score'] = float(score)
            r['rank'] = rank + 1
            final.append(r)
    return final[:k]



def check_hit(results, expected_doc, k):
    """Check if expected document appears in top-k results."""
    expected_lower = expected_doc.lower()
    for r in results[:k]:
        fname = r['filename'].lower()
        # Fuzzy match: check if expected is a substring of filename or vice versa
        if expected_lower in fname or any(
            word in fname for word in expected_lower.split()
            if len(word) > 3
        ):
            return True, r.get('rank', k + 1)
    return False, 0


def run_benchmark(index_dir, queries_path):
    """Run the full benchmark suite."""
    print("=" * 70)
    print("AVAGuard Retrieval Quality Benchmark")
    print("=" * 70)

    # Load index
    print(f"\nLoading index from {index_dir}...")
    index, metadata, model, bm25, is_bge = load_index(index_dir)
    total_docs = metadata.get('total_documents', 0)
    total_chunks = metadata.get('total_chunks', total_docs)
    model_name = metadata.get('model_name', 'unknown')
    print(f"  Model: {model_name}")
    print(f"  Documents: {total_docs}, Chunks: {total_chunks}")

    # Load queries
    queries = []
    with open(queries_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            queries.append(row)
    print(f"  Benchmark queries: {len(queries)}")

    configs = [
        ('FAISS Only', 'faiss'),
        ('Hybrid (BM25+FAISS+RRF)', 'hybrid'),
        ('Full Pipeline (Hybrid+Reranker)', 'full'),
    ]

    all_results = {}

    for config_name, config_type in configs:
        print(f"\n{'-' * 70}")
        print(f"Running: {config_name}")
        print(f"{'-' * 70}")

        hits_at = {1: 0, 3: 0, 5: 0}
        reciprocal_ranks = []
        latencies = []
        scores = []

        for i, q in enumerate(queries):
            question = q['question']
            expected = q['expected_document']

            start = time.perf_counter()

            if config_type == 'faiss':
                results = faiss_search(question, index, metadata, model, is_bge, k=20)
            elif config_type == 'hybrid':
                results = hybrid_search(question, index, metadata, model, bm25, is_bge, k=20)
            elif config_type == 'full':
                hybrid_res = hybrid_search(question, index, metadata, model, bm25, is_bge, k=20)
                results = rerank_results(question, hybrid_res, metadata, k=5)

            elapsed_ms = (time.perf_counter() - start) * 1000
            latencies.append(elapsed_ms)

            # Check hits
            for k in [1, 3, 5]:
                hit, rank = check_hit(results, expected, k)
                if hit:
                    hits_at[k] += 1

            # MRR
            hit_any, rank = check_hit(results, expected, 20)
            if hit_any and rank > 0:
                reciprocal_ranks.append(1.0 / rank)
            else:
                reciprocal_ranks.append(0.0)

            # Avg score
            if results:
                s = results[0].get('reranker_score', results[0].get('score', 0))
                scores.append(s)

            if (i + 1) % 10 == 0:
                print(f"  Progress: {i + 1}/{len(queries)}")

        n = len(queries)
        mrr = sum(reciprocal_ranks) / n if n > 0 else 0
        avg_latency = sum(latencies) / n if n > 0 else 0
        avg_score = sum(scores) / len(scores) if scores else 0

        all_results[config_name] = {
            'top1': hits_at[1] / n * 100,
            'top3': hits_at[3] / n * 100,
            'top5': hits_at[5] / n * 100,
            'mrr': mrr,
            'avg_latency_ms': avg_latency,
            'avg_score': avg_score,
        }

        print(f"  Top-1 Accuracy: {hits_at[1]}/{n} ({hits_at[1]/n*100:.1f}%)")
        print(f"  Top-3 Accuracy: {hits_at[3]}/{n} ({hits_at[3]/n*100:.1f}%)")
        print(f"  Top-5 Accuracy: {hits_at[5]}/{n} ({hits_at[5]/n*100:.1f}%)")
        print(f"  MRR:            {mrr:.4f}")
        print(f"  Avg Latency:    {avg_latency:.1f} ms")
        print(f"  Avg Top Score:  {avg_score:.4f}")

    # Summary table
    print(f"\n{'=' * 70}")
    print("SUMMARY COMPARISON")
    print(f"{'=' * 70}")
    print(f"{'Configuration':<35} {'Top-1':>6} {'Top-3':>6} {'Top-5':>6} {'MRR':>6} {'Lat(ms)':>8}")
    print(f"{'-' * 70}")
    for name, r in all_results.items():
        print(f"{name:<35} {r['top1']:>5.1f}% {r['top3']:>5.1f}% {r['top5']:>5.1f}% {r['mrr']:>6.3f} {r['avg_latency_ms']:>7.1f}")
    print(f"{'=' * 70}")

    # Save results
    output_path = SCRIPT_DIR / "benchmark_results.md"
    with open(output_path, 'w') as f:
        f.write("# AVAGuard Retrieval Benchmark Results\n\n")
        f.write(f"**Date:** {time.strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Model:** {model_name}\n")
        f.write(f"**Documents:** {total_docs} | **Chunks:** {total_chunks}\n")
        f.write(f"**Queries:** {len(queries)}\n\n")
        f.write("| Configuration | Top-1 | Top-3 | Top-5 | MRR | Avg Latency |\n")
        f.write("|---|---|---|---|---|---|\n")
        for name, r in all_results.items():
            f.write(f"| {name} | {r['top1']:.1f}% | {r['top3']:.1f}% | {r['top5']:.1f}% | {r['mrr']:.3f} | {r['avg_latency_ms']:.1f}ms |\n")

    print(f"\nResults saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="AVAGuard Retrieval Benchmark")
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    args = parser.parse_args()

    run_benchmark(args.index_dir, args.queries)


if __name__ == "__main__":
    main()
