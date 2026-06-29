# Governance: Policy and Compliance

**Domain:** Governance
**Subdomain:** Policy and Compliance
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that several Azure subscriptions have been created outside the approved management group hierarchy, bypassing the organization's governance policies. How can the administrator detect and remediate these non-compliant subscriptions using Azure Policy and management group structure?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure management groups configured with a hierarchy, Azure Policy assigned to the root management group to enforce subscription placement

## Symptoms
- Subscriptions appear in the root management group instead of the intended child management group
- Azure Policy compliance dashboard shows non-compliant resources due to missing tags or location restrictions
- Audit logs show subscription creation events without proper management group association

## Error Codes
N/A

## Root Causes
1. No Azure Policy definition exists to enforce that subscriptions must be placed in a specific management group
2. Users with Contributor or Owner role at the root management group can create subscriptions outside the approved hierarchy

## Remediation Steps
1. Create an Azure Policy definition using the 'DeployIfNotExists' effect to move subscriptions to the correct management group. The policy should use the 'Microsoft.Management/managementGroups' resource type and the 'subscriptionId' parameter.
2. Assign the policy at the root management group scope with a parameter specifying the target management group ID.
3. Use the Azure Policy remediation task to move existing non-compliant subscriptions to the correct management group.
4. Restrict subscription creation permissions to a dedicated security group and remove the 'Microsoft.Subscription' resource provider registration from users who do not need it.

## Validation
Run the following Azure CLI command to verify that all subscriptions are in the correct management group: az account management-group list --query "[?name=='<TargetMG>'].properties.children[].id" --output tsv | ForEach-Object { az account show --id $_ --query name }

## Rollback
If the policy causes unintended moves, remove the policy assignment and manually move subscriptions back using the Azure portal or the Move-AzManagementGroupSubscription PowerShell cmdlet.

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/create-management-group-portal>
- <https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies#management-groups>
