# Optimization: Azure Policy

**Domain:** Governance
**Subdomain:** Azure Policy
**Incident Type:** Optimization

## Scenario / Query
An organization has deployed Azure Policy at scale but notices that many non-compliant resources are not being automatically remediated. How can they optimize policy assignment to enable automatic remediation for all applicable policies?

## Environment Context
- **Tenant Type:** Enterprise (multiple subscriptions)
- **Configuration:** Azure Policy assignments with 'enforce' mode but without 'remediation' task configured

## Symptoms
- Resources are flagged as non-compliant in Azure Policy compliance view
- No remediation tasks are created for non-compliant resources
- Manual remediation is required for each non-compliant resource

## Error Codes
N/A

## Root Causes
1. Policy assignments do not have the 'remediation' property configured
2. Managed identity required for remediation tasks is not assigned or lacks permissions

## Remediation Steps
1. For each policy assignment that supports remediation (deployIfNotExists or modify effect), create a remediation task using the Azure portal, Azure PowerShell, or Azure CLI
2. Assign a system-assigned or user-assigned managed identity to the policy assignment with the necessary permissions (e.g., Contributor role on the target scope)
3. Run the remediation task to bring non-compliant resources into compliance

## Validation
After remediation tasks complete, verify that the compliance state of previously non-compliant resources changes to 'Compliant' in the Azure Policy compliance dashboard.

## Rollback
Delete the remediation task from the policy assignment. Resources will remain in their current state; no automatic rollback is provided by Azure Policy.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources>
