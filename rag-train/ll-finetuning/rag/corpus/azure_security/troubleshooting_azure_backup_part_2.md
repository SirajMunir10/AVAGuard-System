# Troubleshooting: Azure Backup (Event Viewer error 517)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to determine if Azure VM backup failure is due to Azure Backup or another backup solution?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Event log, Azure Backup, other backup products

## Symptoms
- Backup failures in Event log with entry Backup in event source or message
- Event Viewer error 517

## Error Codes
- `Event Viewer error 517`

## Root Causes
1. Another backup solution (e.g., Windows Server Backup) failing while Azure Backup works

## Remediation Steps
1. Check whether Azure IaaS VM Backup backups were successful, and whether a Restore Point was created with the desired snapshot type
2. If Azure Backup is working, then the issue is likely with another backup solution
3. If Azure Backup is failing, then look for the corresponding error code in the Common issues section

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
