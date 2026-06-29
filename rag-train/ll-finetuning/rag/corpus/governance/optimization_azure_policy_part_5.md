# Optimization: Azure Policy (ManagedIdentityMissing)

**Domain:** Governance
**Subdomain:** Azure Policy
**Incident Type:** Optimization

## Scenario / Query
How can I identify and remediate Azure Policy assignments that are not being evaluated due to a missing or misconfigured managed identity?

## Environment Context
- **Tenant Type:** Enterprise (multiple subscriptions)
- **Configuration:** Azure Policy assignments with 'deployIfNotExists' or 'modify' effects require a system-assigned managed identity to be enabled on the assignment scope.

## Symptoms
- Policy compliance dashboard shows 'Not started' or 'Conflict' for certain assignments
- Remediation tasks fail with 'ManagedIdentityMissing' or 'NoManagedIdentity' error
- Activity log shows 'PolicyEvaluationFailure' with reason 'Managed identity not found'

## Error Codes
- `ManagedIdentityMissing`
- `NoManagedIdentity`
- `PolicyEvaluationFailure`

## Root Causes
1. The system-assigned managed identity was not enabled when the policy assignment was created
2. The managed identity was deleted or disabled after assignment creation
3. The policy assignment was created using an older API version that did not automatically create the identity

## Remediation Steps
1. 1. Identify affected policy assignments using Azure Policy Insights or the Azure Resource Graph query: 'policyresources | where type == 'microsoft.authorization/policyassignments' | where properties.identity == null'
2. 2. For each affected assignment, update the assignment to enable a system-assigned managed identity using Azure PowerShell: 'Set-AzPolicyAssignment -Id <assignmentId> -IdentityType SystemAssigned'
3. 3. Grant the managed identity the necessary permissions (e.g., 'Contributor' or a custom role) on the target resource scope as documented in the policy definition
4. 4. Trigger a manual remediation scan or wait for the next evaluation cycle

## Validation
Run 'Get-AzPolicyAssignment -Id <assignmentId> | Select-Object -ExpandProperty Identity' and verify that 'PrincipalId' is populated. Then check the policy compliance dashboard to confirm 'Compliant' or 'Non-compliant' status.

## Rollback
To revert, set the identity type to 'None' using 'Set-AzPolicyAssignment -Id <assignmentId> -IdentityType None' and remove any role assignments granted to the managed identity.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources#configure-the-managed-identity>
