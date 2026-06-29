# Troubleshooting: Hybrid Identity (InvalidHardMatch)

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot and resolve InvalidHardMatch errors during Microsoft Entra Connect synchronization when BlockCloudObjectTakeoverThroughHardMatchEnabled is enabled?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with hybrid identity
- **Configuration:** BlockCloudObjectTakeoverThroughHardMatchEnabled feature enabled

## Symptoms
- InvalidHardMatch error during synchronization
- Attempt to hard match objects present in Microsoft Entra ID with a new incoming object that have the same sourceAnchor value fails

## Error Codes
- `InvalidHardMatch`

## Root Causes
1. BlockCloudObjectTakeoverThroughHardMatchEnabled feature is enabled on the tenant
2. Existing Microsoft Entra object has privileged roles assigned and contains an OnPremisesImmutableId value
3. DirSync is re-enabled on the tenant and objects with the same sourceAnchor are synchronized again, but BlockCloudObjectTakeoverThroughHardMatchEnabled feature is enabled
4. User was excluded from sync scope and restored from Microsoft Entra ID Recycle Bin, then re-added to sync scope, but BlockCloudObjectTakeoverThroughHardMatchEnabled feature is enabled
5. A soft-deleted synced Microsoft Entra user with privileged roles assigned is blocked from hard match during restore operations
6. An on-premises Active Directory user attempts to hard match with an existing Microsoft Entra user that has administrative roles assigned and an OnPremisesImmutableId value

## Remediation Steps
1. We advise customers to enable BlockCloudObjectTakeoverThroughHardMatchEnabled unless they need it to take over existent accounts in Microsoft Entra ID

## Validation
1. Run the Microsoft Entra Connect synchronization cycle and check the Synchronization Service Manager for any new InvalidHardMatch errors. 2. Use the Microsoft Graph PowerShell command: Get-MgDirectorySetting | Where-Object {$_.DisplayName -eq 'BlockCloudObjectTakeoverThroughHardMatchEnabled'} to confirm the feature is enabled. 3. Verify that the affected user objects in Microsoft Entra ID no longer have the OnPremisesImmutableId attribute set by running: Get-MgUser -UserId <userPrincipalName> | Select-Object OnPremisesImmutableId. 4. Confirm that no privileged roles are assigned to the affected user objects by running: Get-MgUserMemberOf -UserId <userPrincipalName>.

## Rollback
1. Disable the BlockCloudObjectTakeoverThroughHardMatchEnabled feature by running: Update-MgDirectorySetting -DirectorySettingId <settingId> -Values @{BlockCloudObjectTakeoverThroughHardMatchEnabled = $false}. 2. If the feature was enabled to prevent takeover, re-enable it after resolving the conflict by running: Update-MgDirectorySetting -DirectorySettingId <settingId> -Values @{BlockCloudObjectTakeoverThroughHardMatchEnabled = $true}. 3. If the conflict was due to a soft-deleted user, restore the user from the Microsoft Entra ID Recycle Bin using: Restore-MgDirectoryDeletedItem -DirectoryObjectId <objectId>. 4. Re-run the Microsoft Entra Connect synchronization cycle to allow the hard match to proceed.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
