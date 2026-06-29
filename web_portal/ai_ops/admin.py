from django.contrib import admin
from .models import AIQueryLog, KnowledgeDocument, AISettings


@admin.register(AIQueryLog)
class AIQueryLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'query_text_preview', 'model_used', 'latency_ms', 'flagged', 'created_at')
    list_filter = ('flagged', 'model_used', 'created_at')
    search_fields = ('query_text', 'response_text')
    readonly_fields = ('id', 'user', 'organization', 'query_text', 'sanitized_query',
                       'retrieved_sources', 'response_text', 'grounding_score',
                       'model_used', 'latency_ms', 'retrieval_ms', 'token_count',
                       'flagged', 'created_at')
    ordering = ('-created_at',)

    def query_text_preview(self, obj):
        return obj.query_text[:80] + '...' if len(obj.query_text) > 80 else obj.query_text
    query_text_preview.short_description = 'Query'

    def has_add_permission(self, request):
        return False  # Logs are created by the API only

    def has_change_permission(self, request, obj=None):
        return False  # Immutable

    def has_delete_permission(self, request, obj=None):
        return False  # Immutable


@admin.register(KnowledgeDocument)
class KnowledgeDocumentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'source_type', 'word_count', 'is_active', 'ingested_at')
    list_filter = ('source_type', 'is_active')
    search_fields = ('filename',)


@admin.register(AISettings)
class AISettingsAdmin(admin.ModelAdmin):
    list_display = ('organization', 'is_enabled', 'llm_provider', 'daily_query_limit')
