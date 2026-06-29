# Troubleshooting: Azure Backup (UserErrorMigrationFromTrustedLaunchVMToNonTrustedVMNotAllowed)

**Domain:** Azure
**Subdomain:** Azure Backup
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve backup configuration failure for a VM that migrated from Trusted Launch mode to non-Trusted Launch mode?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Backup cannot be configured for the VM which has migrated from Trusted Launch mode to non Trusted Launch mode

## Error Codes
- `UserErrorMigrationFromTrustedLaunchVMToNonTrustedVMNotAllowed`

## Root Causes
1. Migration of Trusted Launch VM to Generation 2 VM is blocked because the VM Guest State (VMGS) blob created for Trusted Launch VMs isn't present for Generation 2 VM, so the VM won't start.
2. Unable to protect a Standard VM with the same name as of Trusted Launch VM that was previously deleted.

## Remediation Steps
1. Disable soft delete.
2. Stop VM protection with delete backup data.
3. Re-enable soft delete.
4. Configure VM protection again with the appropriate policy after the old backup data deletion is complete from the Recovery Services vault.
5. Alternatively, create a VM with a different name than the original one, or in a different resource group with the same name.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-troubleshoot>
