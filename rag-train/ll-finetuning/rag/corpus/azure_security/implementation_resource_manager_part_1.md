# Implementation: Resource Manager

**Domain:** Azure
**Subdomain:** Resource Manager
**Incident Type:** Implementation

## Scenario / Query
How to implement a resource lock on a resource group using Bicep templates?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Bicep deployment targeting subscription scope

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define a Bicep file with targetScope = 'subscription' and parameters for resource group name and location.
2. Create a resource group using 'Microsoft.Resources/resourceGroups@2021-04-01'.
3. Deploy a module referencing 'lockRg.bicep' that adds a resource group lock with scope set to the resource group.
4. In 'lockRg.bicep', define a resource of type 'Microsoft.Authorization/locks@2016-09-01' with properties: level set to 'CanNotDelete' and notes set to 'Resource group and its resources should not be deleted.'

## Validation
1. Run 'az lock list --resource-group <resource-group-name> --output table' to confirm the lock exists with level 'CanNotDelete'.
2. Attempt to delete the resource group via 'az group delete --name <resource-group-name> --yes --no-wait' and verify the command fails with a 'ScopeLocked' error.
3. Check the Bicep deployment history using 'az deployment sub list --output table' and confirm the deployment succeeded.

## Rollback
1. Remove the resource lock using 'az lock delete --name <lock-name> --resource-group <resource-group-name>'.
2. If the lock was deployed via Bicep, redeploy the original Bicep template without the lock module, or run 'az deployment sub delete --name <deployment-name>' to remove the deployment.
3. Verify the lock is removed by running 'az lock list --resource-group <resource-group-name> --output table' and confirming no locks are listed.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
