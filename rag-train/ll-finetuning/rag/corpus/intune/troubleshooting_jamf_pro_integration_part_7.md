# Troubleshooting: JAMF Pro integration

**Domain:** Intune
**Subdomain:** JAMF Pro integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve JAMF Pro enrollment issues by clearing stale keychain entries and re-enrolling the Mac device?

## Environment Context
- **Tenant Type:** Intune with JAMF Pro
- **Configuration:** Mac device enrolled via JAMF Pro

## Symptoms
- Device enrollment failures
- Registration policy not starting

## Error Codes
N/A

## Root Causes
1. Stale keychain entries from previous enrollment

## Remediation Steps
1. Delete any of the following entries that you find: Kind: Application password ; Account: com.microsoft.workplacejoin.thumbprint
2. Delete any of the following entries that you find: Kind: Application password ; Account: com.microsoft.workplacejoin.registeredUserPrincipalName
3. Delete any of the following entries that you find: Kind: Certificate ; Issued by: MS-Organization-Access
4. Delete any of the following entries that you find: Kind: Identity preference ; Name (ADFS STS URL if present): https://<DNS NAME>.com/adfs/ls
5. Delete any of the following entries that you find: Kind: Identity preference ; Name: https://enterpriseregistration.windows.net
6. Delete any of the following entries that you find: Kind: Identity preference ; Name: https://enterpriseregistration.windows.net/
7. Restart the Mac device.
8. Uninstall Company Portal from the device.
9. Go to portal.manage.microsoft.com and delete out all the instances of the Mac device.
10. Wait at least 30 minutes before you go to the next step.
11. Re-enroll the device in JAMF Pro.
12. Reopen Self Service and start Registration policy.

## Validation
1. Verify that the stale keychain entries have been removed: open Keychain Access and search for 'com.microsoft.workplacejoin.thumbprint', 'com.microsoft.workplacejoin.registeredUserPrincipalName', 'MS-Organization-Access', and the ADFS STS URL (if applicable). Confirm none appear. 2. Confirm the device has restarted. 3. Confirm Company Portal is uninstalled (check Applications folder). 4. In the Microsoft Intune admin center (https://intune.microsoft.com), navigate to Devices > All devices, filter by the Mac device name, and verify no instances remain. 5. Wait at least 30 minutes. 6. Re-enroll the device in JAMF Pro and reopen Self Service. 7. Run the Registration policy and confirm it completes without errors. 8. Check the JAMF Pro console for a successful enrollment status and verify the device appears in Intune as compliant.

## Rollback
1. If keychain entries were accidentally deleted, restore them from a backup or re-enroll the device to regenerate them. 2. If the device was restarted prematurely, no rollback is needed; proceed with the remaining steps. 3. If Company Portal was uninstalled, reinstall it from the Mac App Store. 4. If device instances were deleted from portal.manage.microsoft.com, they cannot be restored; re-enrollment will create new entries. 5. If the 30-minute wait was skipped, wait the full duration before re-enrolling. 6. If re-enrollment fails, verify JAMF Pro connection settings in Intune (Tenant administration > Connectors and tokens > JAMF Pro) and ensure the JAMF Pro server is reachable. 7. If the Registration policy fails, check JAMF Pro logs and Intune enrollment logs for detailed errors, and ensure the device meets all prerequisites (macOS version, network access).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
