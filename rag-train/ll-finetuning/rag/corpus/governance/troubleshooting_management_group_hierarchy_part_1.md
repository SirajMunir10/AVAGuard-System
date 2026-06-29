# Troubleshooting: Management Group Hierarchy (AuthorizationFailed)

**Domain:** Governance
**Subdomain:** Management Group Hierarchy
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports they cannot create a new Azure subscription under a specific management group. The error message indicates insufficient permissions, but the user has the Owner role at the root management group. What is the likely root cause and how do you resolve it?

## Environment Context
- **Tenant Type:** Enterprise (EA or MCA)
- **Configuration:** Management group hierarchy with root management group containing child management groups; the user is assigned the Owner role at the root management group scope.

## Symptoms
- User receives an error when attempting to create a new subscription under a specific management group.
- Error message: 'The user does not have permissions to create a subscription under this management group.'
- User has the Owner role at the root management group scope.

## Error Codes
- `AuthorizationFailed`

## Root Causes
1. The user does not have the required permission 'Microsoft.Subscription/createSubscription/action' at the target management group scope. The Owner role at the root management group does not automatically grant subscription creation permissions at child management groups because subscription creation is a specific action that must be assigned at the scope where the subscription will be created.

## Remediation Steps
1. Assign the user the 'Subscription Creator' role (or a custom role containing 'Microsoft.Subscription/createSubscription/action') at the specific management group where the subscription should be created. This can be done via Azure portal, Azure CLI, or PowerShell.
2. Alternatively, assign the user the Owner role at the target management group scope (not just the root).
3. Verify the assignment by using Azure CLI: 'az role assignment list --scope /providers/Microsoft.Management/managementGroups/{targetMGId}'

## Validation
After the role assignment, the user should be able to create a subscription under the target management group. Use 'az account create' or the Azure portal to confirm.

## Rollback
Remove the role assignment at the target management group scope if the user should not have permanent subscription creation permissions. Use 'az role assignment delete' with the appropriate parameters.

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal#troubleshoot-subscription-creation-permissions>
- <https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#subscription-creator>
