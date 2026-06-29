"""
Functional Tests for AI HTML template views (ai_ops/views/dashboard_views.py and admin_views.py).
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Organization, User
from ai_ops.models import AISettings


class AIUIViewsTestCase(TestCase):
    """Test suite for AI HTML views."""

    def setUp(self):
        self.org = Organization.objects.create(name='TestOrg', tier='PREMIUM')
        
        # Super Admin
        self.super_admin = User.objects.create_user(
            email='super@test.com',
            password='TestPass123!',
            organization=self.org,
            role='SUPER_ADMIN',
        )

        # IT Admin
        self.it_admin = User.objects.create_user(
            email='itadmin@test.com',
            password='TestPass123!',
            organization=self.org,
            role='IT_ADMIN',
        )

        # Regular Viewer
        self.viewer = User.objects.create_user(
            email='viewer@test.com',
            password='TestPass123!',
            organization=self.org,
            role='VIEWER',
        )

        # Settings
        self.ai_settings = AISettings.objects.create(
            organization=self.org,
            is_enabled=True,
            llm_provider='mock',
        )

    # ── 1. General User Views (Query, History) ──
    def test_authenticated_user_can_access_query_console(self):
        """Standard authenticated user can render the Q&A compliance workspace."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:query'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_ops/ai_query.html')
        self.assertIn('ai_settings', response.context)
        self.assertEqual(response.context['active_page'], 'ai_query')

    def test_authenticated_user_can_access_history_page(self):
        """Standard authenticated user can render their query history list."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_ops/history.html')
        self.assertEqual(response.context['active_page'], 'ai_history')

    def test_unauthenticated_user_redirected_to_login(self):
        """Unauthenticated user is redirected to the login page when requesting AI UIs."""
        # Query console
        response = self.client.get(reverse('ai_ops_ui:query'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/login/?next=/ai/query/')

        # Admin Dashboard
        response = self.client.get(reverse('ai_ops_ui:dashboard'))
        self.assertEqual(response.status_code, 302)

    # ── 2. Admin Views (Dashboard, Settings, Audit) ──
    def test_it_admin_can_access_dashboard(self):
        """IT Admin can access the operational dashboard."""
        self.client.login(email='itadmin@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_ops/dashboard.html')

    def test_super_admin_can_access_dashboard(self):
        """Super Admin can access the operational dashboard."""
        self.client.login(email='super@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_viewer_is_blocked_from_admin_dashboard(self):
        """Viewer role is blocked from the administrative dashboard and redirected."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:dashboard'))
        # The role_required decorator redirects unauthorized users to 'dashboard' with error message
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dashboard/', fetch_redirect_response=False)

    def test_super_admin_can_access_settings_panel(self):
        """Super Admin can access the settings configuration panel."""
        self.client.login(email='super@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:admin_settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_ops/admin_settings.html')
        self.assertEqual(response.context['ai_settings'].llm_provider, 'mock')

    def test_it_admin_can_access_settings_panel(self):
        """IT Admin can access the settings configuration panel (read-only in template)."""
        self.client.login(email='itadmin@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:admin_settings'))
        self.assertEqual(response.status_code, 200)

    def test_viewer_is_blocked_from_settings_panel(self):
        """Viewer role is blocked from settings and redirected."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:admin_settings'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dashboard/', fetch_redirect_response=False)

    def test_super_admin_can_access_audit_timeline(self):
        """Super Admin can access the query logs audit timeline."""
        self.client.login(email='super@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:admin_audit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_ops/admin_audit.html')

    def test_viewer_is_blocked_from_audit_timeline(self):
        """Viewer role is blocked from audit timeline and redirected."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:admin_audit'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dashboard/', fetch_redirect_response=False)

    # ── 3. RAG Status Page Tests ──
    def test_super_admin_can_access_rag_status(self):
        """Super Admin can access the RAG System Health page."""
        self.client.login(email='super@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:rag_status'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_ops/rag_status.html')
        self.assertEqual(response.context['active_page'], 'ai_rag_status')

    def test_it_admin_can_access_rag_status(self):
        """IT Admin can access the RAG System Health page."""
        self.client.login(email='itadmin@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:rag_status'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ai_ops/rag_status.html')

    def test_viewer_is_blocked_from_rag_status(self):
        """Viewer role is blocked from the RAG Status page with 403."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:rag_status'))
        self.assertEqual(response.status_code, 403)

    def test_rag_status_context_contains_index_files(self):
        """RAG Status page context includes index_files list."""
        self.client.login(email='super@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:rag_status'))
        self.assertIn('index_files', response.context)
        self.assertIn('corpus_stats', response.context)
        self.assertIn('retriever_ready', response.context)

    # ── 4. AI Query Page Extended Tests ──
    def test_query_page_context_has_mode_and_frameworks(self):
        """AI Query page context includes mode, frameworks, and recent_queries."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:query'))
        self.assertIn('mode', response.context)
        self.assertIn('available_frameworks', response.context)
        self.assertIn('recent_queries', response.context)

    def test_query_page_default_mode_is_ai(self):
        """Default mode for query page should be 'ai' if not set in session."""
        self.client.login(email='viewer@test.com', password='TestPass123!')
        response = self.client.get(reverse('ai_ops_ui:query'))
        self.assertEqual(response.context['mode'], 'ai')

    def test_unauthenticated_user_blocked_from_rag_status(self):
        """Unauthenticated user is redirected to login for RAG status page."""
        response = self.client.get(reverse('ai_ops_ui:rag_status'))
        self.assertEqual(response.status_code, 302)
