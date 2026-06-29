# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle job cancellation errors in Azure Backup for VMs?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Jobs Cancellation isn't supported for this job type
- The job isn't in a cancelable state
- The selected job isn't in a cancelable state
- Backup can't cancel the job because it isn't in progress
- Backup failed to cancel the job

## Error Codes
N/A

## Root Causes
1. The job is almost finished
2. The job is in a transitory state
3. The job is not in progress

## Remediation Steps
1. Wait until the job finishes
2. Wait for the job to finish
3. Wait until the job is finished
4. Try to cancel an in-progress job
5. Wait a minute and retry the cancel operation

## Validation
Run the following Azure PowerShell command to check the current state of the backup job: Get-AzRecoveryServicesBackupJob -VaultId <VaultId> -JobId <JobId>. Verify that the job status is 'Completed' or 'CompletedWithWarnings'. If the job is no longer listed, confirm by running Get-AzRecoveryServicesBackupJob -VaultId <VaultId> -Status InProgress and ensure no jobs with the same ID appear.

## Rollback
If the remediation (waiting) does not resolve the cancellation error, retry the cancel operation after confirming the job is in 'InProgress' state. Use the command: Stop-AzRecoveryServicesBackupJob -VaultId <VaultId> -JobId <JobId>. If the job still fails to cancel, wait 60 seconds and retry. If the job has already finished, no rollback is needed.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
