"""
Tests for the retrieval service (ai_ops/retrieval.py).
Uses MockRetriever since FAISS index may not be available in CI.
"""

from django.test import TestCase
from ai_ops.retrieval import MockRetriever, RetrievalResult


class MockRetrieverTests(TestCase):
    """Tests for the MockRetriever (always available, no FAISS dependency)."""

    def setUp(self):
        self.retriever = MockRetriever()

    def test_is_ready(self):
        self.assertTrue(self.retriever.is_ready())

    def test_load_succeeds(self):
        self.assertTrue(self.retriever.load())

    def test_search_returns_results(self):
        search_result = self.retriever.search("How do I enable MFA?")
        self.assertGreater(len(search_result.results), 0)
        self.assertIsInstance(search_result.results[0], RetrievalResult)

    def test_search_result_has_text(self):
        search_result = self.retriever.search("MFA")
        for r in search_result.results:
            self.assertTrue(len(r.text) > 0)
            self.assertTrue(len(r.filename) > 0)
            self.assertIsInstance(r.score, float)

    def test_search_empty_query(self):
        search_result = self.retriever.search("")
        self.assertEqual(search_result.results, [])

    def test_search_respects_top_k(self):
        search_result = self.retriever.search("compliance", top_k=1)
        self.assertLessEqual(len(search_result.results), 1)

    def test_document_count(self):
        self.assertGreater(self.retriever.document_count(), 0)


class RetrievalResultTests(TestCase):
    """Tests for the RetrievalResult dataclass."""

    def test_creation(self):
        result = RetrievalResult(
            filename="test.txt",
            relative_path="docs/test.txt",
            text="This is a test document.",
            score=0.5,
            word_count=5,
        )
        self.assertEqual(result.filename, "test.txt")
        self.assertEqual(result.score, 0.5)
        self.assertEqual(result.word_count, 5)
