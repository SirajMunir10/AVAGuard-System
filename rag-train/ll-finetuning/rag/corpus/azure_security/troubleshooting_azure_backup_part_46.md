# Troubleshooting: Azure Backup (BackUpOperationFailedV2)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve BackUpOperationFailedV2 error when VM backups fail after policy migration from Standard to Enhanced policy?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** VM backup policy migration from Standard to Enhanced

## Symptoms
- Backups of VMs have failed after the policy migration from Standard to Enhanced policy

## Error Codes
- `BackUpOperationFailedV2`

## Root Causes
1. Snapshot retention of the Enhanced policy is applied on the older recovery points that were originally created under the Standard policy when you move a VM from a Standard to Enhanced policy

## Remediation Steps
1. Contact Microsoft Support for resolution

## Validation
1. Verify that the VM backup policy migration from Standard to Enhanced has been completed by checking the backup policy assigned to the VM in the Azure portal (Backup center > Backup instances > select the VM > Properties > Backup policy).
2. Confirm that no new backup jobs are failing with error code BackUpOperationFailedV2 by running: `Get-AzRecoveryServicesBackupJob -ResourceGroupName <ResourceGroupName> -VaultName <VaultName> -Status Failed | Where-Object {$_.ErrorCode -eq 'BackUpOperationFailedV2'}`
3. Check that the snapshot retention for the Enhanced policy is correctly applied to older recovery points by reviewing the retention rules in the Enhanced policy (Backup center > Backup policies > select the Enhanced policy > Modify policy > Retention rules).
4. Ensure that the VM backup job history shows successful backups after the policy migration by running: `Get-AzRecoveryServicesBackupJob -ResourceGroupName <ResourceGroupName> -VaultName <VaultName> -Status Completed -From (Get-Date).AddDays(-7)`

## Rollback
1. Contact Microsoft Support as per the remediation steps to revert the policy migration or adjust snapshot retention settings for older recovery points.
2. If instructed by Support, reassign the original Standard backup policy to the VM using: `Set-AzRecoveryServicesBackupProtectionPolicy -VaultId <VaultID> -Policy $StandardPolicy -Item $VMItem`
3. Monitor backup jobs for the VM to ensure they resume with the Standard policy and no longer fail with BackUpOperationFailedV2.
4. Document the rollback actions taken and any changes to backup policies for audit purposes.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
