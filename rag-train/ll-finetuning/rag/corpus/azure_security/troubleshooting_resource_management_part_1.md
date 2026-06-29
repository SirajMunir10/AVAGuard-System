# Troubleshooting: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Troubleshooting

## Scenario / Query
Why does a read-only lock on a storage account prevent users from listing account keys?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Read-only lock applied to a storage account

## Symptoms
- Users cannot list storage account keys
- POST requests to Azure Storage List Keys operation are blocked

## Error Codes
N/A

## Root Causes
1. A read-only lock prevents the POST method from sending data to the Azure Resource Manager API
2. The Azure Storage List Keys operation uses a POST request

## Remediation Steps
1. Remove the read-only lock from the storage account if listing keys is required
2. Alternatively, use Microsoft Entra credentials to access blob or queue data instead of account keys

## Validation
1. Verify the read-only lock is removed: Run 'az lock list --resource-group <resource-group-name> --resource-name <storage-account-name> --resource-type Microsoft.Storage/storageAccounts' and confirm no lock of type 'ReadOnly' exists. 2. Test listing account keys: Execute 'az storage account keys list --account-name <storage-account-name> --resource-group <resource-group-name>' and confirm keys are returned successfully. 3. Optionally, confirm POST requests are allowed: Use 'Invoke-RestMethod -Method Post -Uri "https://management.azure.com/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Storage/storageAccounts/<storage-account-name>/listKeys?api-version=2023-01-01" -Headers @{"Authorization"="Bearer <access-token>"}' and verify a 200 OK response with key data.

## Rollback
1. Reapply the read-only lock: Run 'az lock create --lock-type ReadOnly --name <lock-name> --resource-group <resource-group-name> --resource-name <storage-account-name> --resource-type Microsoft.Storage/storageAccounts'. 2. Confirm the lock is active: Run 'az lock list --resource-group <resource-group-name> --resource-name <storage-account-name> --resource-type Microsoft.Storage/storageAccounts' and verify a lock of type 'ReadOnly' appears. 3. Verify that listing keys is blocked: Execute 'az storage account keys list --account-name <storage-account-name> --resource-group <resource-group-name>' and confirm an error message indicating the operation is not allowed due to the lock.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
