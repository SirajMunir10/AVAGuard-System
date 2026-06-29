# Troubleshooting: Azure Backup (ExtensionStuckInDeletionState)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ExtensionStuckInDeletionState error when Azure VM backup fails?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Backup operation fails
- Extension state is not supportive to the backup operation

## Error Codes
- `ExtensionStuckInDeletionState`

## Root Causes
1. Inconsistent state of Backup Extension

## Remediation Steps
1. Ensure Guest Agent is installed and responsive
2. From the Azure portal, go to Virtual Machine > All Settings > Extensions
3. Select the backup extension VmSnapshot or VmSnapshotLinux and select Uninstall
4. After deleting backup extension, retry the backup operation
5. The subsequent backup operation will install the new extension in the desired state

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
