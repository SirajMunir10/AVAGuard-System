# Troubleshooting: Jamf Pro integration

**Domain:** Intune
**Subdomain:** Jamf Pro integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Jamf Pro integration issues with Intune on macOS devices by cleaning up stale files and keychain entries?

## Environment Context
- **Tenant Type:** Intune-managed macOS devices with Jamf Pro
- **Configuration:** Jamf Pro integration with Intune

## Symptoms
- Device enrollment or compliance issues with Jamf Pro and Intune on macOS

## Error Codes
N/A

## Root Causes
1. Stale files or keychain entries from previous enrollment or authentication attempts

## Remediation Steps
1. Delete the following files on the device if they exist: /Library/Application Support/com.microsoft.CompanyPortal.usercontext.info, /Library/Application Support/com.microsoft.CompanyPortal, /Library/Application Support/com.jamfsoftware.selfservice.mac, /Library/Saved Application State/com.jamfsoftware.selfservice.mac.savedState, /Library/Saved Application State/com.microsoft.CompanyPortal.savedState, /Library/Preferences/com.microsoft.CompanyPortal.plist, /Library/Preferences/com.jamfsoftware.selfservice.mac.plist, /Library/Preferences/com.jamfsoftware.management.jamfAAD.plist, /Users/<username>/Library/Cookies/com.microsoft.CompanyPortal.binarycookies, /Users/<username>/Library/Cookies/com.jamf.management.jamfAAD.binarycookies, com.microsoft.CompanyPortal, com.microsoft.CompanyPortal.HockeySDK, enterpriseregistration.windows.net, https://device.login.microsoftonline.com, https://device.login.microsoftonline.com/, Microsoft Session Transport Key (public AND private keys), Microsoft Workplace Join Key (public AND private keys)
2. Remove anything from the keychain on the device that references Microsoft, Intune, or Company Portal, including DeviceLogin.microsoft.com certificates
3. Remove JAMF references except for JAMF public and private key

## Validation
1. Verify that the following files no longer exist on the device: /Library/Application Support/com.microsoft.CompanyPortal.usercontext.info, /Library/Application Support/com.microsoft.CompanyPortal, /Library/Application Support/com.jamfsoftware.selfservice.mac, /Library/Saved Application State/com.jamfsoftware.selfservice.mac.savedState, /Library/Saved Application State/com.microsoft.CompanyPortal.savedState, /Library/Preferences/com.microsoft.CompanyPortal.plist, /Library/Preferences/com.jamfsoftware.selfservice.mac.plist, /Library/Preferences/com.jamfsoftware.management.jamfAAD.plist, /Users/<username>/Library/Cookies/com.microsoft.CompanyPortal.binarycookies, /Users/<username>/Library/Cookies/com.jamf.management.jamfAAD.binarycookies. 2. Open Keychain Access and confirm that entries referencing Microsoft, Intune, Company Portal, DeviceLogin.microsoft.com certificates, Microsoft Session Transport Key (public and private), and Microsoft Workplace Join Key (public and private) are removed. 3. Confirm that JAMF public and private keys remain in the keychain, but other JAMF references are removed. 4. Re-enroll the device via Jamf Pro and verify that the device appears as compliant in Intune without errors.

## Rollback
1. Restore deleted files from backup if available, or reinstall Company Portal and Jamf Self Service to regenerate default files. 2. Re-add keychain entries by re-enrolling the device in Intune and Jamf Pro, which will recreate necessary certificates and keys. 3. If JAMF public or private keys were accidentally removed, re-enroll the device in Jamf Pro to regenerate them. 4. If issues persist, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
