# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure macOS devices with Enterprise SSO plugin for Conditional Access in Google Chrome?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policies on macOS devices using Google Chrome

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. macOS devices using the Enterprise SSO plugin require the Microsoft Single Sign On extension to support SSO and device-based Conditional Access in Google Chrome.
2. For MDM based deployments of Google Chrome and extension management, refer to Set up Chrome browser on Mac and ExtensionInstallForcelist.

## Validation
1. Verify that the Microsoft Single Sign On extension is installed and enabled in Google Chrome on a test macOS device. Navigate to chrome://extensions and confirm the extension appears with status 'Enabled'.
2. Sign in to a test user account in Chrome and navigate to a resource protected by a Conditional Access policy (e.g., https://portal.office.com).
3. Confirm that the user is prompted for device compliance or SSO authentication without additional credential prompts.
4. In the Entra ID sign-in logs, locate the sign-in event for the test user and verify that the 'Conditional Access' tab shows the policy was applied and the device is marked as compliant.

## Rollback
1. If the Enterprise SSO plugin causes issues, remove the Microsoft Single Sign On extension from Chrome by navigating to chrome://extensions, clicking 'Remove' on the extension.
2. For MDM-managed devices, update the ExtensionInstallForcelist policy to remove the extension ID for the Microsoft Single Sign On extension, then force a policy refresh on the device.
3. Clear Chrome browser cache and restart the browser to ensure the extension is fully removed.
4. Verify that users can still access resources without the extension, and adjust Conditional Access policies to exclude macOS devices if necessary.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
