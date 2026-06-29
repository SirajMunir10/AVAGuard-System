# Troubleshooting: Azure Backup (ExtensionFailedTimeoutVMNetworkUnresponsive)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ExtensionFailedTimeoutVMNetworkUnresponsive error when Azure VM backup fails due to snapshot operation timeout?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure VM Backup, Windows VM

## Symptoms
- Backup operation on the VM failed due to delay in network calls while performing the snapshot operation

## Error Codes
- `ExtensionFailedTimeoutVMNetworkUnresponsive`

## Root Causes
1. Snapshot operation failed due to inadequate VM resources

## Remediation Steps
1. Step 1: Create snapshot through Host. From an elevated (admin) command-prompt, run the following command: REG ADD "HKLM\SOFTWARE\Microsoft\BcdrAgentPersistentKeys" /v SnapshotMethod /t REG_SZ /d firstHostThenGuest /f
2. REG ADD "HKLM\SOFTWARE\Microsoft\BcdrAgentPersistentKeys" /v CalculateSnapshotTimeFromHost /t REG_SZ /d True /f
3. REG ADD "HKLM\SOFTWARE\Microsoft\BcdrAgentPersistentKeys" /v SnapshotMethod /t REG_SZ /d firstHostThenGuest /f
4. REG ADD "HKLM\SOFTWARE\Microsoft\BcdrAgentPersistentKeys" /v CalculateSnapshotTimeFromHost /t REG_SZ /d True /f
5. This will ensure the snapshots are taken through host instead of Guest. Retry the backup operation.
6. Step 2: Try changing the backup schedule to a time when the VM is under less load (like less CPU or IOPS)
7. Step 3: Try increasing the size of the VM and retry the operation

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
