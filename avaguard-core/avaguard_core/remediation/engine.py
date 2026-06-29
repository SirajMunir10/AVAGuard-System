"""
AVAGuard Core — Enterprise Remediation Engine

Renders structured remediation commands (Azure CLI, PowerShell, Terraform)
dynamically utilizing Jinja2 templates and active scan finding details.
"""

import logging
from typing import List, Dict, Any
from jinja2 import Template
from avaguard_core.benchmarks.models import RemediationMetadataSpec
from avaguard_core.errors import RemediationRenderError

logger = logging.getLogger(__name__)


class RemediationEngine:
    """
    Renders structured, evidence-aware remediation instructions for security engineers.
    Converts generic templates to precise CLI, PowerShell, and Terraform blocks.
    """

    @staticmethod
    def render(metadata: RemediationMetadataSpec, non_compliant_resources: List[Dict[str, Any]]) -> str:
        """
        Render dynamic, resource-specific remediation guides.

        Args:
            metadata: Structured remediation templates and impact statement.
            non_compliant_resources: List of resources failing validation.

        Returns:
            A formatted, human-readable instructions block detailing:
            - Impact
            - Rendered remediations (CLI, PowerShell, Terraform)
            - Validation checks
        """
        if not non_compliant_resources:
            return "No non-compliant resources found. No remediation required."

        # Renders each template
        rendered_cli = []
        rendered_powershell = []
        rendered_terraform = []

        try:
            # Render CLI
            if metadata.templates.azure_cli:
                template = Template(metadata.templates.azure_cli)
                for resource in non_compliant_resources:
                    rendered_cli.append(template.render(resource=resource))

            # Render PowerShell
            if metadata.templates.powershell:
                template = Template(metadata.templates.powershell)
                for resource in non_compliant_resources:
                    rendered_powershell.append(template.render(resource=resource))

            # Render Terraform
            if metadata.templates.terraform:
                template = Template(metadata.templates.terraform)
                # Usually Terraform is rendered for the resource list overall, but we support both
                for resource in non_compliant_resources:
                    rendered_terraform.append(template.render(resource=resource))

        except Exception as e:
            logger.error(f"Failed to render remediation templates: {e}")
            raise RemediationRenderError(f"Remediation template syntax error: {e}")

        # Build clean audit evidence and reporting blocks
        output = [
            f"### [Severity: {metadata.severity}] Impact Assessment",
            metadata.impact_statement,
            "",
            "### Remediation Instructions",
        ]

        if rendered_cli:
            output.append("#### Azure CLI Remediation")
            output.append("```bash")
            output.extend(rendered_cli)
            output.append("```")
            output.append("")

        if rendered_powershell:
            output.append("#### PowerShell Remediation")
            output.append("```powershell")
            output.extend(rendered_powershell)
            output.append("```")
            output.append("")

        if rendered_terraform:
            output.append("#### Terraform Remediation Overrides")
            output.append("```hcl")
            output.extend(rendered_terraform)
            output.append("```")
            output.append("")

        output.append("### Verification & Validation Steps")
        output.append(metadata.validation_steps)

        return "\n".join(output)
