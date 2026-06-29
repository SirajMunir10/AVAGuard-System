"""
AVAGuard AI Operations — DRF Serializers
"""

from rest_framework import serializers


class AIQueryRequestSerializer(serializers.Serializer):
    """Validates incoming AI query requests."""
    query = serializers.CharField(
        max_length=2000,
        help_text="Natural language compliance question"
    )
    top_k = serializers.IntegerField(
        required=False,
        default=5,
        min_value=1,
        max_value=20,
        help_text="Number of source documents to retrieve (1-20)"
    )
    framework = serializers.CharField(
        required=False,
        default='',
        allow_blank=True,
        help_text="Filter results to a specific framework (e.g., 'CIS', 'NIST', 'AWS Security')"
    )


class AIAskFindingRequestSerializer(serializers.Serializer):
    """Validates incoming queries for the Ask AI finding endpoint."""
    query = serializers.CharField(
        max_length=2000,
        required=False,
        allow_blank=True,
        default="Please provide a step-by-step remediation guide based on this finding.",
        help_text="Specific question about the finding"
    )


class AISourceSerializer(serializers.Serializer):
    """Serializes a single retrieved source document."""
    filename = serializers.CharField()
    score = serializers.FloatField()
    snippet = serializers.CharField()


class AIQueryResponseSerializer(serializers.Serializer):
    """Serializes the AI query response."""
    answer = serializers.CharField()
    sources = AISourceSerializer(many=True)
    query_id = serializers.UUIDField()
    model_used = serializers.CharField()
    latency_ms = serializers.FloatField()
    retrieval_ms = serializers.FloatField()


class AIQueryLogSerializer(serializers.Serializer):
    """Serializes query history entries."""
    id = serializers.UUIDField()
    query_text = serializers.CharField()
    response_text = serializers.CharField()
    model_used = serializers.CharField()
    latency_ms = serializers.FloatField()
    retrieval_ms = serializers.FloatField()
    sources_count = serializers.SerializerMethodField()
    flagged = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    # Phase 1 fields
    mode = serializers.CharField()
    confidence_level = serializers.CharField()
    retrieval_method = serializers.CharField()
    rerank_latency_ms = serializers.FloatField()
    average_similarity_score = serializers.FloatField()
    top_similarity_score = serializers.FloatField()
    retrieved_document_count = serializers.IntegerField()
    reranker_scores = serializers.JSONField()
    retrieved_sources = serializers.JSONField()

    def get_sources_count(self, obj):
        sources = obj.retrieved_sources
        if isinstance(sources, list):
            return len(sources)
        return 0
