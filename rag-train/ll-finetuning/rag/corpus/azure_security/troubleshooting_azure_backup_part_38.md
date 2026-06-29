# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreNotSupportedForCRR)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failure when used with Cross Region Restore?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as Cross Subscription Restore is not supported along-with Cross Region Restore

## Error Codes
- `UserErrorCrossSubscriptionRestoreNotSupportedForCRR`

## Root Causes
1. Cross Subscription Restore is not supported along-with Cross Region Restore.

## Remediation Steps
1. Use either Cross Subscription Restore or Cross Region Restore.

## Validation
1. Verify that the backup vault is configured for either Cross Subscription Restore (CSR) or Cross Region Restore (CRR), but not both. In the Azure portal, navigate to the Recovery Services vault, select 'Properties', and under 'Cross Region Restore', ensure it is set to 'Disable' if CSR is intended, or 'Enable' if CRR is intended. 2. If CSR is intended, confirm that the target subscription is listed in the vault's 'Cross Subscription Restore' settings under 'Properties'. 3. Attempt a restore operation: use Azure CLI command 'az backup restore restore-disks' with the appropriate parameters for the chosen restore type (e.g., --restore-mode for CSR or --use-secondary-region for CRR) and verify the operation completes without error 'UserErrorCrossSubscriptionRestoreNotSupportedForCRR'.

## Rollback
1. If the validation fails or the restore operation fails, revert the vault configuration to the previous state: in the Azure portal, navigate to the Recovery Services vault, select 'Properties', and set 'Cross Region Restore' back to its original setting (Enable or Disable). 2. If CSR was enabled and needs to be disabled, remove the target subscription from the 'Cross Subscription Restore' list under 'Properties'. 3. Re-attempt the restore using the original restore method (CSR or CRR) that was in use before the change, and verify the operation completes successfully.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
