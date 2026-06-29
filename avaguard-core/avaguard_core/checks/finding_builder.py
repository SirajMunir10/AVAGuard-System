from typing import Dict, Any, List, Optional
from datetime import datetime

from .base_check import CheckResult, CheckStatus, CISSeverity


class FindingBuilder:
    """
    Fluent builder for constructing enterprise-grade compliance findings.
    Enforces the ASFF/SARIF data contract and strictly decouples data collection
    from presentation formatting.
    """

    def __init__(self, check_instance):
        self.check = check_instance
        self.result = CheckResult(
            check_id=self.check.CHECK_ID,
            title=self.check.TITLE,
            scan_id=self.check.config.get('scan_id'),
            cis_control_id=self.check.CIS_CONTROL_ID,
            category=self.check.CATEGORY,
            cis_severity=self.check.CIS_SEVERITY,
            priority=self.check.PRIORITY,
            initiated_by=self.check.config.get('initiated_by'),
            target_tenant=self.check.config.get('tenant_id'),
            requires_premium=self.check.REQUIRES_PREMIUM,
            api_permissions_required=self.check.API_PERMISSIONS_REQUIRED,
            
            # Context initialization
            description=self.check.DESCRIPTION,
            
            # Dictionary/List initializations
            metadata={},
            evidence={},
            non_compliant_resources=[],
            compliant_resources=[],
            warning_resources=[]
        )
        
        # Override fields for the new Data Contract
        self._finding_severity = self.check.CIS_SEVERITY.value
        self._why_it_matters = ""
        self._evidence_summary = ""
        self._raw_output = {}
        self._recommended_action = ""
        self._remediation_steps = []
        self._references = []

    def set_status(self, status: CheckStatus) -> 'FindingBuilder':
        """Set the overall pass/fail status."""
        self.result.status = status
        return self

    def set_severity(self, finding_severity: str) -> 'FindingBuilder':
        """Dynamically override the severity based on the actual finding risk."""
        self._finding_severity = finding_severity
        return self

    def set_counts(self, total: int, compliant: int = 0, non_compliant: int = 0, warning: int = 0) -> 'FindingBuilder':
        """Set numeric evaluation counts."""
        self.result.total_count = total
        self.result.compliant_count = compliant
        self.result.non_compliant_count = non_compliant
        self.result.warning_count = warning
        return self

    def set_context(self, why_it_matters: str, description: Optional[str] = None) -> 'FindingBuilder':
        """Set narrative context for AI and reporting."""
        self._why_it_matters = why_it_matters
        if description:
            self.result.description = description
        return self

    def set_evidence(self, summary: str, resources: List[Dict[str, Any]] = None, raw_output: Dict[str, Any] = None) -> 'FindingBuilder':
        """Set the technical evidence supporting the finding."""
        self._evidence_summary = summary
        if resources:
            self.result.non_compliant_resources = resources
        if raw_output:
            self._raw_output = raw_output
        return self

    def set_remediation(self, action: str, steps: List[str] = None, references: List[str] = None) -> 'FindingBuilder':
        """Set explicit remediation guidance."""
        self._recommended_action = action
        if steps:
            self._remediation_steps = steps
        if references:
            self._references = references
        return self

    def set_error(self, message: str, traceback: str = None) -> 'FindingBuilder':
        """Set error metadata if the check crashed."""
        self.result.status = CheckStatus.ERROR
        self.result.error_message = message
        self.result.error_traceback = traceback
        return self

    def build(self) -> CheckResult:
        """Validate and finalize the finding against the Data Contract."""
        # 1. Validation Layer
        if not self.result.status:
            raise ValueError(f"Finding for {self.check.CHECK_ID} must explicitly set a CheckStatus.")
            
        # 2. Logic Overrides
        if self.result.status == CheckStatus.PASS:
            self._finding_severity = "INFO"
            
        # 3. Assemble the ASFF/SARIF Contract structure inside the result
        self.result.metadata.update({
            "finding_type": "compliance_misconfiguration",
            "source_engine": "avaguard-cis-engine",
            "finding_severity": self._finding_severity,
            "scanner_version": "1.2.0",
            
            "context": {
                "description": self.result.description,
                "why_it_matters": self._why_it_matters
            },
            
            "technical_evidence": {
                "evidence_summary": self._evidence_summary,
                "raw_output": self._raw_output,
            },
            
            "remediation": {
                "recommended_action": self._recommended_action,
                "implementation_steps": self._remediation_steps,
                "references": self._references
            }
        })
        
        # Construct result.details for compatibility with tests and legacy views
        details_parts = []
        if self.result.description:
            details_parts.append(f"Description:\n{self.result.description}")
        if self._why_it_matters:
            details_parts.append(f"Why it Matters:\n{self._why_it_matters}")
        if self._evidence_summary:
            details_parts.append(f"Evidence:\n{self._evidence_summary}")
        if self._recommended_action:
            details_parts.append(f"Recommendations:\n{self._recommended_action}")
            if self._remediation_steps:
                steps_str = "\n".join(f"  • {step}" for step in self._remediation_steps)
                details_parts.append(f"Remediation Steps:\n{steps_str}")
        self.result.details = "\n\n".join(details_parts)
        
        # Ensure API Calls and Duration are captured
        self.result.api_calls_count = getattr(self.check, '_api_calls', 0)
        if hasattr(self.check, '_start_time') and self.check._start_time:
            self.result.duration_seconds = (datetime.now() - self.check._start_time).total_seconds()
            
        return self.result
