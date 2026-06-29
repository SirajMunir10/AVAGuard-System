# Governance: Management Groups

**Domain:** Governance
**Subdomain:** Management Groups
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that a new Azure subscription was created outside the intended management group hierarchy, bypassing governance policies. How can the administrator detect and remediate this misconfiguration?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure management group hierarchy with root management group containing all subscriptions

## Symptoms
- Subscription appears under the root management group instead of the designated child management group
- Azure Policy assignments targeting the intended child management group do not apply to the subscription
- Subscription creation audit logs show no explicit assignment to a management group

## Error Codes
N/A

## Root Causes
1. Subscription was created with default placement at the root management group because no explicit management group was specified during creation
2. Lack of Azure Policy or RBAC controls to enforce subscription placement

## Remediation Steps
1. Move the subscription to the correct management group using the Azure portal, PowerShell (Move-AzManagementGroupSubscription), or Azure CLI (az account management-group subscription add)
2. Create an Azure Policy definition with effect 'deny' to prevent subscriptions from being placed outside the intended management group hierarchy (see Microsoft Learn: 'Azure Policy for management groups')
3. Assign the policy at the root management group scope to enforce placement for all new subscriptions

## Validation
Run 'Get-AzManagementGroupSubscription -GroupName <CorrectMG>' to confirm the subscription is now listed under the intended management group.

## Rollback
Move the subscription back to the root management group using the same PowerShell or CLI commands, and remove or disable the enforcing Azure Policy assignment if needed.

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal>
- <https://learn.microsoft.com/en-us/azure/governance/policy/overview#management-groups>
