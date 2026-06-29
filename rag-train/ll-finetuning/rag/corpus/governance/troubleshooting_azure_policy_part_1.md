# Troubleshooting: Azure Policy (Conflict (409))

**Domain:** Governance
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
Why is my Azure Policy assignment showing a 'Conflict' error when I try to assign a built-in policy definition to a management group?

## Environment Context
- **Tenant Type:** Enterprise (multiple management groups)
- **Configuration:** A custom initiative containing the same policy definition is already assigned at a parent management group scope.

## Symptoms
- Azure portal displays 'Conflict' when attempting to assign a built-in policy definition.
- PowerShell command New-AzPolicyAssignment returns error: 'Policy assignment conflict. The policy assignment cannot be created because it conflicts with an existing assignment.'

## Error Codes
- `Conflict (409)`

## Root Causes
1. A policy assignment with the same policy definition already exists at a parent or overlapping scope, causing a conflict per Azure Policy assignment rules.

## Remediation Steps
1. Identify the existing conflicting assignment using Get-AzPolicyAssignment | Where-Object {$_.Properties.PolicyDefinitionId -eq '<policyDefinitionId>'}.
2. Remove the conflicting assignment using Remove-AzPolicyAssignment -Name '<assignmentName>' -Scope '<scope>'.
3. Alternatively, modify the scope of the new assignment to avoid overlap, or update the existing assignment instead of creating a duplicate.

## Validation
Run Get-AzPolicyAssignment -Scope '<targetScope>' and confirm only one assignment exists for the policy definition.

## Rollback
Re-create the removed assignment using New-AzPolicyAssignment with the original parameters.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general#scenario-1---policy-assignment-conflict>
