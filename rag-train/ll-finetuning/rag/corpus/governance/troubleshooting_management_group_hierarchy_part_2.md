# Troubleshooting: Management Group Hierarchy (AuthorizationFailed)

**Domain:** Governance
**Subdomain:** Management Group Hierarchy
**Incident Type:** Troubleshooting

## Scenario / Query
A security admin cannot move a subscription from one management group to another and receives an error about insufficient permissions even though they are assigned the Owner role at the root management group. What is the likely cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Enterprise (multiple management groups)
- **Configuration:** The subscription is currently in a management group that is a child of the root management group. The admin has the Owner role on the root management group but the move operation fails.

## Symptoms
- Move subscription operation fails with a permissions error
- Admin has Owner role at root management group scope
- No other custom role assignments blocking the move

## Error Codes
- `AuthorizationFailed`

## Root Causes
1. The admin does not have the Microsoft.Management/managementGroups/subscriptions/write permission on the source management group. The Owner role at the root management group does not automatically grant this permission on child management groups because the move operation requires write permission on the source management group, not just the root.

## Remediation Steps
1. Assign the 'Management Group Contributor' role to the admin on the source management group (or at the root management group if the admin needs to move subscriptions from any child group). This role includes the Microsoft.Management/managementGroups/subscriptions/write permission required for the move operation.
2. Alternatively, assign a custom role that includes the Microsoft.Management/managementGroups/subscriptions/write action at the source management group scope.

## Validation
After the role assignment, attempt to move the subscription again using the Azure portal, PowerShell (Move-AzManagementGroupSubscription), or Azure CLI (az account management-group subscription add). The operation should succeed.

## Rollback
Remove the 'Management Group Contributor' role assignment from the admin if it was granted only for this purpose and is no longer needed.

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/troubleshoot#error-when-moving-a-subscription>
