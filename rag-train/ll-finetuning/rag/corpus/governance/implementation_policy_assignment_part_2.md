# Implementation: Policy Assignment

**Domain:** Governance
**Subdomain:** Policy Assignment
**Incident Type:** Implementation

## Scenario / Query
After assigning an Azure Policy initiative to a management group, some resources in child subscriptions show as non-compliant even though they meet the policy conditions. What could cause this discrepancy and how can it be resolved?

## Environment Context
- **Tenant Type:** Enterprise (multiple subscriptions under a management group hierarchy)
- **Configuration:** Azure Policy initiative assigned at the management group scope with enforcement mode enabled

## Symptoms
- Policy compliance dashboard shows non-compliant resources that appear to satisfy the policy rules
- Azure Resource Graph queries return conflicting compliance states for the same resource
- No policy exemptions or exclusions are configured for the affected resources

## Error Codes
N/A

## Root Causes
1. Policy evaluation may not have completed for all child scopes after assignment; Azure Policy evaluation is asynchronous and can take up to 30 minutes to propagate
2. The policy initiative includes a policy definition with a scope condition that inadvertently excludes the child subscription or resource group
3. A newer version of the policy definition was published after the assignment, and the assignment still references the older version

## Remediation Steps
1. Wait at least 30 minutes after assignment and trigger an on-demand evaluation scan using: Start-AzPolicyComplianceScan -ResourceGroupName '<ResourceGroupName>' -AsJob (PowerShell) or az policy state trigger-scan (Azure CLI)
2. Verify the assignment scope includes all intended child scopes by reviewing the assignment properties in the Azure portal or using Get-AzPolicyAssignment -Name '<AssignmentName>' | Select-Object -ExpandProperty Properties
3. Check if the policy definition used in the initiative has been updated; if so, update the initiative to reference the latest definition version using Set-AzPolicySetDefinition -Name '<InitiativeName>' -PolicyDefinition '<UpdatedPolicyDefinition>'
4. Review the policy rule logic for any conditions that might exclude certain subscriptions (e.g., location conditions, tag conditions) and adjust the assignment or definition accordingly

## Validation
Run an on-demand compliance scan and confirm that the resources now show as compliant in the Azure Policy compliance dashboard. Use Azure Resource Graph to query policy state: policyResources | where properties.policyAssignmentId == '<AssignmentId>' and properties.complianceState == 'Compliant'

## Rollback
If the remediation steps cause unintended compliance changes, revert the policy assignment to the previous version by reassigning the original initiative with the earlier definition version, or remove the assignment entirely using Remove-AzPolicyAssignment -Name '<AssignmentName>'

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources>
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data#evaluation-triggers>
