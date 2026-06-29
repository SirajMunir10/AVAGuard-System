"""
AVAGuard Core — Declarative Check Evaluator

A reusable engine class that executes compliance assertions defined in versioned
JSON specifications. Subclasses the standard `BaseCheck` for dynamic registration.
"""

import re
import datetime
import logging
from typing import List, Dict, Any, Optional

from avaguard_core.checks.base_check import BaseCheck, CheckResult, CheckStatus, CISSeverity
from avaguard_core.benchmarks.models import ControlDefinition
from avaguard_core.providers.registry import ProviderRegistry
from avaguard_core.remediation.engine import RemediationEngine
from avaguard_core.errors import EvidenceCollectionError

logger = logging.getLogger(__name__)


class DeclarativeCheck(BaseCheck):
    """
    Reusable scan execution class. Validates declarative benchmark rules
    against dynamic provider target responses and formats standardized CheckResult.
    """

    def __init__(self, control_def: ControlDefinition, graph_client=None, config: Optional[Dict] = None):
        """
        Initialize the check with a JSON control definition.
        
        Args:
            control_def: Validated ControlDefinition instance.
            graph_client: Legacy Graph Client (preserved for backward compatibility).
            config: Operational configuration dictionary.
        """
        super().__init__(graph_client, config)
        self.control_def = control_def
        self.CHECK_ID = control_def.control_id
        self.TITLE = control_def.title
        self.DESCRIPTION = control_def.category
        
        # Override class attributes matching BaseCheck schema
        self.CIS_CONTROL_ID = control_def.control_id
        self.CATEGORY = control_def.category
        self.REQUIRES_PREMIUM = False
        
        try:
            self.CIS_SEVERITY = CISSeverity[control_def.remediation_metadata.severity.upper()]
        except (KeyError, ValueError):
            self.CIS_SEVERITY = CISSeverity.MEDIUM
            
        self.PRIORITY = control_def.remediation_metadata.severity.title()

    def execute(self) -> CheckResult:
        """
        Execute the declarative validation flow.
        Queries active providers, evaluates assertions, and renders remediations.
        """
        provider_name = self.control_def.provider_compatibility[0] if self.control_def.provider_compatibility else "azure"
        
        # 1. Resolve Provider Session
        provider = ProviderRegistry.get_active_instance(provider_name)
        
        if not provider:
            # Fallback promotion to dynamically wrap legacy graph_client into AzureProvider
            # This ensures 100% backward compatibility and upgrades legacy clients transparently
            if self.graph_client:
                from avaguard_core.providers.azure.provider import AzureProvider
                
                # Check client type to determine mock mode
                is_mock = self.graph_client.__class__.__name__ == "MockGraphAPIClient"
                
                provider = AzureProvider()
                provider.client = self.graph_client
                provider.use_mock = is_mock
                provider.tenant_id = self.config.get("tenant_id", "mock-tenant-id")
                
                # Sync active instance to registry for subsequent check lookups
                ProviderRegistry.register_active_instance(provider_name, provider)
        
        if not provider:
            raise EvidenceCollectionError(f"No active provider session or client available for '{provider_name}'")

        # 2. Query target resources
        query_spec = self.control_def.scan_query
        try:
            query_response = provider.query_resources(query_spec.resource_type, query_spec.fields)
        except Exception as e:
            logger.error(f"Provider query failed for resource '{query_spec.resource_type}': {e}")
            raise EvidenceCollectionError(f"Failed to query provider resources: {e}")

        # 3. Evaluate rules
        compliant_resources = []
        non_compliant_resources = []

        for resource in query_response.resources:
            is_compliant = True
            for rule in self.control_def.evaluation_rules:
                # Traverse nested dictionary objects (e.g. "properties.enabled")
                val = resource
                for part in rule.field.split('.'):
                    if isinstance(val, dict):
                        val = val.get(part)
                    else:
                        val = None
                        break

                op = rule.operator.lower().strip()
                expected = rule.expected

                if op == "equals":
                    rule_passed = (val == expected)
                elif op == "not_equals":
                    rule_passed = (val != expected)
                elif op == "contains":
                    rule_passed = (isinstance(val, (list, str)) and expected in val)
                elif op == "in":
                    rule_passed = (isinstance(expected, list) and val in expected)
                elif op == "greater_than":
                    try:
                        rule_passed = (float(val) > float(expected))
                    except (ValueError, TypeError):
                        rule_passed = False
                elif op == "regex":
                    try:
                        rule_passed = (val is not None and re.search(str(expected), str(val)) is not None)
                    except Exception:
                        rule_passed = False
                else:
                    rule_passed = False

                if not rule_passed:
                    is_compliant = False
                    break

            if is_compliant:
                compliant_resources.append(resource)
            else:
                non_compliant_resources.append(resource)

        # Map execution state to CheckStatus
        if len(query_response.resources) == 0:
            status = CheckStatus.SKIPPED
        elif non_compliant_resources:
            status = CheckStatus.FAIL
        else:
            status = CheckStatus.PASS

        # 4. Render structured, dynamic remediations
        try:
            rendered_remediation = RemediationEngine.render(
                self.control_def.remediation_metadata, 
                non_compliant_resources
            )
        except Exception as e:
            logger.warning(f"Remediation template rendering failed: {e}")
            rendered_remediation = self.control_def.remediation_metadata.impact_statement

        # Build CheckResult matching table schema and audit evidence needs
        return self.create_result(
            status=status,
            compliant_count=len(compliant_resources),
            non_compliant_count=len(non_compliant_resources),
            total_count=len(query_response.resources),
            details=f"Evaluated {len(query_response.resources)} resources. Compliant: {len(compliant_resources)}. Non-compliant: {len(non_compliant_resources)}.",
            non_compliant_resources=non_compliant_resources,
            compliant_resources=compliant_resources,
            evidence=query_response.evidence_snapshot or {"resources": query_response.resources},
            remediation=rendered_remediation
        )
