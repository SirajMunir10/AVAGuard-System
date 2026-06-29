# Implementation: Management Group Hierarchy (Conflict)

**Domain:** Governance
**Subdomain:** Management Group Hierarchy
**Incident Type:** Implementation

## Scenario / Query
An organization attempts to move a subscription from one management group to another but receives an error stating the operation is not allowed. What configuration or permission issue could prevent the move, and how should it be resolved?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with multiple management groups)
- **Configuration:** Management group hierarchy with inherited Azure Policy assignments that enforce resource location restrictions

## Symptoms
- Subscription move operation fails in Azure Portal or via PowerShell
- Error message indicates the move is blocked by policy or permissions

## Error Codes
- `Conflict`
- `Forbidden`

## Root Causes
1. The target management group has an Azure Policy assignment (e.g., allowed locations) that conflicts with resources already in the subscription
2. The user performing the move does not have Microsoft.Management/managementGroups/subscriptions/write permission on both source and target management groups

## Remediation Steps
1. Ensure the user has the Contributor role (or equivalent) on both the source and target management groups, or assign the Management Group Contributor role
2. Remove or modify conflicting Azure Policy assignments on the target management group before moving the subscription
3. Alternatively, remove the conflicting resources from the subscription or change the policy scope to exclude the subscription after the move

## Validation
After resolving permissions and policy conflicts, retry the subscription move using Azure Portal, PowerShell (Move-AzManagementGroupSubscription), or Azure CLI (az account management-group subscription add).

## Rollback
If the move succeeds but causes unintended policy violations, move the subscription back to its original management group using the same move operation with the original source as the new target.

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/manage#move-subscriptions-between-management-groups>
