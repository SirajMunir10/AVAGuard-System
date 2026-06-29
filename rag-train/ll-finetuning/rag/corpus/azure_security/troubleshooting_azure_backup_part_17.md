# Troubleshooting: Azure Backup (VmNotInDesirableState)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the VmNotInDesirableState error when backing up an Azure VM?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The VM isn't in a state that allows backups

## Error Codes
- `VmNotInDesirableState`

## Root Causes
1. The VM is in a transient state between Running and Shut down
2. The VM is a Linux VM using the Security-Enhanced Linux kernel module and the Azure Linux Agent path /var/lib/waagent is not excluded from the security policy
3. The VM Agent isn't present on the virtual machine

## Remediation Steps
1. If the VM is in a transient state between Running and Shut down, wait for the state to change, then trigger the backup job.
2. If the VM is a Linux VM and uses the Security-Enhanced Linux kernel module, exclude the Azure Linux Agent path /var/lib/waagent from the security policy and make sure the Backup extension is installed.
3. If the VM Agent isn't present on the virtual machine, install any prerequisite and the VM Agent, then restart the operation.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
