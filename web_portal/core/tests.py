from django.test import TestCase, RequestFactory
from django.utils import timezone
from core.models import Organization, User, ScanSummary, ScanResult
from core.normalizer import FindingNormalizer, ValidationError
from core.sync_service import DesktopSyncService
from core.admin_views import scan_detail
from django.contrib.messages.storage.fallback import FallbackStorage
import uuid

class Phase4EValidationTests(TestCase):
    def setUp(self):
        self.org = Organization.objects.create(name='Test Org', domain_filter='test.com')
        self.user = User.objects.create(email='test@test.com', organization=self.org)
        self.factory = RequestFactory()

    def test_normalizer_native_schema(self):
        """Test FindingNormalizer with native Phase 4B JSON payload."""
        raw_payload = {
            "check_id": "test_001",
            "title": "Test Native Check",
            "status": "FAIL",
            "severity": "HIGH",
            "metadata": {
                "finding_type": "compliance_misconfiguration",
                "finding_severity": "CRITICAL",
                "context": {
                    "description": "Ensure native checks work",
                    "why_it_matters": "Risk context"
                },
                "technical_evidence": {
                    "raw_output": {"key": "value"}
                }
            }
        }
        normalized = FindingNormalizer.normalize_finding(raw_payload, str(uuid.uuid4()))
        self.assertEqual(normalized['status'], 'FAIL')
        self.assertEqual(normalized['finding_severity'], 'CRITICAL')
        self.assertEqual(normalized['evidence'], {"key": "value"})

    def test_normalizer_legacy_schema(self):
        """Test FindingNormalizer with legacy flat string payload."""
        raw_payload = {
            "checkId": "legacy_001",
            "title": "Test Legacy Check",
            "result": "PASS",
            "severity": "LOW",
            "details": "<script>alert(1)</script> Found issue",
            "remediation": "Do this"
        }
        normalized = FindingNormalizer.normalize_finding(raw_payload, str(uuid.uuid4()))
        self.assertEqual(normalized['status'], 'PASS')
        self.assertEqual(normalized['finding_severity'], 'INFO') # Coerced
        self.assertEqual(normalized['evidence']['legacy_details'], 'alert(1) Found issue') # XSS stripped

    def test_sync_service_end_to_end(self):
        """Test SyncService ingestion and DB persistence."""
        service = DesktopSyncService(organization=self.org)
        scan_id = uuid.uuid4()
        scan_data = {
            'scan_id': scan_id,
            'score': 80,
            'json_data': {
                'checks': [
                    {
                        "check_id": "c1",
                        "title": "Test Check 1",
                        "status": "FAIL",
                        "metadata": {"finding_type": "test"}
                    }
                ]
            }
        }
        summary = service.sync_scan(scan_data, user=self.user)
        self.assertIsNotNone(summary)
        
        # Verify DB
        results = ScanResult.objects.filter(scan=summary)
        self.assertEqual(results.count(), 1)
        self.assertEqual(results.first().check_id, "c1")

    def test_scan_detail_pagination(self):
        """Test that the view paginates large results correctly."""
        summary = ScanSummary.objects.create(
            id=uuid.uuid4(), organization=self.org, overall_score=50,
            scan_timestamp=timezone.now()
        )
        # Create 150 results
        results = [
            ScanResult(scan=summary, check_id=f"c{i}", status="FAIL")
            for i in range(150)
        ]
        ScanResult.objects.bulk_create(results)
        
        request = self.factory.get(f'/admin/scan/{summary.id}/?page=1')
        request.user = self.user
        setattr(request, 'session', {})
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        
        response = scan_detail(request, summary.id)
        self.assertEqual(response.status_code, 200)
        
        # Validate Paginator context
        page_obj = response.context_data.get('page_obj', response.context.get('page_obj')) if hasattr(response, 'context_data') else None
        if not page_obj:
            # Fallback for Django 3.x if response.context is used
            # Actually, render() doesn't attach context cleanly in simple unit tests without a test client.
            # We'll just rely on the response content instead or use Client.
            pass
        self.assertContains(response, 'Page 1 of 2')
        self.assertContains(response, 'finding-accordion', count=100) # Only 100 on first page
