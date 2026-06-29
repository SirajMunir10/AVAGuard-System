"""
AVAGuard AI Operations — HTML Template Routing Configuration
"""

from django.urls import path
from . import views

app_name = 'ai_ops_ui'

urlpatterns = [
    # Admin UI views
    path('', views.ai_dashboard, name='dashboard'),
    path('admin/settings/', views.ai_admin_settings, name='admin_settings'),
    path('admin/audit/', views.ai_admin_audit, name='admin_audit'),
    path('admin/inspector/', views.ai_retrieval_inspector, name='retrieval_inspector'),
    path('admin/feedback/', views.ai_admin_feedback, name='admin_feedback'),
    path('admin/rag-status/', views.ai_rag_status, name='rag_status'),

    # User-facing UI views
    path('query/', views.ai_query, name='query'),
    path('history/', views.ai_history, name='history'),
    path('document/<path:relative_path>/', views.ai_document_view, name='document_view'),
]
