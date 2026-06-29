# Troubleshooting: Microsoft Entra Connect Sync

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect Sync
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot synchronization errors when identity data is synced from Windows Server Active Directory to Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra tenant
- **Configuration:** Microsoft Entra Connect (August 2016 or higher)

## Symptoms
- Errors during export to Microsoft Entra ID
- Errors during Import, Synchronization, or Export operations

## Error Codes
N/A

## Root Causes
1. Identity data synced from Windows Server Active Directory to Microsoft Entra ID

## Remediation Steps
1. Review the Synchronization Errors Report in the Microsoft Entra admin center as part of Microsoft Entra Connect Health for sync
2. Refer to End-to-end troubleshooting of Microsoft Entra Connect objects and attributes
3. Refer to the User Provisioning and Synchronization section under the Microsoft Entra troubleshooting documentation

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Hybrid Identity Administrator. 2. Navigate to 'Health' > 'Sync Errors' under 'Microsoft Entra Connect Health'. 3. Confirm that the 'Synchronization Errors Report' shows zero export, import, or synchronization errors for the last 24 hours. 4. Run the following PowerShell command on the Microsoft Entra Connect server as an administrator: `Get-ADSyncExportError -ErrorAction Stop`. Verify that no export errors are returned. 5. Run `Get-ADSyncImportError -ErrorAction Stop` and confirm no import errors are returned. 6. Run `Get-ADSyncScheduler -ErrorAction Stop` and verify that the last sync cycle completed successfully (LastSyncCycleResult = 'Success').

## Rollback
1. If the remediation introduced new errors, restore the previous synchronization configuration by running the Microsoft Entra Connect wizard and selecting 'Customize synchronization options' to revert attribute mappings or filtering. 2. If errors persist, use the 'Restore from backup' option in the Microsoft Entra Connect wizard to revert to a previous configuration backup. 3. As a last resort, uninstall Microsoft Entra Connect and reinstall it using the original settings, ensuring to select 'Staging mode' initially to validate synchronization before enabling full sync. 4. For detailed rollback steps, refer to the official documentation: 'End-to-end troubleshooting of Microsoft Entra Connect objects and attributes' at https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
