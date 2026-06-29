"""
AVAGuard AI Operations — Compliance Retrieval Service

Hybrid Search (BM25 + FAISS) with Reciprocal Rank Fusion (RRF)
and Cross-Encoder Reranking for production-grade RAG.
"""

import time
import pickle
import logging
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Dict
import numpy as np
from django.conf import settings

logger = logging.getLogger(__name__)


@dataclass
class RetrievalResult:
    """A single retrieved document/chunk from the vector index."""
    filename: str
    relative_path: str
    text: str
    score: float            # RRF or final similarity score
    word_count: int = 0
    metadata: dict = field(default_factory=dict)
    # Reranking fields
    reranker_score: float = 0.0
    hybrid_rank: int = 0
    final_rank: int = 0


@dataclass
class SearchResult:
    """Complete search result with metadata for logging."""
    results: List[RetrievalResult]
    confidence: str             # 'high', 'medium', 'low', 'none'
    retrieval_ms: float = 0.0
    rerank_ms: float = 0.0
    total_candidates: int = 0
    avg_reranker_score: float = 0.0
    top_reranker_score: float = 0.0
    reranker_details: list = field(default_factory=list)  # Per-chunk scoring details


class ComplianceRetriever:
    """
    Loads a FAISS index and BM25 index from disk and performs
    Hybrid Search (Dense + Keyword) with Reciprocal Rank Fusion (RRF)
    and Cross-Encoder Reranking.
    """

    def __init__(self, index_dir: Path, model_name: str = None):
        self._index_dir = Path(index_dir)
        self._model_name = model_name or getattr(
            settings, 'AI_EMBEDDING_MODEL', 'sentence-transformers/all-MiniLM-L6-v2'
        )
        self._index = None
        self._metadata = None
        self._model = None
        self.bm25_index = None
        self._cross_encoder = None
        self._loaded = False

    def load(self) -> bool:
        """Load FAISS, embedding model, and build BM25 index."""
        try:
            import faiss
            from sentence_transformers import SentenceTransformer
            from rank_bm25 import BM25Okapi
        except ImportError as e:
            logger.error(
                f"Missing AI dependencies: {e}. "
                "Install faiss-cpu, sentence-transformers, rank-bm25."
            )
            return False

        index_path = self._index_dir / "faiss.index"
        meta_path = self._index_dir / "meta.pkl"

        if not index_path.exists() or not meta_path.exists():
            logger.warning(
                f"FAISS index not found at {self._index_dir}. Run build_index.py first."
            )
            return False

        try:
            self._index = faiss.read_index(str(index_path))

            with open(meta_path, "rb") as f:
                self._metadata = pickle.load(f)

            # Verify model compatibility
            index_model = self._metadata.get("model_name", "")
            if index_model and index_model != self._model_name:
                logger.warning(
                    f"Model mismatch: index was built with '{index_model}' "
                    f"but configured model is '{self._model_name}'. "
                    f"Loading the index model instead."
                )
                self._model_name = index_model

            self._model = SentenceTransformer(self._model_name)

            # Load BM25 Index if serialized on disk, otherwise build from chunk texts
            bm25_path = self._index_dir / "bm25.pkl"
            if bm25_path.exists():
                try:
                    with open(bm25_path, "rb") as f:
                        self.bm25_index = pickle.load(f)
                    logger.info("BM25 index loaded from disk")
                except Exception as e:
                    logger.warning(f"Failed to load serialized BM25 index: {e}. Rebuilding...")
                    texts = self._metadata.get("texts", [])
                    if texts:
                        tokenized_texts = [text.lower().split() for text in texts]
                        self.bm25_index = BM25Okapi(tokenized_texts)
            else:
                texts = self._metadata.get("texts", [])
                if texts:
                    tokenized_texts = [text.lower().split() for text in texts]
                    self.bm25_index = BM25Okapi(tokenized_texts)

            self._loaded = True

            total_chunks = self._metadata.get("total_chunks",
                           self._metadata.get("total_documents", 0))
            total_docs = self._metadata.get("total_documents", 0)
            logger.info(
                f"ComplianceRetriever loaded: {total_docs} documents, "
                f"{total_chunks} chunks, model={self._model_name}"
            )
            return True

        except Exception as e:
            logger.error(f"Failed to load FAISS index: {e}")
            self._loaded = False
            return False

    def _load_cross_encoder(self):
        """Lazy-load the cross-encoder reranker model."""
        try:
            from sentence_transformers import CrossEncoder
            model_name = getattr(
                settings, 'AI_RERANKER_MODEL',
                'cross-encoder/ms-marco-MiniLM-L-6-v2'
            )
            self._cross_encoder = CrossEncoder(model_name)
            logger.info(f"Cross-encoder loaded: {model_name}")
        except Exception as e:
            logger.error(f"Failed to load cross-encoder: {e}")
            self._cross_encoder = None

    def is_ready(self) -> bool:
        return self._loaded and self._index is not None

    def _bm25_search(self, query: str, k: int):
        """Keyword-based search using BM25Okapi."""
        if not self.bm25_index:
            return []
        tokenized_query = query.lower().split()
        scores = self.bm25_index.get_scores(tokenized_query)

        top_indices = np.argsort(scores)[-k:][::-1]

        documents = self._metadata.get("documents", [])
        texts = self._metadata.get("texts", [])

        results = []
        for i in top_indices:
            if scores[i] <= 0:
                continue
            doc_meta = documents[i] if i < len(documents) else {}
            res = RetrievalResult(
                filename=doc_meta.get("filename", f"doc_{i}"),
                relative_path=doc_meta.get("relative_path", ""),
                text=texts[i] if i < len(texts) else "",
                score=float(scores[i]),
                word_count=doc_meta.get("word_count", 0),
                metadata=doc_meta,
            )
            results.append((res, int(i)))
        return results

    def _faiss_search(self, query: str, k: int):
        """Dense vector search using FAISS with optional BGE prefix."""
        if "bge" in self._model_name.lower():
            faiss_query = (
                "Represent this sentence for searching relevant passages: "
                + query
            )
        else:
            faiss_query = query

        query_embedding = self._model.encode([faiss_query])
        distances, indices = self._index.search(query_embedding, k)

        documents = self._metadata.get("documents", [])
        texts = self._metadata.get("texts", [])

        results = []
        for j, i in enumerate(indices[0]):
            if i < 0 or i >= len(documents):
                continue
            doc_meta = documents[i]
            res = RetrievalResult(
                filename=doc_meta.get("filename", f"doc_{i}"),
                relative_path=doc_meta.get("relative_path", ""),
                text=texts[i] if i < len(texts) else "",
                score=float(distances[0][j]),
                word_count=doc_meta.get("word_count", 0),
                metadata=doc_meta,
            )
            results.append((res, int(i)))
        return results

    def _reciprocal_rank_fusion(self, list1, list2, top_k: int, rrf_k: int):
        """Merge two ranked result lists using Reciprocal Rank Fusion."""
        scores = {}
        doc_map = {}

        for rank, (doc, idx) in enumerate(list1):
            scores[idx] = scores.get(idx, 0) + 1 / (rrf_k + rank + 1)
            doc_map[idx] = doc

        for rank, (doc, idx) in enumerate(list2):
            scores[idx] = scores.get(idx, 0) + 1 / (rrf_k + rank + 1)
            doc_map[idx] = doc

        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        final_results = []
        for idx, rrf_score in sorted_docs[:top_k]:
            doc = doc_map[idx]
            doc.score = rrf_score
            final_results.append(doc)

        return final_results

    def _rerank(self, query: str, candidates: List[RetrievalResult],
                final_k: int) -> Tuple[List[RetrievalResult], float]:
        """
        Cross-encoder reranking with threshold filtering.

        Returns:
            Tuple of (reranked results, rerank latency in ms)
        """
        if not candidates:
            return [], 0.0

        # Lazy-load cross-encoder on first use
        if self._cross_encoder is None:
            self._load_cross_encoder()

        if self._cross_encoder is None:
            # Cross-encoder failed to load — return candidates as-is
            logger.warning("Cross-encoder unavailable, skipping reranking")
            for i, doc in enumerate(candidates[:final_k]):
                doc.final_rank = i + 1
                doc.reranker_score = doc.score
            return candidates[:final_k], 0.0

        rerank_start = time.perf_counter()

        # Assign hybrid ranks before reranking
        for i, doc in enumerate(candidates):
            doc.hybrid_rank = i + 1

        # Score all candidate pairs
        pairs = [(query, doc.text) for doc in candidates]
        scores = self._cross_encoder.predict(pairs)

        # Sort by reranker score descending
        reranked = sorted(
            zip(candidates, scores), key=lambda x: x[1], reverse=True
        )

        # Apply relevance threshold
        min_score = getattr(settings, 'AI_MIN_RELEVANCE_SCORE', -0.5)
        filtered = [
            (doc, float(score))
            for doc, score in reranked
            if float(score) >= min_score
        ]

        # Assign final ranks and reranker scores
        results = []
        for i, (doc, score) in enumerate(filtered[:final_k]):
            doc.reranker_score = score
            doc.final_rank = i + 1
            results.append(doc)

        rerank_ms = (time.perf_counter() - rerank_start) * 1000
        return results, rerank_ms

    def _compute_confidence(self, results: List[RetrievalResult]) -> str:
        """Confidence level based on average reranker score.

        ms-marco-MiniLM-L-6-v2 outputs raw logit scores (unbounded),
        NOT 0-1 probabilities. Observed distribution from 234 samples:
            P25=1.74, Median=3.06, P75=4.46, Max=9.09

        Thresholds calibrated against this distribution:
            high   >= 3.0  (above median — strong relevance)
            medium >= 1.5  (above ~P25 — moderate relevance)
            low    <  1.5  (bottom quartile — weak relevance)
        """
        if not results:
            return 'none'
        avg = sum(r.reranker_score for r in results) / len(results)
        if avg >= 3.0:
            return 'high'
        elif avg >= 1.5:
            return 'medium'
        else:
            return 'low'

    def search(self, query: str, top_k: int = 5,
               framework_filter: str = None) -> SearchResult:
        """
        Full retrieval pipeline:
        1. BM25 keyword search
        2. FAISS dense search
        3. Reciprocal Rank Fusion
        3b. Framework filter (optional)
        4. Cross-encoder reranking
        5. Relevance threshold filtering
        6. Confidence scoring

        Args:
            query: Natural language question.
            top_k: Number of results to return.
            framework_filter: Optional framework name to scope results
                             (e.g., 'CIS', 'NIST', 'AWS Security').

        Returns a SearchResult with results, confidence, and timing data.
        """
        if not self.is_ready() or not query or not query.strip():
            return SearchResult(results=[], confidence='none')

        try:
            k_candidates = getattr(settings, 'AI_RETRIEVAL_K_CANDIDATES', 20)
            k_final = top_k if top_k != 5 else getattr(settings, 'AI_RETRIEVAL_K_FINAL', 5)
            rrf_constant = getattr(settings, 'AI_RRF_CONSTANT', 60)

            retrieval_start = time.perf_counter()

            # 1. BM25 Search
            bm25_results = self._bm25_search(query, k_candidates)

            # 2. FAISS Dense Search
            faiss_results = self._faiss_search(query, k_candidates)

            # 3. Reciprocal Rank Fusion
            merged = self._reciprocal_rank_fusion(
                bm25_results, faiss_results,
                top_k=k_candidates,
                rrf_k=rrf_constant,
            )

            # 3b. Framework filter (optional)
            if framework_filter:
                fw_lower = framework_filter.lower()
                merged = [
                    doc for doc in merged
                    if doc.metadata.get('framework', '').lower() == fw_lower
                ]

            retrieval_ms = (time.perf_counter() - retrieval_start) * 1000

            # 4. Cross-encoder reranking
            reranked, rerank_ms = self._rerank(query, merged, final_k=k_final)

            # 5. Confidence scoring
            confidence = self._compute_confidence(reranked)

            # 6. Build per-chunk scoring details for logging
            reranker_details = []
            for doc in reranked:
                reranker_details.append({
                    'filename': doc.filename,
                    'hybrid_rank': doc.hybrid_rank,
                    'reranker_score': round(doc.reranker_score, 4),
                    'final_rank': doc.final_rank,
                })

            avg_score = (
                sum(r.reranker_score for r in reranked) / len(reranked)
                if reranked else 0.0
            )
            top_score = (
                max(r.reranker_score for r in reranked)
                if reranked else 0.0
            )

            return SearchResult(
                results=reranked,
                confidence=confidence,
                retrieval_ms=retrieval_ms,
                rerank_ms=rerank_ms,
                total_candidates=len(merged),
                avg_reranker_score=round(avg_score, 4),
                top_reranker_score=round(top_score, 4),
                reranker_details=reranker_details,
            )

        except Exception as e:
            logger.error(f"Hybrid search failed: {e}", exc_info=True)
            return SearchResult(results=[], confidence='none')

    def document_count(self) -> int:
        if self._metadata:
            return self._metadata.get("total_documents", 0)
        return 0

    def chunk_count(self) -> int:
        if self._metadata:
            return self._metadata.get("total_chunks",
                   self._metadata.get("total_documents", 0))
        return 0

    def available_frameworks(self) -> list:
        """Return sorted list of framework names present in the index."""
        if self._metadata:
            fw = self._metadata.get('files_by_framework', {})
            return sorted(fw.keys())
        return []

    def index_metadata(self) -> dict:
        """Return index metadata for status pages."""
        if self._metadata:
            return {
                'total_documents': self._metadata.get('total_documents', 0),
                'total_chunks': self._metadata.get('total_chunks', 0),
                'model_name': self._metadata.get('model_name', ''),
                'dimension': self._metadata.get('dimension', 0),
                'chunk_size': self._metadata.get('chunk_size', 0),
                'chunk_overlap': self._metadata.get('chunk_overlap', 0),
                'built_at': self._metadata.get('built_at', ''),
                'files_by_framework': self._metadata.get('files_by_framework', {}),
            }
        return {}


