import os
import glob
import random
from django.conf import settings

class MockResponseService:
    """
    Returns a relevant pre-generated response for demo/offline use.
    Sources: keyword-matches corpus .txt files, then synthesises a
    structured markdown answer with per-source summaries.
    """

    CORPUS_DIR = getattr(settings, 'AI_CORPUS_DIR', '')

    @classmethod
    def get_response(cls, query: str) -> dict:
        if not cls.CORPUS_DIR or not os.path.exists(cls.CORPUS_DIR):
            return {
                'answer': 'The knowledge base is currently empty. Please generate corpus files first.',
                'sources': [],
                'mode': 'mock',
                'confidence': 'none',
                'chunks_retrieved': 0
            }

        query_words = set(query.lower().split())
        all_files = glob.glob(os.path.join(cls.CORPUS_DIR, '*.txt'))

        if not all_files:
            return {
                'answer': 'The knowledge base is currently empty. Please generate corpus files first.',
                'sources': [],
                'mode': 'mock',
                'confidence': 'none',
                'chunks_retrieved': 0
            }

        # Score files by keyword overlap with query
        scored = []
        for f in all_files:
            fname = os.path.basename(f).lower().replace('_', ' ').replace('-', ' ')
            overlap = len(query_words & set(fname.split()))
            scored.append((overlap, f))

        scored.sort(reverse=True)

        # Take up to 3 relevant files; fall back to random if no keyword matches
        top_scored = [(s, f) for s, f in scored if s > 0][:3]
        if not top_scored:
            top_scored = [(0, f) for f in random.sample(all_files, min(3, len(all_files)))]

        # Confidence: high if ≥ 2 files matched by keyword, medium if 1, low if none
        matching_count = len([s for s, _ in top_scored if s > 0])
        if matching_count >= 2:
            confidence = 'high'
        elif matching_count == 1:
            confidence = 'medium'
        else:
            confidence = 'low'

        sources = []
        source_summaries = []

        for rank, (overlap, fpath) in enumerate(top_scored, 1):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            rel_path = os.path.relpath(fpath, cls.CORPUS_DIR).replace('\\', '/')
            filename = os.path.basename(fpath)
            word_count = len(content.split())

            # Use first ~400 characters as the snippet preview
            snippet = content[:400].strip()
            if len(content) > 400:
                snippet += '...'

            # Build a short summary for the answer body (first 200 words)
            summary_words = content.split()[:200]
            summary = ' '.join(summary_words)
            if word_count > 200:
                summary += '...'

            sources.append({
                'filename': filename,
                'relative_path': rel_path,
                'text': content,
                'snippet': snippet,
                'score': float(overlap),
                'reranker_score': float(overlap) / max(1, len(top_scored)),
                'hybrid_rank': rank,
                'final_rank': rank,
                'metadata': {
                    'framework': cls._infer_framework(rel_path),
                    'category': cls._infer_category(filename),
                    'relative_path': rel_path,
                    'word_count': word_count,
                    'char_count': len(content),
                }
            })
            source_summaries.append((filename, summary))

        # Build structured markdown answer
        answer = cls._build_answer(query, source_summaries)

        return {
            'answer': answer,
            'sources': sources,
            'mode': 'mock',
            'confidence': confidence,
            'chunks_retrieved': len(sources)
        }

    @classmethod
    def _build_answer(cls, query: str, summaries: list) -> str:
        """Construct a structured mock answer from the retrieved source summaries."""
        if not summaries:
            return "No relevant documents were found in the knowledge base for this query."

        parts = [f"**Based on the retrieved compliance documents, here is a summary relevant to your query:**\n"]

        for i, (filename, summary) in enumerate(summaries, 1):
            # Derive a display name from the filename
            display = filename.replace('.txt', '').replace('_', ' ').replace('-', ' ').title()
            parts.append(f"**Source {i} — {display}** (`{filename}`):")
            parts.append(summary)
            parts.append("")

        parts.append("---")
        parts.append(
            "**Synthesis:** Based on the above compliance documents, ensure your configuration "
            "aligns with the requirements outlined in the sources. Review each referenced document "
            "for specific control objectives, implementation guidance, and validation steps relevant "
            f"to your query about: *{query[:120]}*."
        )
        parts.append("")
        parts.append(
            "_Note: This is a mock response generated from indexed compliance corpus documents. "
            "Enable AI Mode for a live, LLM-generated answer with full RAG retrieval._"
        )

        return '\n'.join(parts)

    @staticmethod
    def _infer_framework(rel_path: str) -> str:
        """Infer a framework label from the file path."""
        path_lower = rel_path.lower()
        if 'cis' in path_lower:
            return 'CIS'
        if 'nist' in path_lower:
            return 'NIST'
        if 'iso' in path_lower:
            return 'ISO 27001'
        if 'azure' in path_lower:
            return 'Azure Security'
        if 'pci' in path_lower:
            return 'PCI-DSS'
        return 'Compliance'

    @staticmethod
    def _infer_category(filename: str) -> str:
        """Infer a category from the filename."""
        name = filename.lower()
        if 'identity' in name or 'iam' in name or 'access' in name:
            return 'Identity & Access Management'
        if 'password' in name or 'credential' in name:
            return 'Authentication'
        if 'network' in name or 'firewall' in name:
            return 'Network Security'
        if 'encrypt' in name or 'crypto' in name:
            return 'Encryption'
        if 'log' in name or 'audit' in name or 'monitor' in name:
            return 'Logging & Monitoring'
        if 'patch' in name or 'update' in name or 'vulner' in name:
            return 'Vulnerability Management'
        return 'Security Control'
