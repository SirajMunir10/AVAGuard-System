# Implementation: Resource Manager

**Domain:** Azure
**Subdomain:** Resource Manager
**Incident Type:** Implementation

## Scenario / Query
How to implement resource locks in Azure to prevent accidental deletion or modification of resources?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Resource locks can be applied at subscription, resource group, or resource level.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Apply a CanNotDelete lock to prevent deletion of a resource.
2. Apply a ReadOnly lock to prevent modification of a resource.

## Validation
1. Run: `Get-AzResourceLock -ResourceGroupName <ResourceGroupName> -ResourceName <ResourceName> -ResourceType <ResourceType>` (or at subscription/resource group scope) to confirm the lock exists and its LockLevel is 'CanNotDelete' or 'ReadOnly'. 2. Attempt to delete the locked resource via Azure Portal, CLI (`az resource delete`), or PowerShell (`Remove-AzResource`); the operation should fail with a 'Conflict' or 'Forbidden' error. 3. For ReadOnly locks, attempt to modify the resource (e.g., update tags or properties); the operation should fail with a similar error.

## Rollback
1. Remove the lock using: `Remove-AzResourceLock -LockName <LockName> -ResourceGroupName <ResourceGroupName> -ResourceName <ResourceName> -ResourceType <ResourceType>` (or at the appropriate scope). 2. Verify removal with `Get-AzResourceLock` to ensure the lock no longer appears. 3. Retry the original delete or modify operation to confirm it now succeeds.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
