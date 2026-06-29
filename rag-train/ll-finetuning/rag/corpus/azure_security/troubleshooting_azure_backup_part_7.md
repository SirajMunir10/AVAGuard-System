# Troubleshooting: Azure Backup (ExtensionFailedVssWriterInBadState)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Azure VM backup failure due to VSS writers being in a bad state (ExtensionFailedVssWriterInBadState)?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Snapshot operation failed because VSS writers were in a bad state

## Error Codes
- `ExtensionFailedVssWriterInBadState`

## Root Causes
1. VSS writers were in a bad state
2. VSS writers timing out due to limited IOPS

## Remediation Steps
1. Step 1: Check the Free Disk Space, VM resources as RAM and page file, and CPU utilization percentage. Increase the VM size to increase vCPUs and RAM space. Increase the disk size if the free disk space is low.
2. Step 2: Restart VSS writers that are in a bad state. From an elevated command prompt, run vssadmin list writers. The output contains all VSS writers and their state. For every VSS writer with a state that's not [1] Stable, restart the respective VSS writer's service. To restart the service, run the following commands from an elevated command prompt: net stop serviceName net start serviceName. Restarting some services can have an impact on your production environment. Ensure the approval process is followed and the service is restarted at the scheduled downtime.
3. Step 3: If restarting the VSS writers did not resolve the issue, then run the following command from an elevated command-prompt (as an administrator) to prevent the threads from being created for blob-snapshots: REG ADD "HKLM\SOFTWARE\Microsoft\BcdrAgentPersistentKeys" /v SnapshotWithoutThreads /t REG_SZ /d True /f
4. Step 4: If steps 1 and 2 did not resolve the issue, then the failure could be due to VSS writers timing out due to limited IOPS. To verify, navigate to System and Event Viewer Application logs and check for the following error message: The shadow copy provider timed out while holding writes to the volume being shadow copied. This is probably due to excessive activity on the volume by an application or a system service. Try again later when activity on the volume is reduced. Check for possibilities to distribute the load across the VM disks. This will reduce the load on single disks. You can check the IOPs throttling by enabling diagnostic metrics at storage level. Change the backup policy to perform backups during off peak hours, when the load on the VM is at its lowest. Upgrade the Azure disks to support higher IOPs.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
