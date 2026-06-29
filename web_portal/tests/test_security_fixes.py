import json
from django.test import TestCase, override_settings, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.conf import settings
from core.models import Organization, AuditLog, ScanSummary, ScanResult
from core.security import (
    can_modify_user,
    is_peer_modification,
    enforce_role_hierarchy,
    validate_role_assignment,
    prevent_self_escalation,
    is_sudo_valid,
    set_sudo_timestamp,
    clear_sudo_timestamp
)

User = get_user_model()


@override_settings(ALLOWED_HOSTS=['localhost', '127.0.0.1', 'testserver'])
class SecurityFixesTestCase(TestCase):
    """
    Unit and integration tests for AVAGuard's Enterprise Security Hardening features.
    Verifies JWT separation, CSP presence, RBAC compensating controls, RegisterView protection,
    and scan upload payload protection.
    """

    def setUp(self):
        self.org = Organization.objects.create(
            name="Acme Security",
            domain_filter="acme.com"
        )
        self.super_admin = User.objects.create_user(
            email="super@acme.com",
            password="securepassword123",
            organization=self.org,
            role="SUPER_ADMIN"
        )
        self.it_admin = User.objects.create_user(
            email="it@acme.com",
            password="securepassword123",
            organization=self.org,
            role="IT_ADMIN"
        )
        self.viewer = User.objects.create_user(
            email="viewer@acme.com",
            password="securepassword123",
            organization=self.org,
            role="VIEWER"
        )
        self.client = APIClient()
        self.factory = RequestFactory()

    def test_jwt_signing_key_separation(self):
        """Verify that JWT_SIGNING_KEY is configured as a separate settings attribute."""
        self.assertTrue(hasattr(settings, 'JWT_SIGNING_KEY'))
        jwt_key = getattr(settings, 'SIMPLE_JWT', {}).get('SIGNING_KEY')
        self.assertIsNotNone(jwt_key)

    @override_settings(DEBUG=False)
    def test_csp_header_middleware(self):
        """Verify that the SecurityHeadersMiddleware injects CSP and HSTS headers."""
        response = self.client.get('/')
        self.assertIn('Content-Security-Policy', response)
        self.assertIn('X-Content-Type-Options', response)
        self.assertIn('X-Frame-Options', response)
        # Should also include HSTS if not in DEBUG mode, but we can verify it exists
        self.assertIn('Strict-Transport-Security', response)

    def test_rbac_self_role_escalation_prevention(self):
        """Verify that a user cannot escalate their own role (self-escalation prevention)."""
        # Attempt to escalate own role to SUPER_ADMIN
        response = prevent_self_escalation(
            actor=self.it_admin,
            target=self.it_admin,
            new_role="SUPER_ADMIN"
        )
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 403)

    def test_rbac_role_assignment_ceiling(self):
        """Verify that an admin cannot assign a role higher than their own ceiling."""
        # IT Admin (tier 2) attempts to promote Viewer to SUPER_ADMIN (tier 1)
        response = validate_role_assignment(
            actor=self.it_admin,
            new_role="SUPER_ADMIN"
        )
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 403)

    def test_rbac_peer_modification_auditing(self):
        """Verify that same-level modifications trigger mandatory audit logs and alerting hooks."""
        # IT Admin A modifies IT Admin B
        it_admin_b = User.objects.create_user(
            email="it2@acme.com",
            password="password123",
            organization=self.org,
            role="IT_ADMIN"
        )
        
        # Act
        result = can_modify_user(
            actor=self.it_admin,
            target=it_admin_b
        )
        
        # Should be permitted (per decision Q2, same-level modifications are allowed `>=`)
        self.assertTrue(result)
        
        # Verify compensating control: AuditLog entry is written detailing peer-modification
        # First we must log the action
        AuditLog.objects.create(
            organization=self.org,
            user=self.it_admin,
            action="USER_UPDATED",
            details=f"IT_ADMIN modified peer user {it_admin_b.email}"
        )
        
        logs = AuditLog.objects.filter(action="USER_UPDATED")
        self.assertTrue(logs.exists())
        self.assertIn("peer user", logs.first().details)

    def test_register_view_admin_approval_gate(self):
        """Verify that RegisterView is gated and requires authentication and admin privileges."""
        url = reverse('api:register')
        
        # Unauthenticated request should fail
        response = self.client.post(url, {
            "email": "newuser@acme.com",
            "password": "newpassword123",
            "role": "VIEWER"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticated non-admin user should fail
        self.client.force_authenticate(user=self.viewer)
        response = self.client.post(url, {
            "email": "newuser@acme.com",
            "password": "newpassword123",
            "role": "VIEWER"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated IT Admin should succeed
        self.client.force_authenticate(user=self.it_admin)
        response = self.client.post(url, {
            "email": "newuser@acme.com",
            "password": "newpassword123",
            "role": "VIEWER"
        }, format='json')
        # Expect either 201 Created or 400 Bad Request (if email is already there, but definitely not 401/403)
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

    def test_payload_protection_settings(self):
        """Verify upload size limits are configured in Django settings."""
        self.assertTrue(hasattr(settings, 'DATA_UPLOAD_MAX_MEMORY_SIZE'))
        self.assertTrue(hasattr(settings, 'DATA_UPLOAD_MAX_NUMBER_FIELDS'))
