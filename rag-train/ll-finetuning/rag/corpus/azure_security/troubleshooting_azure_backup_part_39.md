# Troubleshooting: Azure Backup (UserErrorCrossSubscriptionRestoreNotSupportedFromSnapshot)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve cross-subscription restore failure when restoring from a Snapshot recovery point?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Operation failed as Cross Subscription Restore is not supported when restoring from a Snapshot recovery point

## Error Codes
- `UserErrorCrossSubscriptionRestoreNotSupportedFromSnapshot`

## Root Causes
1. Cross Subscription Restore is not supported when restoring from a Snapshot recovery point.

## Remediation Steps
1. Select a different recovery point where Tier 2 (Vault-Tier) is available.

## Validation
1. Navigate to the Recovery Services vault in the Azure portal.
2. Select 'Backup items' and choose the VM for which the restore failed.
3. Click 'Restore VM' and review the available recovery points.
4. Confirm that the selected recovery point has 'Tier 2 (Vault-Tier)' listed as available.
5. Attempt a cross-subscription restore using that vault-tier recovery point and verify the operation completes without the UserErrorCrossSubscriptionRestoreNotSupportedFromSnapshot error.

## Rollback
1. If the cross-subscription restore fails or causes issues, revert to the original subscription context.
2. Re-select a snapshot recovery point (Tier 1) for restore within the same subscription.
3. Ensure the restore operation targets the original subscription and resource group.
4. If needed, delete any partially created resources from the failed cross-subscription restore attempt.
5. Document the failure and contact Azure Support for further assistance if cross-subscription restore from snapshot is required.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
