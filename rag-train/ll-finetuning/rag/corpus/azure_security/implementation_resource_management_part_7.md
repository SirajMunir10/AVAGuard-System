# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
How to assign the required permissions to tag Azure resources using the Tag Contributor role?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Tag Contributor role, Microsoft.Resources/tags resource type

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign the Tag Contributor role to grant write access to the Microsoft.Resources/tags resource type.
2. This role allows tagging any resource even without direct access to the resource itself.
3. The Tag Contributor role can apply tags to subscriptions through the Azure portal.
4. It supports all tag operations through Azure PowerShell and REST API.

## Validation
1. Verify the role assignment: Run `Get-AzRoleAssignment -RoleDefinitionName 'Tag Contributor' -Scope '/subscriptions/<subscription-id>'` in Azure PowerShell. 2. Confirm the user/group can tag a resource: Use `New-AzTag -ResourceId '/subscriptions/<subscription-id>/resourceGroups/<rg-name>/providers/Microsoft.Compute/virtualMachines/<vm-name>' -Tag @{'env'='test'}`. 3. Check the portal: Navigate to the resource's 'Tags' blade and verify the tag is visible.

## Rollback
1. Remove the role assignment: Run `Remove-AzRoleAssignment -RoleDefinitionName 'Tag Contributor' -Scope '/subscriptions/<subscription-id>' -ObjectId <object-id>` in Azure PowerShell. 2. Delete any test tags: Use `Remove-AzTag -ResourceId '/subscriptions/<subscription-id>/resourceGroups/<rg-name>/providers/Microsoft.Compute/virtualMachines/<vm-name>' -Tag @{'env'='test'}`. 3. Confirm removal: Re-run the validation commands to ensure no residual permissions or tags remain.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
