# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
How do I lock deployed Azure resources using Azure CLI to prevent accidental deletion?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure CLI

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the az lock create command to lock a resource. Provide the resource name, resource type, and resource group name. Example: az lock create --name LockSite --lock-type CanNotDelete --resource-group exampleresourcegroup --resource-name examplesite --resource-type Microsoft.Web/sites
2. To lock a resource group, provide the resource group name. Example: az lock create --name LockGroup --lock-type CanNotDelete --resource-group exampleresourcegroup

## Validation
Use az lock list to verify locks. To get all locks in your subscription: az lock list. To get all locks for a resource: az lock list --resource-group exampleresourcegroup --resource-name examplesite --namespace Microsoft.Web --resource-type sites --parent "". To get all locks for a resource group: az lock list --resource-group exampleresourcegroup

## Rollback
To delete a lock for a resource: lockid=$(az lock show --name LockSite --resource-group exampleresourcegroup --resource-type Microsoft.Web/sites --resource-name examplesite --output tsv --query id) then az lock delete --ids $lockid. To delete a lock for a resource group: lockid=$(az lock show --name LockSite --resource-group exampleresourcegroup --output tsv --query id) then az lock delete --ids $lockid

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
