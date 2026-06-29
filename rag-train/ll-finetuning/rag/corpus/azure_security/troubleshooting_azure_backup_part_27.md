# Troubleshooting: Azure Backup (UserErrorUnableToOpenMount)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve backup failures due to the backup extension being unable to open mount points on an Azure VM?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Backups failed because the backup extensions on the VM were unable to open the mount points in the VM

## Error Codes
- `UserErrorUnableToOpenMount`

## Root Causes
1. The backup extension on the VM was unable to open the mount points in the VM

## Remediation Steps
1. Ensure that all mount points are accessible

## Validation
1. Connect to the VM via RDP or SSH. 2. Run 'mountvol' (Windows) or 'mount' (Linux) to list all mount points. 3. Verify each mount point is accessible by attempting to read from it (e.g., 'dir' on Windows, 'ls' on Linux). 4. Check the Backup extension logs at C:\WindowsAzure\Logs\Plugins\Microsoft.Azure.RecoveryServices.VMSnapshot\* (Windows) or /var/log/azure/ (Linux) for any 'UserErrorUnableToOpenMount' errors. 5. Trigger an on-demand backup from the Azure portal and confirm it completes successfully.

## Rollback
1. If a mount point was unmounted or changed, remount it to its original path using the original configuration (e.g., 'mountvol X: /d' then 'mountvol X: \\Volume{GUID}\' on Windows, or 'mount -a' on Linux). 2. Restore any modified permissions on the mount point to their original state. 3. Restart the Backup extension service: on Windows, run 'net stop WindowsAzureGuestAgent' then 'net start WindowsAzureGuestAgent'; on Linux, run 'systemctl restart waagent'. 4. Re-run the on-demand backup to verify the issue is resolved or reverted.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
