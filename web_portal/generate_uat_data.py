from django.utils import timezone
from core.models import Organization, User, ScanSummary, ScanResult
import uuid

def generate_uat_data():
    org, _ = Organization.objects.get_or_create(name='UAT Org', domain_filter='uat.com')
    user, _ = User.objects.get_or_create(email='admin@uat.com', organization=org, defaults={'role': 'ADMIN'})
    
    scan_id = uuid.uuid4()
    summary = ScanSummary.objects.create(
        id=scan_id,
        organization=org,
        uploaded_by=user,
        overall_score=45,
        total_checks=105,
        passed_count=5,
        failed_count=100,
        scan_timestamp=timezone.now()
    )
    
    results = []
    
    # 1. Native FindingBuilder Schema (PASS -> Coerced to INFO)
    results.append(ScanResult(
        scan=summary,
        check_id="UAT-001",
        title="Verify MFA Status",
        status="PASS",
        finding_severity="INFO",
        rule_severity="CRITICAL",
        category="Identity",
        source_engine="avaguard-cis-engine",
        finding_type="compliance_misconfiguration",
        details="Ensure MFA is enabled for all admin users.",
        why_it_matters="Prevents credential stuffing attacks.",
        error_message="",
        evidence={"compliant_users": ["admin@uat.com", "sec@uat.com"]},
        remediation="Already compliant."
    ))
    
    # 2. Native FindingBuilder Schema (FAIL -> Renders Table)
    results.append(ScanResult(
        scan=summary,
        check_id="UAT-002",
        title="Ensure Disks are Encrypted",
        status="FAIL",
        finding_severity="HIGH",
        rule_severity="HIGH",
        category="Compute",
        source_engine="avaguard-vuln-engine",
        finding_type="vulnerability",
        details="All OS disks must be encrypted at rest.",
        why_it_matters="Protects data from physical theft.",
        error_message="Found unencrypted disks in production.",
        evidence={"cve_id": "CVE-2024-UAT", "cvss_score": 8.5, "missing_protocols": ["TLS 1.2"]},
        non_compliant_resources=["vm-prod-01", "vm-prod-02"],
        remediation="Navigate to Azure Portal > Disks > Enable Encryption.",
        references=["https://docs.microsoft.com/azure/security"]
    ))
    
    # 3. Legacy Scanner Output (XSS Protection Test)
    results.append(ScanResult(
        scan=summary,
        check_id="UAT-003",
        title="Legacy Audit Check",
        status="WARNING",
        finding_severity="MEDIUM",
        rule_severity="MEDIUM",
        category="Legacy",
        source_engine="avaguard-cis-engine-legacy",
        finding_type="legacy_audit_record",
        details="Legacy Check",
        why_it_matters="Context not provided by legacy scanner.",
        error_message="See raw output below.",
        evidence={"legacy_details": "<script>alert('XSS Attack Failed!');</script> Legacy scanner found bad config.", "compliant_count": 0, "non_compliant_count": 1, "total_count": 1},
        remediation="Consult CIS Benchmarks."
    ))

    # 4. Generate 102 more dummy findings to test Pagination (>100 total)
    for i in range(4, 106):
        results.append(ScanResult(
            scan=summary,
            check_id=f"UAT-{str(i).zfill(3)}",
            title=f"Pagination Filler Check {i}",
            status="FAIL",
            finding_severity="LOW",
            rule_severity="LOW",
            category="System",
            details="Filler check for pagination test."
        ))

    ScanResult.objects.bulk_create(results)
    print(f"\\n[SUCCESS] UAT Data Generated! Open: /admin/scan/{scan_id}/")

generate_uat_data()
