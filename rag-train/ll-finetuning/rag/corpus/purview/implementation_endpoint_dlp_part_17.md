# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I find the full path of a macOS app to add it to the Restricted app activities list in Microsoft Purview Endpoint DLP?

## Environment Context
- **Tenant Type:** macOS
- **Configuration:** Endpoint DLP settings for macOS devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the macOS device, open Activity Monitor.
2. Find and double-click the process you want to restrict.
3. Select the Open Files and Ports tab.
4. Make a note of the full path name, including the name of the app. For example, /System/Applications/TextEdit.app/Contents/MacOS/TextEdit

## Validation
On the macOS device, open Terminal and run: `ls -la /System/Applications/TextEdit.app/Contents/MacOS/TextEdit` to confirm the full path exists. Then, in Microsoft Purview compliance portal, navigate to Endpoint DLP > Device settings > Restricted app activities, add the path `/System/Applications/TextEdit.app/Contents/MacOS/TextEdit`, and save. Verify the app appears in the restricted list and that a DLP policy with this restriction is enforced by attempting to copy sensitive data via TextEdit and confirming the action is blocked.

## Rollback
In Microsoft Purview compliance portal, go to Endpoint DLP > Device settings > Restricted app activities, locate the added path `/System/Applications/TextEdit.app/Contents/MacOS/TextEdit`, and remove it. Save the settings. If the DLP policy was updated to include this restriction, revert the policy to its previous state. On the macOS device, no changes were made to the file system, so no additional rollback is needed.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
