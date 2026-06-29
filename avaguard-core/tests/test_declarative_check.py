import os
import json
import pytest
from datetime import datetime

from avaguard_core.providers.base import CloudProvider, ProviderCapabilities, QueryResponse
from avaguard_core.providers.registry import ProviderRegistry
from avaguard_core.benchmarks.models import ControlDefinition, BenchmarkVersion
from avaguard_core.benchmarks.loader import BenchmarkLoader
from avaguard_core.remediation.engine import RemediationEngine
from avaguard_core.checks.declarative_check import DeclarativeCheck
from avaguard_core.checks.base_check import CheckStatus, CISSeverity
from avaguard_core.errors import (
    ProviderAuthError,
    BenchmarkValidationError,
    EvidenceCollectionError,
    RemediationRenderError
)


# ==============================================================================
# Mock Provider Implementation for Testing
# ==============================================================================

class MockTestProvider(CloudProvider):
    """Deterministic Mock Provider for testing Dynamic Registries and Scan Queries."""

    def __init__(self, provider_id=None):
        super().__init__(provider_id)
        self.initialized_with = None
        self.mock_resources = {}

    def get_capabilities(self) -> ProviderCapabilities:
        return ProviderCapabilities(
            name="mock_test",
            display_name="Mock Test Provider",
            supported_services=["users", "buckets"],
            supported_remediations=["azure_cli", "powershell"],
            authentication_modes=["client_secret"],
            supported_benchmarks=["cis_mock_v1"]
        )

    def initialize(self, credentials: dict) -> None:
        if "secret" not in credentials:
            raise ProviderAuthError("Missing authentication secret key")
        self.initialized_with = credentials

    def query_resources(self, resource_type: str, fields=None) -> QueryResponse:
        resources = self.mock_resources.get(resource_type, [])
        return QueryResponse(
            provider_name="mock_test",
            resource_type=resource_type,
            resources=resources,
            query_timestamp=datetime.now()
        )

    def is_healthy(self) -> bool:
        return True


# ==============================================================================
# Unit & Integration Test Suite
# ==============================================================================

def test_provider_registration_and_capabilities():
    """Verify that ProviderRegistry dynamic loader works and discovers capabilities."""
    ProviderRegistry.register_provider("mock_test", MockTestProvider)
    
    # 1. Verification of class registry
    registered = ProviderRegistry.get_registered_providers()
    assert "mock_test" in registered

    # 2. Dynamic Capability discovery
    caps = ProviderRegistry.get_capabilities()
    assert "mock_test" in caps
    assert caps["mock_test"].display_name == "Mock Test Provider"
    assert "users" in caps["mock_test"].supported_services


def test_provider_session_registration():
    """Verify active authenticated provider instances can be cached/retrieved."""
    provider_instance = MockTestProvider()
    ProviderRegistry.register_active_instance("mock_test", provider_instance)

    active = ProviderRegistry.get_active_instance("mock_test")
    assert active is provider_instance

    # Tear down
    ProviderRegistry.clear_active_instances()
    assert ProviderRegistry.get_active_instance("mock_test") is None


def test_declarative_benchmark_schema_validation():
    """Verify that ControlDefinition Pydantic model correctly validates valid and invalid JSON schemas."""
    valid_json = {
        "control_id": "1.1",
        "title": "Enforce MFA for admins",
        "version": "1.0.0",
        "provider_compatibility": ["azure"],
        "category": "Identity",
        "scan_query": {
            "resource_type": "users",
            "fields": ["id", "mfa_enabled"]
        },
        "evaluation_rules": [
            {
                "field": "mfa_enabled",
                "operator": "equals",
                "expected": True
            }
        ],
        "remediation_metadata": {
            "severity": "HIGH",
            "impact_statement": "MFA prevents credential hacking.",
            "validation_steps": "Check settings.",
            "templates": {
                "azure_cli": "az ad user update --id {{ resource.id }} --mfa true"
            }
        }
    }

    # Should validate and load successfully
    loader = BenchmarkLoader("Test Benchmark", "1.0", "azure")
    control = loader.load_control_from_json_string(json.dumps(valid_json))
    assert control.control_id == "1.1"
    assert control.scan_query.resource_type == "users"
    assert control.remediation_metadata.severity == "HIGH"

    # Malformed fields should fail validation
    invalid_json = valid_json.copy()
    invalid_json["evaluation_rules"] = "must be a list of dicts, not string"

    with pytest.raises(BenchmarkValidationError):
        loader.load_control_from_json_string(json.dumps(invalid_json))


