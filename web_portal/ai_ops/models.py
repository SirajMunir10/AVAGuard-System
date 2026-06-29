"""
AVAGuard AI Operations — Database Models

Tracks AI query audit logs, ingested knowledge documents, and per-org AI settings.
All query logs are immutable for compliance audit purposes.
"""

import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


class AIQueryLog(models.Model):
    """
    Immutable audit record of every AI query and response.

    Every question a user asks, every set of documents retrieved, and every
    LLM-generated answer is recorded here. Entries cannot be updated or deleted
    to maintain a tamper-resistant audit trail.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='ai_queries'
    )
    organization = models.ForeignKey(
        'core.Organization',
        on_delete=models.CASCADE,
        null=True
    )
    query_text = models.TextField(help_text="User's original question")
    sanitized_query = models.TextField(
        blank=True,
        help_text="Query after prompt safety processing"
    )
    retrieved_sources = models.JSONField(
        default=list,
        help_text="List of {filename, score, snippet} from vector search"
    )
    response_text = models.TextField(
        blank=True,
        help_text="LLM-generated answer"
    )
    grounding_score = models.FloatField(
        null=True, blank=True,
        help_text="How well the answer maps to retrieved sources (0.0-1.0)"
    )
    model_used = models.CharField(
        max_length=100, default='mock',
        help_text="LLM model identifier (e.g. gpt-4o-mini, mock)"
    )
    latency_ms = models.FloatField(
        default=0.0,
        help_text="Total request-to-response time in milliseconds"
    )
    retrieval_ms = models.FloatField(
        default=0.0,
        help_text="Vector search time only in milliseconds"
    )
    token_count = models.IntegerField(
        null=True, blank=True,
        help_text="Response token count"
    )
    flagged = models.BooleanField(
        default=False,
        help_text="True if query was flagged by safety checks"
    )
    flag_reason = models.CharField(
        max_length=200, blank=True,
        help_text="Reason for safety flag, if any"
    )
    provider_used = models.CharField(
        max_length=50, blank=True, default='',
        help_text="LLM provider that handled this request (deepseek, openai, mock)"
    )
    is_fallback = models.BooleanField(
        default=False,
        help_text="True if response came from mock/fallback mode instead of real LLM"
    )
    source_count = models.IntegerField(
        default=0,
        help_text="Number of documents retrieved for this query"
    )
    status = models.CharField(
        max_length=20, default='success',
        help_text="'success' or 'error'"
    )
    mode = models.CharField(
        max_length=10, default='ai',
        help_text="'ai' or 'mock'"
    )
    response_time_ms = models.IntegerField(
        null=True, blank=True,
        help_text="latency in milliseconds"
    )
    chunks_retrieved = models.IntegerField(
        null=True, blank=True,
        help_text="how many FAISS results"
    )
    error_message = models.TextField(
        null=True, blank=True,
        help_text="Full error message if status is error"
    )
    # Phase 1: Retrieval Quality Fields
    retrieval_method = models.CharField(
        max_length=20, default='hybrid',
        help_text="'hybrid', 'bm25', 'faiss_only', 'mock'"
    )
    rerank_latency_ms = models.FloatField(
        null=True, blank=True,
        help_text="Cross-encoder reranking time in milliseconds"
    )
    average_similarity_score = models.FloatField(
        null=True, blank=True,
        help_text="Average reranker score across returned chunks"
    )
    top_similarity_score = models.FloatField(
        null=True, blank=True,
        help_text="Highest reranker score among returned chunks"
    )
    confidence_level = models.CharField(
        max_length=10, default='none',
        choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low'), ('none', 'none')],
        help_text="Confidence level based on reranker scores"
    )
    retrieved_document_count = models.IntegerField(
        default=0,
        help_text="Number of chunks that passed the relevance threshold"
    )
    reranker_scores = models.JSONField(
        default=list, blank=True,
        help_text="Per-chunk reranker details: [{filename, hybrid_rank, reranker_score, final_rank}]"
    )
    # Phase 5A Fields: Context Tracking & Privacy
    context_reference = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="ID or reference of the ScanResult/Finding"
    )
    transformation_metadata = models.JSONField(
        default=list, blank=True,
        help_text="Audit log of topological transformations (e.g., {'10.0.0.1': '[INTERNAL_HOST]'})"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['organization', '-created_at']),
            models.Index(fields=['flagged']),
            models.Index(fields=['status']),
            models.Index(fields=['mode']),
            models.Index(fields=['confidence_level']),
        ]

    def __str__(self):
        preview = self.query_text[:60] + '...' if len(self.query_text) > 60 else self.query_text
        return f"AIQuery by {self.user} — {preview}"

    def save(self, *args, **kwargs):
        """Block updates to existing entries — insert only."""
        if self.pk and AIQueryLog.objects.filter(pk=self.pk).exists():
            raise ValueError("AIQueryLog entries are immutable. Updates are not permitted.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Block deletion of query logs."""
        raise ValueError("AIQueryLog entries cannot be deleted.")


