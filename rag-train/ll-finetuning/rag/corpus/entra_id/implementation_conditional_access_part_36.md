# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure macOS devices using Firefox browser for device-based Conditional Access?

## Environment Context
- **Tenant Type:** Entra ID tenant with device-based Conditional Access
- **Configuration:** Firefox browser on macOS version 10.15 or newer

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure macOS version is 10.15 or newer
2. Install and configure the Microsoft Enterprise SSO plug-in appropriately

## Validation
1. Verify macOS version: sw_vers -productVersion. Confirm it is 10.15 or newer.
2. Check that the Microsoft Enterprise SSO plug-in is installed: ls /Applications/ | grep -i 'Microsoft Enterprise SSO' or check in System Preferences > Profiles.
3. Confirm the plug-in is enabled in Firefox: In Firefox, navigate to about:addons, select Extensions, and verify 'Microsoft Single Sign On' is listed and enabled.
4. Test device-based Conditional Access: Sign in to a resource protected by a Conditional Access policy requiring compliant or domain-joined device from Firefox on macOS. Confirm access is granted and the device is recognized as compliant.

## Rollback
1. If macOS version is incompatible, upgrade to 10.15 or newer via Software Update.
2. If the Microsoft Enterprise SSO plug-in is not installed, download and install from Microsoft 365 admin center or Microsoft download page.
3. If the plug-in is disabled in Firefox, enable it from about:addons.
4. If device compliance is not recognized, re-register the device in Entra ID: Run 'sudo jamf recon' (if using Jamf) or manually re-enroll via Company Portal. If issues persist, remove and re-add the device in Entra ID.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
