# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreNotSupportedForTrustedLaunchAzureVM)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failures for Trusted Launch Azure VMs?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as Cross Subscription Restore is not supported for Trusted Launch Azure VMs (TVMs)

## Error Codes
- `UserErrorCrossSubscriptionRestoreNotSupportedForTrustedLaunchAzureVM`

## Root Causes
1. Cross Subscription Restore is not supported for Trusted Launch Azure VMs (TVMs)

## Remediation Steps
1. Use the same subscription for Restore of Trusted Launch Azure VMs

## Validation
1. Verify that the Trusted Launch Azure VM is restored in the same subscription as the backup vault. Use Azure CLI: az backup recoverypoint list --vault-name <VaultName> --resource-group <VaultRG> --container-name <ContainerName> --item-name <VMName> --backup-management-type AzureIaasVM. Then attempt a restore to the same subscription using: az backup restore restore-disks --vault-name <VaultName> --resource-group <VaultRG> --container-name <ContainerName> --item-name <VMName> --rp-name <RecoveryPointName> --storage-account <StorageAccountName> --target-resource-group <TargetRG> --target-vm-name <VMName> --target-vnet-name <VNetName> --target-subnet-name <SubnetName> --target-subscription <SameSubscriptionID>. Confirm the restore operation completes without the error 'UserErrorCrossSubscriptionRestoreNotSupportedForTrustedLaunchAzureVM'. 2. In Azure portal, navigate to the backup vault, select 'Backup Items', choose the VM, and click 'Restore VM'. Ensure the 'Subscription' dropdown shows the same subscription as the vault and proceed. Verify the restore job status shows 'Completed'.

## Rollback
If the restore fails or causes issues: 1. Cancel any ongoing restore operation via Azure CLI: az backup job stop --vault-name <VaultName> --resource-group <VaultRG> --name <JobName>. 2. Delete any partially created resources (e.g., disks, NICs) in the target resource group using: az resource delete --ids <ResourceID>. 3. Revert to the original VM state by restoring from a different recovery point in the same subscription if needed. 4. If cross-subscription restore is required, consider using a non-Trusted Launch VM or export the VM's disks to a storage account in the target subscription and create a new VM manually. Refer to: https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
