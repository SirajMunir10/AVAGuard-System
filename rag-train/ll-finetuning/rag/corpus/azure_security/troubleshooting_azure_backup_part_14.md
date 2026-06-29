# Troubleshooting: Azure Backup (320001)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Azure Backup errors 320001 (ResourceNotFound) and 400094 (BCMV2VMNotFound) when the primary VM is deleted?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Azure Backup policy configured for a VM that has been deleted

## Symptoms
- Backup job fails with error code 320001 or 400094
- Error message: Could not perform the operation as VM no longer exists
- Error message: The virtual machine doesn't exist

## Error Codes
- `320001`
- `400094`

## Root Causes
1. The primary VM is deleted, but the backup policy still looks for a VM to back up

## Remediation Steps
1. Re-create the virtual machine with the same name and same resource group name
2. Stop protecting the virtual machine with or without deleting the backup data

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
