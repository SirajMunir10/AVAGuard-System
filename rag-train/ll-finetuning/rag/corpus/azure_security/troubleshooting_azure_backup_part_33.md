# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve restore failure when the type of storage account specified for the restore operation isn't online?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The type of storage account specified for the restore operation isn't online

## Error Codes
N/A

## Root Causes
1. Transient error in Azure Storage
2. Outage

## Remediation Steps
1. Make sure that the storage account specified in the restore operation is online
2. Choose another storage account

## Validation
1. Run 'Get-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName>' to verify the storage account's ProvisioningState is 'Succeeded' and StatusOfPrimary is 'Available'. 2. Use 'Test-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName>' to confirm the account is reachable. 3. Initiate a test restore to the same storage account and monitor the job status in the Azure portal under Backup Center > Backup Jobs.

## Rollback
1. If the original storage account remains offline, select a different storage account that is online by running 'Get-AzStorageAccount | Where-Object {$_.ProvisioningState -eq "Succeeded" -and $_.StatusOfPrimary -eq "Available"}' to list available accounts. 2. Modify the restore operation to use the new storage account via the Azure portal or PowerShell. 3. If the issue persists, contact Azure Support to investigate underlying storage outages.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
