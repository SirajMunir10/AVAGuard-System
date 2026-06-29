# Optimization: Resource Organization

**Domain:** Governance
**Subdomain:** Resource Organization
**Incident Type:** Optimization

## Scenario / Query
A customer has hundreds of Azure subscriptions with no consistent naming convention or management group hierarchy. They want to enforce a standard naming pattern and group subscriptions by department and environment to improve governance and cost tracking. How should they design the management group structure and apply Azure Policy to enforce naming conventions?

## Environment Context
- **Tenant Type:** Enterprise (multiple departments, dev/test/prod environments)
- **Configuration:** No existing management group hierarchy; subscriptions are scattered under the root management group.

## Symptoms
- Subscriptions have inconsistent, non-descriptive names (e.g., 'sub123', 'test1', 'prod-westus').
- No logical grouping for chargeback or compliance reporting.
- Azure Policy is not applied at scale; each subscription must be individually configured.

## Error Codes
N/A

## Root Causes
1. No management group hierarchy defined.
2. No naming convention policy assigned at a scope above individual subscriptions.

## Remediation Steps
1. Design a management group hierarchy that mirrors the organization's structure (e.g., /root/Department/Environment).
2. Move each subscription into the appropriate management group using Azure Portal, PowerShell (New-AzManagementGroup), or Azure CLI (az account management-group add).
3. Create a custom Azure Policy definition with a 'pattern' effect to enforce a naming convention on resources (e.g., 'dep-env-{resourceType}-###').
4. Assign the naming policy at the root management group or at each department management group to ensure all new resources comply.
5. Use Azure Policy's 'audit' or 'deny' effect to prevent creation of non-compliant resources.

## Validation
After assignment, attempt to create a resource with a non-compliant name; the creation should be denied or flagged in the compliance dashboard.

## Rollback
Remove the policy assignment from the management group scope, or change the policy effect to 'audit' (non-enforcing).

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal>
- <https://learn.microsoft.com/en-us/azure/governance/policy/concepts/pattern-naming-convention>
