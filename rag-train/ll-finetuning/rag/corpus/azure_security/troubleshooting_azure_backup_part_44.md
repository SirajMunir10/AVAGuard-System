# Troubleshooting: Azure Backup

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot VM snapshot issues during Azure VM backup?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Backup job fails due to snapshot task failure
- Snapshot task is queued and delayed
- Snapshot task times out

## Error Codes
N/A

## Root Causes
1. Lack of storage access or delays during a snapshot task run
2. VMs with SQL Server configured can experience snapshot delays when Azure VM Backup interacts with the SQL Server VSS Writer
3. VM runs at high memory or CPU usage, more than 90 percent, causing snapshot task to be queued and delayed

## Remediation Steps
1. For Windows VMs running SQL Server, if you explicitly require a VSS Full (Non-Copy-Only) backup, configure the following registry key on the Windows VM: REG ADD "HKLM\SOFTWARE\Microsoft\BcdrAgent" /v UseVssFullBackup /t REG_SZ /d True /f
2. If the VM status is reported incorrectly because the VM is shut down in RDP, use the Shutdown option in the portal VM dashboard to shut down the VM
3. If the VM runs at high CPU or memory usage, try an on-demand backup

## Validation
1. Verify the registry key was set correctly: Run `reg query "HKLM\SOFTWARE\Microsoft\BcdrAgent" /v UseVssFullBackup` on the Windows VM. Confirm the value is `True`.
2. For VM shutdown issue: In the Azure portal, navigate to the VM's Overview blade, click 'Stop', then start the VM again. Check the VM status shows 'Running'.
3. For high CPU/memory: Trigger an on-demand backup from the Azure portal (Backup center > Backup Instances > select VM > Backup Now). Monitor the job in Backup Jobs to ensure it completes without snapshot delays.

## Rollback
1. If the registry key causes issues, delete it: `reg delete "HKLM\SOFTWARE\Microsoft\BcdrAgent" /v UseVssFullBackup /f`.
2. If the VM shutdown via portal fails, use Azure CLI: `az vm deallocate --resource-group <rg> --name <vm>` then `az vm start --resource-group <rg> --name <vm>`.
3. If on-demand backup fails, reduce VM load by scaling down or stopping non-essential services, then retry the backup.

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
