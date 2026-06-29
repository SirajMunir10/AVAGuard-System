"""
Tests for the LLM service (ai_ops/llm_service.py).
"""

from django.test import TestCase
from ai_ops.llm_service import MockLLMService, GenerationResult, GROUNDING_PROMPT


class MockLLMServiceTests(TestCase):
    """Tests for the MockLLMService."""

    def setUp(self):
        self.service = MockLLMService()

    def test_generate_with_context(self):
        result = self.service.generate(
            query="What is MFA?",
            context_chunks=["MFA is multi-factor authentication used to verify user identity."],
        )
        self.assertIsInstance(result, GenerationResult)
        self.assertTrue(result.success)
        self.assertGreater(len(result.text), 0)
        self.assertEqual(result.model, 'mock')
        self.assertGreater(result.token_count, 0)

    def test_generate_without_context(self):
        result = self.service.generate(
            query="What is MFA?",
            context_chunks=[],
        )
        self.assertTrue(result.success)
        self.assertIn("don't have enough information", result.text)

    def test_generate_returns_latency(self):
        result = self.service.generate(
            query="test",
            context_chunks=["some context"],
        )
        self.assertGreater(result.latency_ms, 0)


class GroundingPromptTests(TestCase):
    """Tests that the grounding prompt template is correctly structured."""

    def test_prompt_has_context_placeholder(self):
        self.assertIn("{context}", GROUNDING_PROMPT)

    def test_prompt_has_query_placeholder(self):
        self.assertIn("{query}", GROUNDING_PROMPT)

    def test_prompt_enforces_context_only(self):
        self.assertIn("ONLY the provided context", GROUNDING_PROMPT)

    def test_prompt_instructs_no_external_knowledge(self):
        self.assertIn("Do not use any external knowledge", GROUNDING_PROMPT)

    def test_prompt_handles_insufficient_context(self):
        self.assertIn("don't have enough information", GROUNDING_PROMPT)
