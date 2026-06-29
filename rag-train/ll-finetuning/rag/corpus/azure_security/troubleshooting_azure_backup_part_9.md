# Troubleshooting: Azure Backup (UserErrorSkuNotAvailable)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve VM restore failure due to unsupported VM size (UserErrorSkuNotAvailable)?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- VM creation failed during restore operation

## Error Codes
- `UserErrorSkuNotAvailable`

## Root Causes
1. VM size selected during the restore operation is an unsupported size

## Remediation Steps
1. Use the restore disks option during the restore operation
2. Use those disks to create a VM from the list of available supported VM sizes using PowerShell cmdlets

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
