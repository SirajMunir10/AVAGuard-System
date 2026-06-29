# Troubleshooting: Azure Backup (UserErrorBCMPremiumStorageQuotaError)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve UserErrorBCMPremiumStorageQuotaError when backing up premium VMs on VM backup stack V1?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Premium VMs on VM backup stack V1

## Symptoms
- Could not copy the snapshot of the virtual machine, due to insufficient free space in the storage account

## Error Codes
- `UserErrorBCMPremiumStorageQuotaError`

## Root Causes
1. Insufficient free space in the storage account for copying the snapshot

## Remediation Steps
1. Allocate only 50 percent (17.5 TB) of the total storage account space so that the Azure Backup service can copy the snapshot to the storage account and transfer data from this copied location in the storage account to the vault

## Validation
1. Check the current storage account usage: Run `Get-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName> | Select-Object -ExpandProperty Usage` to confirm the used capacity is below 50% (17.5 TB).
2. Verify the backup job status: Use `Get-AzRecoveryServicesBackupJob -ResourceGroupName <VaultResourceGroupName> -VaultName <VaultName> -Status InProgress` to ensure no ongoing backup jobs are failing with UserErrorBCMPremiumStorageQuotaError.
3. Review backup job history: Run `Get-AzRecoveryServicesBackupJob -ResourceGroupName <VaultResourceGroupName> -VaultName <VaultName> -Status Completed -From (Get-Date).AddDays(-1)` to confirm recent backup jobs completed successfully.

## Rollback
1. If the remediation causes insufficient space for snapshots, increase the storage account quota by contacting Azure Support to request a higher limit for premium storage accounts.
2. Alternatively, move the VM backup to a different storage account with sufficient space: Use `Set-AzVMBootDiagnostic -ResourceGroupName <ResourceGroupName> -VMName <VMName> -StorageAccountName <NewStorageAccountName>` to update the boot diagnostics storage account, then reconfigure the backup policy to use the new storage account.
3. Restore the original storage account configuration: If the storage account was changed, revert to the previous storage account using the same `Set-AzVMBootDiagnostic` cmdlet with the original storage account name.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
