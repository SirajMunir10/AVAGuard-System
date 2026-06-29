# Governance: Microsoft Entra ID (Azure AD) Governance

**Domain:** Azure
**Subdomain:** Microsoft Entra ID (Azure AD) Governance
**Incident Type:** Governance

## Scenario / Query
An Azure subscription has been created by a user who is not an Owner or Contributor of the management group or billing account. How can an administrator detect and remediate this unauthorized subscription creation?

## Environment Context
- **Tenant Type:** Enterprise (EA or MCA)
- **Configuration:** Default Azure RBAC permissions allow users with Owner role on a billing account or management group to create subscriptions. If a user without those roles creates a subscription, it may indicate a misconfiguration or a security incident.

## Symptoms
- Unexpected Azure subscription appears in the tenant
- Subscription creation activity logged without a corresponding authorized role assignment
- Billing or cost management shows a subscription not created by an authorized administrator

## Error Codes
N/A

## Root Causes
1. A user was granted the Subscription Creator role on a management group scope, which is not an Owner or Contributor role but still allows subscription creation
2. A custom role with Microsoft.Subscription/aliases/write permission was assigned to a user at a high scope
3. Billing administrator role (EA or MCA) was assigned to a user who is not an Owner or Contributor of the management group

## Remediation Steps
1. Review the Azure Activity Log for the subscription creation event to identify the user and the scope at which they were granted permission
2. Remove the Subscription Creator role assignment from the user if it was not intended
3. Restrict the ability to create subscriptions by assigning the Subscription Creator role only to a limited set of users via a management group policy
4. Use Azure Policy to deny subscription creation at the root management group scope for all users except a break-glass account

## Validation
Verify that only authorized users can create subscriptions by checking the role assignments at the management group and billing account scopes. Use the Azure portal or Azure CLI to list role assignments with the Microsoft.Subscription/aliases/write permission.

## Rollback
If the subscription was created in error, the subscription owner can cancel the subscription within the Azure portal (for most subscription types) or contact billing support for cancellation.

## References
- <https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/prevent-subscription-creation>
