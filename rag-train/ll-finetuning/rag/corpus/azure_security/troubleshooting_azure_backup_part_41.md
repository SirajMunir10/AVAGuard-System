# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreNotSupportedForEncryptedAzureVM)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failures for encrypted Azure VMs?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as Cross Subscription Restore is not supported for Encrypted Azure VMs

## Error Codes
- `UserErrorCrossSubscriptionRestoreNotSupportedForEncryptedAzureVM`

## Root Causes
1. Cross Subscription Restore is not supported for Encrypted Azure VMs

## Remediation Steps
1. Use the same subscription for Restore of Encrypted Azure VMs

## Validation
1. Verify that the source encrypted Azure VM is in the same subscription as the Recovery Services vault by running: Get-AzRecoveryServicesBackupItem -VaultId $vault.ID -Container $container -WorkloadType AzureVM | Where-Object {$_.Properties.VirtualMachineId -eq $sourceVMId}. 2. Confirm the restore operation completes without error by checking the job status: Get-AzRecoveryServicesBackupJob -VaultId $vault.ID -Status InProgress, Completed, Failed | Where-Object {$_.Operation -eq 'Restore'}. 3. Validate the restored VM is accessible and encrypted: Get-AzVm -ResourceGroupName $restoreRG -Name $restoreVMName | Select-Object Name, ResourceGroupName, StorageProfile.OSDisk.EncryptionSettings.Enabled.

## Rollback
1. If the restore operation fails or causes issues, delete the partially restored VM and its associated resources: Remove-AzVm -ResourceGroupName $restoreRG -Name $restoreVMName -Force. 2. Remove any managed disks created during the failed restore: Get-AzDisk -ResourceGroupName $restoreRG | Where-Object {$_.Name -like '*restore*'} | Remove-AzDisk -Force. 3. Re-initiate the restore to the original subscription using the same Recovery Services vault and backup point: Restore-AzRecoveryServicesBackupItem -VaultId $vault.ID -RecoveryPoint $rp -StorageAccountName $storageAccount -StorageAccountResourceGroupName $storageRG -TargetResourceGroupName $targetRG -TargetVMName $targetVMName.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
