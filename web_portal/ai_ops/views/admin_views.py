"""
AVAGuard AI Operations — Admin UI Views
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.admin_views import role_required
from ..models import AISettings, AIQueryLog


@login_required
@role_required('SUPER_ADMIN', 'IT_ADMIN')
def ai_dashboard(request):
    """
    Renders the AI Operational Dashboard home page for Administrators.
    """
    from ..models import AIQueryFeedback
    org = request.user.organization
    if getattr(request.user, 'role', '') == 'SUPER_ADMIN':
        unresolved_count = AIQueryFeedback.objects.filter(needs_review=True).count()
    else:
        unresolved_count = AIQueryFeedback.objects.filter(query_log__organization=org, needs_review=True).count()

    context = {
        'active_page': 'ai_dashboard',
        'unresolved_feedback_count': unresolved_count,
    }
    return render(request, 'ai_ops/dashboard.html', context)


@login_required
@role_required('SUPER_ADMIN', 'IT_ADMIN')
def ai_admin_settings(request):
    """
    Renders the AI global configurations panel.
    Super Admins have full access, while IT Admins have read-only visibility.
    """
    org = request.user.organization
    ai_settings = None
    if org:
        ai_settings, _ = AISettings.objects.get_or_create(organization=org)

    context = {
        'active_page': 'ai_admin_settings',
        'ai_settings': ai_settings,
        'provider_choices': AISettings.LLM_PROVIDER_CHOICES,
    }
    return render(request, 'ai_ops/admin_settings.html', context)


@login_required
@role_required('SUPER_ADMIN', 'IT_ADMIN')
def ai_admin_audit(request):
    """
    Renders the immutable audit trail and query log timeline.
    """
    context = {
        'active_page': 'ai_admin_audit',
    }
    return render(request, 'ai_ops/admin_audit.html', context)


@login_required
@role_required('SUPER_ADMIN', 'IT_ADMIN')
def ai_retrieval_inspector(request):
    """
    Renders the Retrieval Inspector debug page.
    Allows admins to replay queries and inspect the full pipeline.
    """
    context = {
        'active_page': 'ai_retrieval_inspector',
    }
    return render(request, 'ai_ops/retrieval_inspector.html', context)


@login_required
@role_required('SUPER_ADMIN', 'IT_ADMIN')
def ai_admin_feedback(request):
    """
    Renders the AI Feedback Moderation panel.
    """
    context = {
        'active_page': 'ai_admin_feedback',
    }
    return render(request, 'ai_ops/admin_feedback.html', context)
