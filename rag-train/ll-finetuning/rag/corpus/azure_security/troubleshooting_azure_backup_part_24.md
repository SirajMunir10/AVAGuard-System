# Troubleshooting: Azure Backup (CopyingVHDsFromBackUpVaultTakingLongTime)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the CopyingVHDsFromBackUpVaultTakingLongTime error when copying backed up data from vault times out?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure VM Backup

## Symptoms
- Copying backed up data from vault timed out

## Error Codes
- `CopyingVHDsFromBackUpVaultTakingLongTime`

## Root Causes
1. Transient storage errors
2. Insufficient storage account IOPS for backup service to transfer data to the vault within the timeout period

## Remediation Steps
1. Configure VM backup using these best practices and retry the backup operation.

## Validation
1. Verify that the VM backup configuration follows best practices: Check that the backup policy is set to use Standard or Premium storage for the backup vault, and that the storage account used for backup has sufficient IOPS (at least 1000 IOPS for the backup service).
2. Run the following Azure CLI command to check the backup job status and ensure no timeout errors: az backup job list --resource-group <ResourceGroupName> --vault-name <VaultName> --output table
3. Confirm that the backup job completes successfully within the expected time by reviewing the job details: az backup job show --resource-group <ResourceGroupName> --vault-name <VaultName> --name <JobName>
4. Validate that the backup data is accessible and no CopyingVHDsFromBackUpVaultTakingLongTime error appears in the Azure Backup reports or logs.

## Rollback
1. If the remediation fails or causes issues, revert the VM backup configuration to the previous settings: Update the backup policy to the original storage tier (e.g., change from Standard to Basic or adjust IOPS limits) using Azure Portal or PowerShell: Set-AzRecoveryServicesBackupProtectionPolicy -VaultId <VaultID> -Policy <OriginalPolicyObject>
2. If the backup job continues to time out, consider increasing the storage account IOPS or switching to a different storage account with higher performance limits.
3. As a last resort, disable and re-enable backup for the VM to reset the backup pipeline: az backup protection disable --resource-group <ResourceGroupName> --vault-name <VaultName> --item-name <VMName> --container-name <ContainerName> --delete-backup-data false, then re-enable with az backup protection enable-for-vm --resource-group <ResourceGroupName> --vault-name <VaultName> --vm <VMID> --policy-name <PolicyName>.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
