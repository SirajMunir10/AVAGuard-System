# Troubleshooting: Azure Backup (UserErrorFsFreezeFailed)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve UserErrorFsFreezeFailed when Azure VM backup fails to freeze mount points for a file-system consistent snapshot?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Linux VM with Azure Backup extension

## Symptoms
- Failed to freeze one or more mount-points of the VM to take a file-system consistent snapshot

## Error Codes
- `UserErrorFsFreezeFailed`

## Root Causes
1. Mount points cannot be frozen due to file system state not cleaned
2. Duplicate mount points present

## Remediation Steps
1. Unmount the devices for which the file system state wasn't cleaned, using the umount command
2. Run a file system consistency check on these devices by using the fsck command
3. Mount the devices again and retry backup operation
4. If you can't un-mount the devices, update the VM backup configuration to ignore certain mount points by adding the MountsToSkip property in /etc/azure/vmbackup.conf
5. Check if there is the vmbackup.conf file under the /etc/azure/ directory
6. If there's no /etc/azure/vmbackup.conf, copy file from the /var/lib/waagent/Microsoft.Azure.RecoveryServices.VMSnapshotLinux-1.0.XXX.0/main/tempPlugin/vmbackup.conf
7. In the /etc/azure/vmbackup.conf file, add the following configuration: [SnapshotThread] fsfreeze: True MountsToSkip = /mnt/resource SafeFreezeWaitInSeconds=600
8. Check if there are duplicate mount points present. Identify the failed to freeze mount points from the extension log file
9. On the Linux VM execute 'mount' command and check if the failed mount points have multiple entries. If yes, remove the old entries or rename the mount path and retry the backup operation

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
