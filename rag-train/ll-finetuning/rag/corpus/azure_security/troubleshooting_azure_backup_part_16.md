# Troubleshooting: Azure Backup (ExtensionSnapshotBitlockerError)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ExtensionSnapshotBitlockerError when taking a VM backup in Azure Backup?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The snapshot operation failed with the Volume Shadow Copy Service (VSS) operation error
- Error message: This drive is locked by BitLocker Drive Encryption. You must unlock this drive from the Control Panel.

## Error Codes
- `ExtensionSnapshotBitlockerError`

## Root Causes
1. BitLocker Drive Encryption is enabled on the VM drives, preventing VSS snapshot operations.

## Remediation Steps
1. Turn off BitLocker for all drives on the VM
2. Check if the VSS issue is resolved

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
