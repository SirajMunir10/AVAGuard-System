# Troubleshooting: Azure Backup (UserErrorVmNotInDesirableState)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve backup failure when VM is in a Failed state?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Backup operation failed
- VM is in Failed state

## Error Codes
- `UserErrorVmNotInDesirableState`

## Root Causes
1. VM is in Failed state
2. VM is in a transient state between Running and Shut down
3. Linux VM with Security-Enhanced Linux kernel module blocking Azure Linux Agent path

## Remediation Steps
1. Wait for the VM state to change to Running, Stopped, or Stopped (deallocated)
2. Trigger the backup job after state change
3. If the VM is a Linux VM and uses the Security-Enhanced Linux kernel module, exclude the Azure Linux Agent path /var/lib/waagent from the security policy
4. Make sure the Backup extension is installed

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
