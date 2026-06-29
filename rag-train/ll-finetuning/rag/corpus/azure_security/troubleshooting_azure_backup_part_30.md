# Troubleshooting: Azure Backup (UserErrorInstantRpNotFound)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve restore failure when the snapshot of the VM was not found?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Restore failed because the snapshot of the VM was not found

## Error Codes
- `UserErrorInstantRpNotFound`

## Root Causes
1. The snapshot could have been deleted
2. The recovery point was not transferred to the vault and was deleted in the snapshot phase

## Remediation Steps
1. Try to restore the VM from a different restore point

## Validation
1. Run 'Get-AzRecoveryServicesBackupItem -VaultId $vault.ID -Container $container -WorkloadType AzureVM' to list backup items. 2. Use 'Get-AzRecoveryServicesBackupRecoveryPoint -Item $item' to list recovery points for the VM. 3. Verify that at least one recovery point with a valid snapshot exists (e.g., RecoveryPointType = 'AppConsistent' or 'FileSystemConsistent' and not marked as deleted). 4. Attempt a test restore from a different recovery point using 'Restore-AzRecoveryServicesBackupItem -RecoveryPoint $rp -StorageAccountName $storageAccount -StorageAccountResourceGroupName $resourceGroup' and confirm the restore job completes without the 'UserErrorInstantRpNotFound' error.

## Rollback
1. If the restore from a different recovery point fails, re-attempt the original restore point using 'Restore-AzRecoveryServicesBackupItem -RecoveryPoint $originalRP -StorageAccountName $storageAccount -StorageAccountResourceGroupName $resourceGroup'. 2. If the original restore point is still unavailable, check the backup job history with 'Get-AzRecoveryServicesBackupJob -VaultId $vault.ID -From (Get-Date).AddDays(-30) -Status Failed' to identify any snapshot deletion events. 3. If the snapshot was deleted, re-create the VM from the latest available recovery point in the vault (not snapshot) by selecting a recovery point with RecoveryPointType = 'VaultStandard' and performing a restore to a new VM. 4. After restore, re-enable backup on the new VM using 'Enable-AzRecoveryServicesBackupProtection -Policy $policy -Name $vmName -ResourceGroupName $resourceGroup'.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
