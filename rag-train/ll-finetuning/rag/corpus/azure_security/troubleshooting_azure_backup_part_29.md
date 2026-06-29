# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
Disks appear offline after File Restore in Azure Backup

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Disks appear offline after restore

## Error Codes
N/A

## Root Causes
1. Machine where the script is executed does not meet OS requirements
2. Restoring to the same source

## Remediation Steps
1. Verify if the machine where the script is executed meets the OS requirements
2. Ensure you are not restoring to the same source

## Validation
1. On the target machine, run 'winver' to confirm the OS version matches the supported list for Azure Backup file restore (e.g., Windows Server 2012 R2 or later, Windows 10/11).
2. Run 'diskmgmt.msc' and verify that the restored disks appear as 'Online' and have a drive letter assigned.
3. Check the script execution path: ensure the restore script was run on a machine that is NOT the original source VM.
4. Run 'Get-Disk | Where-Object {$_.OperationalStatus -eq "Offline"}' in PowerShell to confirm no disks remain offline.

## Rollback
1. If disks remain offline, run 'Set-Disk -Number <DiskNumber> -IsOffline $false' in PowerShell to bring each disk online.
2. If the restore was performed to the same source VM, delete the restored disks from that VM and re-run the restore script on a different machine.
3. If the OS is unsupported, upgrade the machine to a supported version (e.g., Windows Server 2012 R2 or later) and re-run the restore script.
4. As a last resort, re-initiate the file restore from the Azure Backup vault, ensuring the target machine meets OS requirements and is not the original source.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