def test_benchmark_loader_differential_updates_and_overrides():
    """Verify that BenchmarkLoader supports dynamic updates, deprecations, and severity overrides."""
    loader = BenchmarkLoader("Test Benchmark", "1.0", "azure")
    
    control_a = ControlDefinition(
        control_id="1.1",
        title="Check A",
        version="1.0.0",
        provider_compatibility=["azure"],
        category="Identity",
        scan_query={"resource_type": "users"},
        evaluation_rules=[{"field": "x", "operator": "equals", "expected": True}],
        remediation_metadata={"severity": "MEDIUM", "impact_statement": "x", "validation_steps": "x"}
    )
    
    # 1. Initial Load
    loader.update_control(control_a)
    assert "1.1" in loader.benchmark.controls
    assert loader.benchmark.controls["1.1"].version == "1.0.0"

    # 2. Differential Update (version upgrade)
    control_a_updated = control_a.copy(update={"version": "1.1.0"})
    loader.update_control(control_a_updated)
    assert loader.benchmark.controls["1.1"].version == "1.1.0"

    # 3. Control Deprecation
    loader.deprecate_control("1.1")
    assert loader.benchmark.controls["1.1"].deprecated is True

    # 4. Apply organization-specific severity overrides
    overrides = {
        "controls": {
            "1.1": {
                "reremediation_metadata": {
                    "severity": "CRITICAL"
                }
            }
        }
    }
    loader.apply_overrides(overrides)
    assert loader.benchmark.controls["1.1"].remediation_metadata.severity == "CRITICAL"


def test_remediation_engine_jinja_rendering():
    """Verify that Jinja2 templates render resources dynamically."""
    metadata = {
        "severity": "HIGH",
        "impact_statement": "Credential risk.",
        "validation_steps": "Check query.",
        "templates": {
            "azure_cli": "az ad user update --id {{ resource.id }} --mfa true",
            "powershell": "Set-MsolUser -UPN {{ resource.upn }}"
        }
    }
    
    loader = BenchmarkLoader("Test", "1.0", "azure")
    control = loader.load_control_from_json_string(json.dumps({
        "control_id": "1.1",
        "title": "MFA Check",
        "version": "1.0",
        "provider_compatibility": ["azure"],
        "category": "Identity",
        "scan_query": {"resource_type": "users"},
        "evaluation_rules": [],
        "remediation_metadata": metadata
    }))

    non_compliant = [
        {"id": "user-001", "upn": "tony@acme.com"},
        {"id": "user-002", "upn": "pepper@acme.com"}
    ]

    # Act
    output = RemediationEngine.render(control.remediation_metadata, non_compliant)

    # Asserts
    assert "### [Severity: HIGH] Impact Assessment" in output
    assert "az ad user update --id user-001 --mfa true" in output
    assert "az ad user update --id user-002 --mfa true" in output
    assert "Set-MsolUser -UPN pepper@acme.com" in output


