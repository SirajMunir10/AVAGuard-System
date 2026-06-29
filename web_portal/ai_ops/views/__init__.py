"""
AVAGuard AI Operations Views Package Initializer
"""

from .api_views import (
    AIQueryView,
    AIAskFindingView,
    AIQueryHistoryView,
    AISettingsView,
    AIAuditLogView,
    AIStatsView,
    SetAIModeView,
    AIRetrievalInspectView,
    AIFeedbackView,
    AIFeedbackResolveView,
    AIDocumentContentView,
    AIClearCacheView,
)

from .dashboard_views import (
    ai_query,
    ai_history,
    ai_rag_status,
    ai_document_view,
)

from .admin_views import (
    ai_dashboard,
    ai_admin_settings,
    ai_admin_audit,
    ai_retrieval_inspector,
    ai_admin_feedback,
)
