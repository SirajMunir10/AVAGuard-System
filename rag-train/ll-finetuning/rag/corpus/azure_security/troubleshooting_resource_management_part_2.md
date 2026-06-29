# Troubleshooting: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Troubleshooting

## Scenario / Query
Why does a read-only lock on a storage account prevent creation of a blob container?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Read-only lock applied to a storage account

## Symptoms
- Cannot create a blob container in the storage account

## Error Codes
N/A

## Root Causes
1. A read-only lock blocks control plane create requests
2. Blob container creation can be done through both control plane and data plane, but the lock only blocks control plane requests

## Remediation Steps
1. Remove the read-only lock from the storage account to allow blob container creation via control plane
2. Alternatively, create the blob container through the data plane, which is not blocked by the lock

## Validation
1. Verify the read-only lock is removed: Run `az lock list --resource-group <resource-group-name> --resource-name <storage-account-name> --resource-type Microsoft.Storage/storageAccounts --query "[?level=='ReadOnly']"` and confirm the output is empty. 2. Attempt to create a blob container via control plane: Run `az storage container create --account-name <storage-account-name> --name <container-name> --auth-mode login` and confirm success. 3. Optionally, verify data plane creation still works: Run `az storage container create --account-name <storage-account-name> --name <container-name2> --auth-mode key` and confirm success.

## Rollback
1. Reapply the read-only lock: Run `az lock create --name <lock-name> --resource-group <resource-group-name> --resource-name <storage-account-name> --resource-type Microsoft.Storage/storageAccounts --lock-type ReadOnly`. 2. Verify the lock is applied: Run `az lock list --resource-group <resource-group-name> --resource-name <storage-account-name> --resource-type Microsoft.Storage/storageAccounts --query "[?level=='ReadOnly']"` and confirm the lock exists. 3. Confirm that control plane blob container creation is blocked: Run `az storage container create --account-name <storage-account-name> --name <container-name> --auth-mode login` and expect an error.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
