# Troubleshooting: Azure Backup (ExtensionFailedSnapshotLimitReachedError)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ExtensionFailedSnapshotLimitReachedError when Azure Backup snapshot operation fails due to snapshot limit exceeded for some attached disks?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Snapshot operation failed as snapshot limit is exceeded for some of the disks attached

## Error Codes
- `ExtensionFailedSnapshotLimitReachedError`

## Root Causes
1. Snapshot limit has exceeded for some of the disks attached

## Remediation Steps
1. Delete the disk blob-snapshots that aren't required. Be careful to not delete disk blobs. Only snapshot blobs should be deleted.
2. If Soft-delete is enabled on VM disk Storage-Accounts, configure soft-delete retention so existing snapshots are less than the maximum allowed at any point of time.
3. If Azure Site Recovery is enabled in the backed-up VM, then perform the steps below: Ensure the value of isanysnapshotfailed is set as false in /etc/azure/vmbackup.conf
4. Schedule Azure Site Recovery at a different time, so it doesn't conflict the backup operation.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
