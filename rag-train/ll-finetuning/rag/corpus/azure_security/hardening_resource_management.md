# Hardening: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Hardening

## Scenario / Query
How do I lock an Azure subscription, resource group, or resource to protect them from accidental user deletions and modifications?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Management locks

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set locks that prevent either deletions or modifications. In the portal, these locks are called Delete and Read-only. In the command line, these locks are called CanNotDelete and ReadOnly.
2. CanNotDelete means authorized users can read and modify a resource, but they can't delete it.
3. ReadOnly means authorized users can read a resource, but they can't delete or update it. Applying this lock is similar to restricting all authorized users to the permissions that the Reader role provides.

## Validation
1. Navigate to the Azure portal, select the subscription, resource group, or resource that was locked. 2. Under 'Settings', select 'Locks'. 3. Verify that the lock (CanNotDelete or ReadOnly) is listed with the correct name and type. 4. Attempt to delete the resource (for CanNotDelete) or modify the resource (for ReadOnly) as a user with Owner or Contributor permissions; the action should be blocked with an error message indicating the resource is locked. 5. Use Azure CLI: `az lock list --resource-group <rg-name>` or `az lock list --subscription <sub-id>` to confirm the lock exists. 6. Use PowerShell: `Get-AzResourceLock -ResourceGroupName <rg-name>` or `Get-AzResourceLock -SubscriptionId <sub-id>` to verify.

## Rollback
1. In the Azure portal, navigate to the locked subscription, resource group, or resource. 2. Under 'Settings', select 'Locks'. 3. Click the 'Delete' icon next to the lock you want to remove. 4. Confirm the deletion. 5. Use Azure CLI: `az lock delete --name <lock-name> --resource-group <rg-name>` or `az lock delete --name <lock-name> --subscription <sub-id>`. 6. Use PowerShell: `Remove-AzResourceLock -LockName <lock-name> -ResourceGroupName <rg-name>` or `Remove-AzResourceLock -LockName <lock-name> -SubscriptionId <sub-id>`. 7. Verify removal by repeating validation steps.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