def test_declarative_evaluator_scan_execution():
    """Verify that DeclarativeCheck executes scan assertions and outputs correct compliance CheckResult."""
    # Define declarative check
    control_json = {
        "control_id": "1.2",
        "title": "Check User Admin Password Age",
        "version": "1.0.0",
        "provider_compatibility": ["mock_test"],
        "category": "Password Policy",
        "scan_query": {
            "resource_type": "users"
        },
        "evaluation_rules": [
            {
                "field": "password_age_days",
                "operator": "greater_than",
                "expected": 90
            }
        ],
        "remediation_metadata": {
            "severity": "MEDIUM",
            "impact_statement": "Old password risk.",
            "validation_steps": "Query age.",
            "templates": {
                "azure_cli": "az password reset --id {{ resource.id }}"
            }
        }
    }

    loader = BenchmarkLoader("Test", "1.0", "mock_test")
    control = loader.load_control_from_json_string(json.dumps(control_json))

    # Initialize Mock Provider and data
    provider = MockTestProvider()
    provider.mock_resources["users"] = [
        {"id": "user-01", "password_age_days": 120}, # Non-compliant (> 90 expected, wait! wait! wait!)
        # Ah, rule says: password_age_days > 90, so resource with age 120 passes, and resource with 45 fails!
        # Let's check rule logic: is_compliant if operator is met.
        # If password_age_days operator is greater_than 90, then 120 passes (compliant) and 45 fails (non-compliant).
        {"id": "user-02", "password_age_days": 45}   # Non-compliant (< 90)
    ]

    ProviderRegistry.register_active_instance("mock_test", provider)

    # Act
    check = DeclarativeCheck(control)
    result = check.execute()

    # Asserts
    assert result.status == CheckStatus.FAIL  # because user-02 failed
    assert result.total_count == 2
    assert result.compliant_count == 1
    assert result.non_compliant_count == 1
    assert result.non_compliant_resources[0]["id"] == "user-02"
    assert "az password reset --id user-02" in result.remediation

    # Tear down
    ProviderRegistry.clear_active_instances()


def test_declarative_evaluator_empty_resources_skipped():
    """Verify that DeclarativeCheck returns SKIPPED status when zero resources are evaluated."""
    control_json = {
        "control_id": "1.3",
        "title": "Check Empty Resources",
        "version": "1.0.0",
        "provider_compatibility": ["mock_test"],
        "category": "Test Policy",
        "scan_query": {
            "resource_type": "buckets"
        },
        "evaluation_rules": [
            {
                "field": "encrypted",
                "operator": "equals",
                "expected": True
            }
        ],
        "remediation_metadata": {
            "severity": "HIGH",
            "impact_statement": "Empty resource risk.",
            "validation_steps": "Query list.",
            "templates": {}
        }
    }

    loader = BenchmarkLoader("Test", "1.0", "mock_test")
    control = loader.load_control_from_json_string(json.dumps(control_json))

    # Initialize Mock Provider with empty resources list
    provider = MockTestProvider()
    provider.mock_resources["buckets"] = []  # Empty resource collection

    ProviderRegistry.register_active_instance("mock_test", provider)

    # Act
    check = DeclarativeCheck(control)
    result = check.execute()

    # Asserts
    assert result.status == CheckStatus.SKIPPED
    assert result.total_count == 0
    assert result.compliant_count == 0
    assert result.non_compliant_count == 0
    assert "Evaluated 0 resources" in result.details

    # Tear down
    ProviderRegistry.clear_active_instances()


def test_risk_scorer_excludes_skipped_checks():
    """Verify that RiskScorer excludes SKIPPED checks from scoring numerator and denominator."""
    from avaguard_core.risk_scorer import RiskScorer
    from avaguard_core.checks.base_check import CheckResult

    # Construct mock CheckResult objects
    # Skipped check (Medium severity - weight 4.0). Should be ignored completely.
    skipped_res = CheckResult(
        check_id="check_skipped",
        status=CheckStatus.SKIPPED,
        cis_severity=CISSeverity.MEDIUM
    )
    # Passed check (High severity - weight 7.0). Earns 7.0.
    passed_res = CheckResult(
        check_id="check_passed",
        status=CheckStatus.PASS,
        cis_severity=CISSeverity.HIGH
    )
    # Failed check (Low severity - weight 1.0). Earns 0.0.
    failed_res = CheckResult(
        check_id="check_failed",
        status=CheckStatus.FAIL,
        cis_severity=CISSeverity.LOW
    )

    results = [skipped_res, passed_res, failed_res]

    # Act
    score = RiskScorer.calculate_score(results)
    metrics = RiskScorer.calculate_metrics(results)

    # Asserts
    # Expected: (Passed weight) / (Passed weight + Failed weight) = 7.0 / (7.0 + 1.0) = 87.5%
    assert score == 87.5
    assert metrics["overall_score"] == 87.5
    assert metrics["passed"] == 1
    assert metrics["failed"] == 1
    assert metrics["skipped"] == 1
    assert metrics["errors"] == 0
    assert metrics["total"] == 3
