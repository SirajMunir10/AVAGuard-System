import os
import json
import pytest
import hashlib
from pathlib import Path
from datetime import datetime

from avaguard_core.providers.base import ProviderCapabilities, QueryResponse
from avaguard_core.providers.registry import ProviderRegistry
from avaguard_core.providers.azure.provider import AzureProvider
from avaguard_core.providers.evidence import classify_evidence
from avaguard_core.benchmarks.loader import BenchmarkLoader
from avaguard_core.checks import AVAILABLE_CHECKS, FREE_TIER_CHECKS, PREMIUM_CHECKS
from avaguard_core.framework_mapper import FrameworkMapper
from avaguard_core.errors import BenchmarkValidationError, ProviderAuthError, EvidenceCollectionError


def test_azure_provider_registration_and_capabilities():
    """Verify that AzureProvider is auto-registered and exposes rich capabilities."""
    registered = ProviderRegistry.get_registered_providers()
    assert "azure" in registered

    caps = ProviderRegistry.get_capabilities()
    assert "azure" in caps
    azure_caps = caps["azure"]
    assert azure_caps.display_name == "Microsoft Azure AD & CIS Ingestion Provider"
    assert "users" in azure_caps.supported_services
    assert "azure_cli" in azure_caps.supported_remediations
    assert "mock" in azure_caps.authentication_modes


def test_azure_provider_mock_initialization():
    """Verify that AzureProvider initializes correctly in mock mode and is healthy."""
    provider = AzureProvider()
    credentials = {
        "use_mock": True,
        "mock_data_file": "datasets/failure_0.json"
    }
    
    provider.initialize(credentials)
    assert provider.use_mock is True
    assert provider.is_healthy() is True


def test_evidence_classification_and_redaction():
    """Verify that evidence is split into tiers and AI-Safe blocks are strictly redacted."""
    raw_resources = [
        {
            "id": "user-001",
            "displayName": "Tony Stark",
            "userPrincipalName": "tony@starkindustries.com",
            "mail": "tony@starkindustries.com",
            "temp_session": "secret-session-token-abc",
            "password": "SuperSecurePassword123",
            "client_secret": "sensitive-credential-value",
            "ipAddress": "192.168.1.100",
            "nested_data": {
                "tenantId": "1234abcd-1234-abcd-1234-123456789abc",
                "secret_key": "some-api-token"
            }
        }
    ]

    classified = classify_evidence(raw_resources)

    # 1. Raw checks
    assert len(classified["raw"]) == 1
    assert classified["raw"][0]["password"] == "SuperSecurePassword123"

    # 2. Normalized checks
    assert len(classified["normalized"]) == 1
    assert "userPrincipalName" in classified["normalized"][0]

    # 3. Audit-Safe checks: strips volatile session state
    assert "temp_session" not in classified["audit_safe"][0]
    assert "password" in classified["audit_safe"][0] # Remains in audit-safe

    # 4. AI-Safe checks: MANDATORY scrubbing of secrets, tenant IDs, PII, names, emails, IPs, UUIDs
    ai_safe_res = classified["ai_safe"][0]
    assert ai_safe_res["displayName"] == "[REDACTED_DISPLAYNAME]"
    assert ai_safe_res["userPrincipalName"] == "[REDACTED_USERPRINCIPALNAME]"
    assert ai_safe_res["mail"] == "[REDACTED_MAIL]"
    assert ai_safe_res["password"] == "[REDACTED_SENSITIVE_FIELD]"
    assert ai_safe_res["client_secret"] == "[REDACTED_SENSITIVE_FIELD]"
    assert ai_safe_res["ipAddress"] == "[REDACTED_SENSITIVE_FIELD]"
    
    # Nested field scrubbing
    assert ai_safe_res["nested_data"]["tenantId"] == "[REDACTED_SENSITIVE_FIELD]"
    assert ai_safe_res["nested_data"]["secret_key"] == "[REDACTED_SENSITIVE_FIELD]"


def test_integrity_manifest_tampering_verification(tmp_path):
    """Verify that tampered JSON checks fail SHA-256 manifest verification."""
    # 1. Setup temporary benchmark directory with JSON check and manifest
    bench_dir = tmp_path / "benchmarks"
    bench_dir.mkdir()
    
    check_file = bench_dir / "test_check.json"
    check_content = {
        "control_id": "99.9.9",
        "title": "Test Integrity",
        "version": "1.0",
        "deprecated": False,
        "profile_level": "Level 1",
        "provider_compatibility": ["azure"],
        "category": "Test",
        "scan_query": {"resource_type": "users"},
        "evaluation_rules": [],
        "remediation_metadata": {"severity": "LOW", "impact_statement": "x", "validation_steps": "x"}
    }
    
    check_file.write_text(json.dumps(check_content), encoding="utf-8")
    
    # Compute valid hash
    file_bytes = check_file.read_bytes()
    valid_hash = hashlib.sha256(file_bytes).hexdigest()
    
    manifest_file = bench_dir / "manifest.sha256"
    manifest_file.write_text(f"{valid_hash} test_check.json\n", encoding="utf-8")

    # Loader verification: Should load fine with matching manifest hash
    loader = BenchmarkLoader("Test", "1.0", "azure")
    loaded = loader.load_control_from_file(str(check_file))
    assert loaded.control_id == "99.9.9"

    # Tampering check: modify JSON content
    check_file.write_text(json.dumps(check_content | {"title": "TAMPERED TITLE"}), encoding="utf-8")

    # Loader verification: Should fail now due to mismatching hash
    with pytest.raises(BenchmarkValidationError) as exc:
        loader.load_control_from_file(str(check_file))
    assert "Integrity check failed" in str(exc.value)


def test_dynamic_declarative_check_compilation():
    """Verify that declarative JSON checks are compiled dynamically into global registers."""
    assert "10.3.12" in AVAILABLE_CHECKS
    assert "2.2.1" in AVAILABLE_CHECKS

    check_class = AVAILABLE_CHECKS["10.3.12"]
    assert check_class.TITLE == "Ensure Redundancy is set to 'geo-redundant storage (GRS)' on critical Azure Storage"
    assert check_class.CATEGORY == "Storage"
    assert check_class.CIS_SEVERITY.value == "MEDIUM"


def test_data_driven_framework_mapper():
    """Verify that FrameworkMapper resolves NIST/ISO mappings dynamically from check metadata."""
    # 1. Dynamic Check mapping
    mapping = FrameworkMapper.get_mapping("10.3.12")
    assert "CP-9" in mapping.nist_800_53
    assert "CP-10" in mapping.nist_800_53
    assert "A.17.1.1" in mapping.iso_27001
    
    # 2. Legacy Check mapping (static fallback verification)
    legacy_mapping = FrameworkMapper.get_mapping("1.1")
    assert "AC-2(1)" in legacy_mapping.nist_800_53
    assert "A.9.4.2" in legacy_mapping.iso_27001
