# Implementation: Management Group Hierarchy

**Domain:** Governance
**Subdomain:** Management Group Hierarchy
**Incident Type:** Implementation

## Scenario / Query
After creating a new Azure management group hierarchy, policy assignments at the root management group are not being inherited by child subscriptions. What configuration step is missing?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Root management group ID is set, but no policy assignment scope includes the root group ID.

## Symptoms
- Azure Policy assignments created at the root management group do not appear in the effective policies of child subscriptions.
- Compliance reports show 'Not applicable' for policies assigned at the root group.

## Error Codes
N/A

## Root Causes
1. The root management group was not explicitly defined as the scope for the policy assignment. By default, policy assignments are scoped to the management group or subscription where they are created, but inheritance requires the assignment to be at the root management group scope.
2. The root management group ID may not be set correctly in the tenant. The root management group ID is a GUID that must be retrieved and used as the scope.

## Remediation Steps
1. Retrieve the root management group ID using the Azure CLI: 'az account management-group list --query "[?name=='Tenant Root Group'].id" --output tsv'.
2. Recreate the policy assignment with the root management group as the scope: 'az policy assignment create --name "PolicyName" --policy "PolicyDefinitionID" --scope "/providers/Microsoft.Management/managementGroups/<RootGroupID>"'.
3. Alternatively, use the Azure portal: navigate to 'Management groups', select the root group, then 'Assign policy' under 'Policies'.

## Validation
Verify that the policy assignment shows the root management group in the 'Scope' column. Run 'az policy assignment list --scope "/providers/Microsoft.Management/managementGroups/<RootGroupID>"' and confirm the assignment is listed.

## Rollback
Delete the policy assignment from the root management group using 'az policy assignment delete --name "PolicyName" --scope "/providers/Microsoft.Management/managementGroups/<RootGroupID>"'.

## References
- <https://learn.microsoft.com/en-us/azure/governance/management-groups/overview>
- <https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/create-and-manage>
