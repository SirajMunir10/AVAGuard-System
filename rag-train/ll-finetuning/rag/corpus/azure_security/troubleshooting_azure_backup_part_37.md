# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreNotSupportedForUnManagedAzureVM)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failure for Azure VMs with Unmanaged Disks?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as Cross Subscription Restore is not supported for Azure VMs with Unmanaged Disks

## Error Codes
- `UserErrorCrossSubscriptionRestoreNotSupportedForUnManagedAzureVM`

## Root Causes
1. Cross Subscription Restore is not supported for Azure VMs with Unmanaged Disks.

## Remediation Steps
1. Perform standard restores within the same subscription instead.

## Validation
1. Verify that the source VM's disks are unmanaged by checking the VM's storage profile: az vm show --resource-group <SourceRG> --name <SourceVMName> --query 'storageProfile.osDisk.managedDisk' -o tsv. If the output is null, the disk is unmanaged. 2. Confirm that the restore operation is initiated in the same subscription as the source VM by running: az backup restore restore-disks --resource-group <TargetRG> --vault-name <VaultName> --container-name <ContainerName> --item-name <ItemName> --recovery-point-id <RPID> --storage-account-name <StorageAccountName> --subscription <SourceSubscriptionID>. 3. Check the restore job status: az backup job list --resource-group <VaultRG> --vault-name <VaultName> --query "[?operation=='Restore'].{Status:status, ErrorDetails:errorDetails}" -o table. Ensure the status is 'Completed' with no error details.

## Rollback
1. If the restore operation fails or causes issues, delete any partially created disks or storage artifacts: az disk delete --resource-group <TargetRG> --name <DiskName> --yes (if managed disks were inadvertently created) or az storage blob delete --account-name <StorageAccountName> --container-name <ContainerName> --name <BlobName> (for unmanaged disk VHDs). 2. Revert to the original source VM state by ensuring no changes were made to the source VM's configuration. 3. If the restore was attempted in a different subscription, cancel the restore job: az backup job stop --resource-group <VaultRG> --vault-name <VaultName> --name <JobName>. 4. Document the failure and plan a new restore within the same subscription following the standard restore procedure.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
