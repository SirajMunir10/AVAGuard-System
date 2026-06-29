# Troubleshooting: Resource Manager

**Domain:** Azure
**Subdomain:** Resource Manager
**Incident Type:** Troubleshooting

## Scenario / Query
How to delete a locked resource group created by a managed application like Azure Databricks?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Managed application with locked infrastructure resource group

## Symptoms
- Error stating that the resource group is locked when trying to delete the infrastructure resource group
- Error stating that the lock can't be deleted because a system application owns it when trying to delete the lock for the infrastructure resource group

## Error Codes
N/A

## Root Causes
1. The infrastructure resource group is locked by a system application (managed application) and cannot be deleted directly or have its lock removed manually

## Remediation Steps
1. Delete the service (managed application) instead of the infrastructure resource group
2. For managed applications, choose the service you deployed
3. Notice the service includes a link for a Managed Resource Group that holds the infrastructure and is locked
4. To delete everything for the service, including the locked infrastructure resource group, choose Delete for the service

## Validation
1. Verify that the managed application (e.g., Azure Databricks workspace) has been deleted by running: az managedapp list --query "[?name=='<managed-app-name>']" --output none. 2. Confirm the infrastructure resource group no longer exists: az group show --name <infrastructure-resource-group-name> --query "properties.provisioningState" --output tsv (should return 'NotFound' or empty). 3. Check that no locks remain on the resource group: az lock list --resource-group <infrastructure-resource-group-name> --output none (should return no locks).

## Rollback
1. If the managed application deletion fails or was unintended, restore it from a backup or redeploy the managed application using the original deployment template. 2. If the infrastructure resource group was accidentally deleted but the managed application still exists, recreate the resource group with the same name and region: az group create --name <infrastructure-resource-group-name> --location <region>. 3. Reapply the necessary locks to the resource group: az lock create --name <lock-name> --resource-group <infrastructure-resource-group-name> --lock-type CanNotDelete.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
