# Troubleshooting: Azure Policy

**Domain:** Governance
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that Azure Policy assignments are not being enforced on a newly created subscription. How do you troubleshoot why policies are not applying?

## Environment Context
- **Tenant Type:** Enterprise (multiple subscriptions under a management group)
- **Configuration:** Azure Policy assigned at management group scope; subscription was created under that management group.

## Symptoms
- New subscription does not show any policy compliance data in Azure Policy
- Resources created in the subscription are not blocked or audited as expected
- Policy assignment appears in the management group but not in the subscription's compliance view

## Error Codes
N/A

## Root Causes
1. Policy assignment was not inherited because the subscription was created after the policy assignment and the assignment's 'excludedSubscriptions' or 'notScopes' property inadvertently excludes the new subscription
2. The subscription is not a direct child of the management group where the policy is assigned (e.g., it was moved or created under a different hierarchy)
3. The policy assignment's 'enforcementMode' is set to 'DoNotEnforce'

## Remediation Steps
1. Verify the subscription is in the correct management group hierarchy using Azure Portal or the Azure CLI command: `az account management-group list --subscription <subscription-id>`
2. Check the policy assignment's scope and exclusions in the Azure Portal under 'Policy > Assignments' or via PowerShell: `Get-AzPolicyAssignment -Scope '/providers/Microsoft.Management/managementGroups/<MG-id>'`
3. If the assignment has 'enforcementMode' set to 'DoNotEnforce', change it to 'Default' using: `Update-AzPolicyAssignment -Name <assignment-name> -Scope <scope> -EnforcementMode Default`
4. If the subscription was excluded, remove the exclusion by updating the assignment's 'notScopes' property
5. Wait up to 30 minutes for policy evaluation to propagate, or trigger an on-demand evaluation scan using: `Start-AzPolicyComplianceScan -ResourceGroupName <rg-name>`

## Validation
After remediation, create a test resource that should be denied or audited by the policy and verify the compliance state updates in Azure Policy within 30 minutes.

## Rollback
Reapply the original exclusion or set 'enforcementMode' back to 'DoNotEnforce' if the change was incorrect.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