class MockRetriever:
    """
    Returns canned results for testing without a real FAISS index.
    """

    def __init__(self):
        self._loaded = True

    def load(self) -> bool:
        return True

    def is_ready(self) -> bool:
        return True

    def search(self, query: str, top_k: int = 5) -> SearchResult:
        if not query:
            return SearchResult(results=[], confidence='none')

        results = [
            RetrievalResult(
                filename="cis_azure_1.1_mfa.txt",
                relative_path="azure/cis_azure_1.1_mfa.txt",
                text=(
                    "CIS Azure Benchmark 1.1 — Ensure Multi-Factor Authentication is enabled "
                    "for all privileged users. MFA adds an additional layer of protection on top "
                    "of a username and password."
                ),
                score=0.42,
                word_count=50,
                reranker_score=0.72,
                final_rank=1,
            ),
            RetrievalResult(
                filename="cis_azure_1.2_conditional_access.txt",
                relative_path="azure/cis_azure_1.2_conditional_access.txt",
                text=(
                    "CIS Azure Benchmark 1.2 — Ensure Conditional Access policies are "
                    "configured to require MFA."
                ),
                score=0.58,
                word_count=35,
                reranker_score=0.65,
                final_rank=2,
            ),
        ][:top_k]

        return SearchResult(
            results=results,
            confidence='high',
            retrieval_ms=5.0,
            rerank_ms=0.0,
            total_candidates=2,
            avg_reranker_score=0.685,
            top_reranker_score=0.72,
        )

    def document_count(self) -> int:
        return 2

    def chunk_count(self) -> int:
        return 2

    def index_metadata(self) -> dict:
        return {
            'total_documents': 2,
            'total_chunks': 2,
            'model_name': 'mock',
            'dimension': 384,
        }
