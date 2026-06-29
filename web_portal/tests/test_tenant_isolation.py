import uuid
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from core.models import Organization, ScanSummary, ScanResult, CompliancePolicy, AuditLog, Policy
from core.tenant_manager import TenantAwareManager
from core.tenant_middleware import TenantMiddleware

User = get_user_model()


class TenantIsolationTestCase(TestCase):
    """
    Unit and integration tests for AVAGuard's Multi-Tenant Isolation Layer.
    Ensures complete database-level and query-level isolation between organizations.
    """

    def setUp(self):
        # Create Organizations (Tenants)
        self.org_a = Organization.objects.create(
            name="Acme Corp",
            domain_filter="acme.com",
            tier="PREMIUM"
        )
        self.org_b = Organization.objects.create(
            name="Stark Industries",
            domain_filter="stark.com",
            tier="ENTERPRISE"
        )

        # Create Users
        self.user_a = User.objects.create_user(
            email="tony@acme.com",
            password="testpassword123",
            organization=self.org_a,
            role="IT_ADMIN"
        )
        self.user_b = User.objects.create_user(
            email="pepper@stark.com",
            password="testpassword123",
            organization=self.org_b,
            role="SUPER_ADMIN"
        )

        # Create Scans for Tenant A
        self.scan_a = ScanSummary.objects.create(
            id=uuid.UUID("11111111-1111-1111-1111-111111111111"),
            organization=self.org_a,
            uploaded_by=self.user_a,
            overall_score=85.50,
            passed_count=8,
            failed_count=2,
            total_checks=10
        )
        self.result_a = ScanResult.objects.create(
            id=uuid.UUID("11111111-1111-1111-1111-222222222222"),
            scan=self.scan_a,
            check_id="AZ-01",
            cis_control_id="1.1",
            title="Ensure MFA is enabled for all users",
            status="PASS",
            severity="HIGH"
        )

        # Create Scans for Tenant B
        self.scan_b = ScanSummary.objects.create(
            id=uuid.UUID("22222222-2222-2222-2222-222222222222"),
            organization=self.org_b,
            uploaded_by=self.user_b,
            overall_score=45.00,
            passed_count=4,
            failed_count=6,
            total_checks=10
        )
        self.result_b = ScanResult.objects.create(
            id=uuid.UUID("22222222-2222-2222-2222-333333333333"),
            scan=self.scan_b,
            check_id="AZ-01",
            cis_control_id="1.1",
            title="Ensure MFA is enabled for all users",
            status="FAIL",
            severity="HIGH"
        )

        # Create Compliance Policies
        self.policy_a = CompliancePolicy.objects.create(
            organization=self.org_a,
            check_id="AZ-01",
            is_enabled=True
        )
        self.policy_b = CompliancePolicy.objects.create(
            organization=self.org_b,
            check_id="AZ-01",
            is_enabled=False
        )

        # Create Policies
        self.custom_policy_a = Policy.objects.create(
            organization=self.org_a,
            name="Acme Custom Policy",
            check_id="AZ-02",
            status="ACTIVE"
        )
        self.custom_policy_b = Policy.objects.create(
            organization=self.org_b,
            name="Stark Custom Policy",
            check_id="AZ-02",
            status="DISABLED"
        )

        # Create Audit Logs
        self.audit_a = AuditLog.objects.create(
            organization=self.org_a,
            user=self.user_a,
            action="LOGIN",
            details="User logged in from Acme IP"
        )
        self.audit_b = AuditLog.objects.create(
            organization=self.org_b,
            user=self.user_b,
            action="LOGIN",
            details="User logged in from Stark IP"
        )

        self.factory = RequestFactory()

    def test_scan_summary_tenant_isolation(self):
        """Verify ScanSummary.objects.for_tenant() returns ONLY scoped tenant scans."""
        scans_a = ScanSummary.objects.for_tenant(self.org_a)
        self.assertEqual(scans_a.count(), 1)
        self.assertEqual(scans_a.first().id, self.scan_a.id)

        scans_b = ScanSummary.objects.for_tenant(self.org_b)
        self.assertEqual(scans_b.count(), 1)
        self.assertEqual(scans_b.first().id, self.scan_b.id)

        # Unscoped bypass
        all_scans = ScanSummary.objects.unscoped()
        self.assertGreaterEqual(all_scans.count(), 2)

    def test_scan_result_tenant_isolation(self):
        """Verify ScanResult.objects.for_tenant() filters via scan relationship correctly."""
        results_a = ScanResult.objects.for_tenant(self.org_a)
        self.assertEqual(results_a.count(), 1)
        self.assertEqual(results_a.first().id, self.result_a.id)

        results_b = ScanResult.objects.for_tenant(self.org_b)
        self.assertEqual(results_b.count(), 1)
        self.assertEqual(results_b.first().id, self.result_b.id)

        # Unscoped bypass
        all_results = ScanResult.objects.unscoped()
        self.assertGreaterEqual(all_results.count(), 2)

    def test_compliance_policy_tenant_isolation(self):
        """Verify CompliancePolicy.objects.for_tenant() isolates organization policies."""
        policies_a = CompliancePolicy.objects.for_tenant(self.org_a)
        self.assertEqual(policies_a.count(), 1)
        self.assertEqual(policies_a.first().id, self.policy_a.id)

        policies_b = CompliancePolicy.objects.for_tenant(self.org_b)
        self.assertEqual(policies_b.count(), 1)
        self.assertEqual(policies_b.first().id, self.policy_b.id)

    def test_audit_log_tenant_isolation(self):
        """Verify AuditLog.objects.for_tenant() isolates enterprise audit trails."""
        audits_a = AuditLog.objects.for_tenant(self.org_a)
        self.assertEqual(audits_a.count(), 1)
        self.assertEqual(audits_a.first().id, self.audit_a.id)

        audits_b = AuditLog.objects.for_tenant(self.org_b)
        self.assertEqual(audits_b.count(), 1)
        self.assertEqual(audits_b.first().id, self.audit_b.id)

    def test_policy_tenant_isolation(self):
        """Verify Policy.objects.for_tenant() isolates security policies."""
        p_a = Policy.objects.for_tenant(self.org_a)
        self.assertEqual(p_a.count(), 1)
        self.assertEqual(p_a.first().id, self.custom_policy_a.id)

        p_b = Policy.objects.for_tenant(self.org_b)
        self.assertEqual(p_b.count(), 1)
        self.assertEqual(p_b.first().id, self.custom_policy_b.id)

    def test_empty_tenant_handling(self):
        """Verify that calling for_tenant(None) returns self.none() for protection."""
        self.assertEqual(ScanSummary.objects.for_tenant(None).count(), 0)
        self.assertEqual(ScanResult.objects.for_tenant(None).count(), 0)
        self.assertEqual(AuditLog.objects.for_tenant(None).count(), 0)

    def test_tenant_middleware(self):
        """Verify TenantMiddleware attaches the current user's organization to the request."""
        middleware = TenantMiddleware(lambda r: None)

        # Unauthenticated request
        request_anon = self.factory.get("/dashboard/")
        request_anon.user = AnonymousUser()
        middleware.process_request(request_anon)
        self.assertIsNone(request_anon.organization)

        # Authenticated request (User A)
        request_a = self.factory.get("/dashboard/")
        request_a.user = self.user_a
        middleware.process_request(request_a)
        self.assertEqual(request_a.organization, self.org_a)

        # Authenticated request (User B)
        request_b = self.factory.get("/dashboard/")
        request_b.user = self.user_b
        middleware.process_request(request_b)
        self.assertEqual(request_b.organization, self.org_b)
