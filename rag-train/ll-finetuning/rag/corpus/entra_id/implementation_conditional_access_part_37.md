# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure Chrome on Windows 10 Creators Update (version 1703) or later for device-based Conditional Access?

## Environment Context
- **Tenant Type:** Entra ID tenant with device-based Conditional Access
- **Configuration:** Chrome browser on Windows 10 version 1703 or later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Install the Microsoft Single Sign On extension
2. Or enable Chrome's CloudApAuthEnabled

## Validation
1. Verify that the Microsoft Single Sign On extension is installed in Chrome by navigating to chrome://extensions and confirming the extension is listed and enabled. 2. Alternatively, if using CloudApAuthEnabled, open Chrome policy management (e.g., via Group Policy or registry) and confirm that the registry key HKLM\Software\Policies\Google\Chrome\CloudApAuthEnabled is set to 1. 3. Sign in to a test user account in Chrome on the Windows 10 device and access a resource protected by device-based Conditional Access (e.g., https://portal.azure.com). Confirm that the user is prompted for device authentication and access is granted without errors.

## Rollback
1. Remove the Microsoft Single Sign On extension by navigating to chrome://extensions, clicking 'Remove' on the extension. 2. If CloudApAuthEnabled was enabled, set the registry key HKLM\Software\Policies\Google\Chrome\CloudApAuthEnabled to 0 or delete the key. 3. Clear Chrome browser cache and restart the browser. 4. Test that device-based Conditional Access now fails as expected (e.g., user is prompted for additional authentication or access is blocked).

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