class AIQueryFeedback(models.Model):
    """
    Mutable feedback record attached to an immutable AI query log.
    """
    RATING_CHOICES = [
        ('up', 'up'),
        ('down', 'down'),
    ]

    query_log = models.OneToOneField(
        AIQueryLog, on_delete=models.CASCADE, related_name='feedback'
    )
    rating = models.CharField(max_length=10, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    needs_review = models.BooleanField(default=False, db_index=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"Feedback ({self.rating}) for {self.query_log.id}"



class KnowledgeDocument(models.Model):
    """
    Registry of documents ingested into the knowledge base.

    Tracks which files have been indexed in FAISS for deduplication
    and provenance tracking.
    """
    SOURCE_TYPE_CHOICES = [
        ('cis_benchmark', 'CIS Benchmark'),
        ('scan_result', 'Scan Result'),
        ('remediation', 'Remediation Guide'),
        ('custom', 'Custom Document'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        'core.Organization',
        on_delete=models.CASCADE,
        null=True, blank=True,
        help_text="Null for global/shared documents"
    )
    filename = models.CharField(max_length=500)
    content_hash = models.CharField(
        max_length=64,
        help_text="SHA-256 hash for deduplication"
    )
    word_count = models.IntegerField(default=0)
    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPE_CHOICES,
        default='custom'
    )
    ingested_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-ingested_at']
        indexes = [
            models.Index(fields=['content_hash']),
            models.Index(fields=['source_type']),
        ]

    def __str__(self):
        return f"{self.filename} ({self.source_type})"


class AISettings(models.Model):
    """
    Per-organization AI configuration.

    Controls whether AI features are enabled, which LLM provider to use,
    generation parameters, and rate limits.
    """
    LLM_PROVIDER_CHOICES = [
        ('deepseek', 'DeepSeek'),
        ('openai', 'OpenAI'),
        ('azure_openai', 'Azure OpenAI'),
        ('mock', 'Mock (Testing)'),
    ]

    organization = models.OneToOneField(
        'core.Organization',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='ai_settings'
    )
    is_enabled = models.BooleanField(
        default=False,
        help_text="Master toggle for AI features in this organization"
    )
    llm_provider = models.CharField(
        max_length=50,
        choices=LLM_PROVIDER_CHOICES,
        default='mock'
    )
    model_name = models.CharField(
        max_length=100,
        default='deepseek-chat',
        help_text="LLM model to use for generation (e.g. deepseek-chat, gpt-4o-mini)"
    )
    max_tokens = models.IntegerField(
        default=1024,
        help_text="Maximum tokens in LLM response"
    )
    temperature = models.FloatField(
        default=0.1,
        help_text="LLM temperature (0.0 = deterministic, 1.0 = creative)"
    )
    top_k_results = models.IntegerField(
        default=5,
        help_text="Number of documents to retrieve per query"
    )
    daily_query_limit = models.IntegerField(
        default=100,
        help_text="Maximum AI queries per day for this organization"
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'AI Settings'
        verbose_name_plural = 'AI Settings'

    def __str__(self):
        status = 'enabled' if self.is_enabled else 'disabled'
        return f"AI Settings for {self.organization.name} ({status})"
