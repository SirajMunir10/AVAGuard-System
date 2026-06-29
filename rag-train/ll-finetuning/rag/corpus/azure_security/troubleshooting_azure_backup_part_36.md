# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreNotSupportedForOLR)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failure for Original Location Recovery?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as Cross Subscription Restore is not supported for Original Location Recovery

## Error Codes
- `UserErrorCrossSubscriptionRestoreNotSupportedForOLR`

## Root Causes
1. Cross Subscription Restore is not supported for Original Location Recovery.

## Remediation Steps
1. Ensure that you select Create New/ Restore Disk for restore operation.

## Validation
1. Verify that the restore operation is configured to use 'Create new' or 'Restore disk' instead of 'Original location recovery'. 2. Run the following Azure PowerShell command to confirm the restore job is using the correct restore type: Get-AzRecoveryServicesBackupJob -VaultId <VaultID> | Where-Object {$_.Operation -eq 'Restore' -and $_.Status -eq 'Completed'} | Select-Object JobId, Operation, Status. 3. Check the Azure portal under the Recovery Services vault -> Backup items -> Restore points, and ensure the restore point selected is associated with a 'Create new' or 'Restore disk' operation.

## Rollback
1. If the restore operation fails or causes issues, cancel any in-progress restore jobs using: Stop-AzRecoveryServicesBackupJob -JobId <JobID> -VaultId <VaultID>. 2. Delete any newly created resources (e.g., disks, VMs) that were created as part of the failed restore. 3. Re-initiate the restore operation using the original location recovery method, ensuring the subscription and resource group are correctly targeted. 4. If cross-subscription restore is required, consider using a different restore method such as 'Restore as new VM' or 'Restore disks' to a different subscription.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
