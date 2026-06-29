# Troubleshooting: Azure Backup (380008)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Azure VM backup failure with error code 380008 (AzureVmOffline) indicating the VM is not running?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Azure VM with Recovery Services extension

## Symptoms
- Failed to install Microsoft Recovery Services extension
- Virtual machine is not running

## Error Codes
- `380008`
- `AzureVmOffline`

## Root Causes
1. VM Agent is not installed or not running
2. VM is in a stopped/deallocated state

## Remediation Steps
1. Install the Azure Virtual Machine Agent
2. Restart the registration operation
3. Check if the VM Agent is installed correctly
4. Make sure that the flag on the VM config is set correctly

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
