"""
AVAGuard Core — Benchmark Declarative Schema Models

Uses Pydantic to enforce strong typing, validation boundaries, and versioned
schemas for declarative compliance checks and multi-framework mappings.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class ScanQuerySpec(BaseModel):
    """Specifies the target resource type and fields to query from the provider."""
    resource_type: str = Field(description="Target provider resource type (e.g. 'users', 's3_buckets')")
    fields: Optional[List[str]] = Field(default=None, description="Specific attributes to request (optional)")


class EvaluationRuleSpec(BaseModel):
    """Specifies a deterministic condition to evaluate against query results."""
    field: str = Field(description="Resource property to inspect")
    operator: str = Field(
        description="Condition operator: 'equals', 'contains', 'in', 'greater_than', 'regex', 'not_equals'"
    )
    expected: Any = Field(description="Expected value to match or compare")
    remedy_on_fail: bool = Field(
        default=True, 
        description="Whether resource failure triggers remediation requirements"
    )


class RemediationTemplatesSpec(BaseModel):
    """Versioned code templates for diverse target environments."""
    azure_cli: Optional[str] = Field(default=None, description="Azure CLI remedy template")
    powershell: Optional[str] = Field(default=None, description="PowerShell remedy template")
    terraform: Optional[str] = Field(default=None, description="Terraform infrastructure remedy template")


class RemediationMetadataSpec(BaseModel):
    """Enterprise-ready structured remediation info."""
    severity: str = Field(description="Standard risk severity: CRITICAL, HIGH, MEDIUM, LOW")
    impact_statement: str = Field(description="Explanation of the risk and vulnerability impact")
    validation_steps: str = Field(description="Steps or queries to verify the fix succeeded")
    templates: RemediationTemplatesSpec = Field(default_factory=RemediationTemplatesSpec)


class ControlDefinition(BaseModel):
    """
    Standard declarative specification schema for a single benchmark control.
    Maps directly to schema-validated JSON configurations.
    """
    control_id: str = Field(description="CIS or framework ID (e.g., '1.1')")
    title: str = Field(description="Vulnerability description or control title")
    version: str = Field(description="Semantic version of this control specification")
    deprecated: bool = Field(default=False, description="True if control was superseded in newer benchmarks")
    profile_level: str = Field(default="Level 1", description="CIS profile tier (Level 1, Level 2)")
    provider_compatibility: List[str] = Field(description="Compatible providers (e.g. ['azure'])")
    category: str = Field(description="Security area classification (e.g. 'Identity Management')")
    
    # Standard compliance framework mappings (NIST, ISO, SOC2)
    framework_mappings: Dict[str, List[str]] = Field(
        default_factory=dict, 
        description="Compliance controls mapping (e.g., {'SOC2_TSC': ['CC6.1']})"
    )
    
    scan_query: ScanQuerySpec = Field(description="Data collection specs")
    evaluation_rules: List[EvaluationRuleSpec] = Field(description="List of validation assertions")
    remediation_metadata: RemediationMetadataSpec = Field(description="Structured remediation metrics")


class BenchmarkVersion(BaseModel):
    """
    Versioned benchmark catalog containing mapped controls.
    Enables versioning and differential update pipelines.
    """
    title: str = Field(description="Benchmark name (e.g. 'CIS Microsoft Azure Foundations Benchmark')")
    version: str = Field(description="Semantic version reference (e.g. '4.0.0')")
    provider: str = Field(description="Target platform provider (e.g. 'azure')")
    controls: Dict[str, ControlDefinition] = Field(
        default_factory=dict, 
        description="Active control catalog mapped by control_id"
    )
