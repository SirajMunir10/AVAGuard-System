# Troubleshooting: Azure Backup (ExtensionFailedVssServiceInBadState)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ExtensionFailedVssServiceInBadState error during Azure VM backup?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Snapshot operation failed due to VSS (Volume Shadow Copy) service in bad state

## Error Codes
- `ExtensionFailedVssServiceInBadState`

## Root Causes
1. VSS service was in a bad state

## Remediation Steps
1. Restart VSS (Volume Shadow Copy) service. Navigate to Services.msc and restart 'Volume Shadow Copy service'.
2. Run the following commands from an elevated command prompt: net stop VSS net start VSS
3. If the issue still persists, restart the VM at the scheduled downtime.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
