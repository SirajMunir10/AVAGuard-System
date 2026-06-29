# Governance: Management Group Hierarchy

**Domain:** Governance
**Subdomain:** Management Group Hierarchy
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that a new Azure subscription was created outside the intended management group hierarchy, bypassing governance policies. How can this be detected and prevented?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Management group hierarchy with root management group containing all subscriptions; Azure Policy assigned at root to enforce governance.

## Symptoms
- Subscription appears in the root management group instead of a designated child management group
- Azure Policy compliance reports show the subscription as non-compliant with management group assignment policies
- Audit logs show subscription creation by a user without proper management group permissions

## Error Codes
N/A

## Root Causes
1. User creating the subscription had insufficient permissions to place it in the correct management group
2. No Azure Policy or RBAC restriction enforces that new subscriptions must be created under a specific management group

## Remediation Steps
1. Move the subscription to the correct management group using the Azure portal or PowerShell: `Move-AzManagementGroupSubscription -GroupId '<target-group>' -SubscriptionId '<subscription-id>'`
2. Assign an Azure Policy at the root management group to deny creation of subscriptions outside the intended hierarchy (e.g., policy definition 'Allowed locations for management groups')
3. Configure RBAC so that only authorized users (e.g., Subscription Creator role) can create subscriptions, and require them to specify the parent management group

## Validation
Verify the subscription appears in the correct management group and that the Azure Policy assignment shows compliance for new subscriptions.

## Rollback
If the move was incorrect, move the subscription back to its original management group using the same PowerShell command with the original group ID.

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/overview>
- <https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#subscription-creator>
