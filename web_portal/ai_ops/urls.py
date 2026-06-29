"""
AVAGuard AI Operations — URL Configuration
"""

from django.urls import path
from . import views

app_name = 'ai_ops'

urlpatterns = [
    # User-facing AI query endpoints
    path('query/', views.AIQueryView.as_view(), name='query'),
    path('ask-finding/<uuid:result_id>/', views.AIAskFindingView.as_view(), name='ask_finding'),
    path('history/', views.AIQueryHistoryView.as_view(), name='history'),
    path('set-mode/', views.SetAIModeView.as_view(), name='set_mode'),
    path('feedback/', views.AIFeedbackView.as_view(), name='feedback'),
    path('document/content/', views.AIDocumentContentView.as_view(), name='document_content'),

    # SuperAdmin management endpoints (RBAC-protected)
    path('admin/settings/', views.AISettingsView.as_view(), name='admin_settings'),
    path('admin/audit/', views.AIAuditLogView.as_view(), name='admin_audit'),
    path('admin/stats/', views.AIStatsView.as_view(), name='admin_stats'),
    path('admin/inspect/', views.AIRetrievalInspectView.as_view(), name='admin_inspect'),
    path('admin/feedback/resolve/', views.AIFeedbackResolveView.as_view(), name='admin_feedback_resolve'),
    path('admin/clear-cache/', views.AIClearCacheView.as_view(), name='admin_clear_cache'),
]

