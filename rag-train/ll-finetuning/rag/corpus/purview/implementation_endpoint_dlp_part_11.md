# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure the Restricted apps list for Endpoint DLP on Windows 10/11 and macOS devices?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with Restricted apps list

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a custom list of applications for the Restricted apps list.
2. For Windows devices, include only the executable name (e.g., browser.exe), not the path to the executable.
3. Configure the action (audit, block with override, or block) for when a user uses an app on the list to access a DLP-protected file.
4. If an app on the Restricted apps list is also a member of a Restricted app group, note that the actions configured for activities in the Restricted app group override the actions configured for the Restricted apps list.
5. To exclude a path from enforcement, add it to the exclusion list (this path is where files identified in Activity Explorer are located).

## Validation
1. Verify that the custom Restricted apps list is applied by checking the Endpoint DLP policy configuration in the Microsoft Purview compliance portal: navigate to Data Loss Prevention > Policies, select the relevant policy, and under 'Locations' confirm that 'Devices' is selected and the policy includes the 'Restricted apps' settings. 2. On a Windows 10/11 test device, sign in with a user in scope, then attempt to open a DLP-protected file using an app that is on the Restricted apps list (e.g., browser.exe). Confirm that the configured action (audit, block with override, or block) is enforced. 3. On a macOS test device, perform the same test with the corresponding app. 4. Check Activity Explorer for events showing the restricted app activity and verify the action taken matches the policy configuration.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the relevant Endpoint DLP policy. 2. Under 'Locations', edit the 'Devices' settings and remove or modify the Restricted apps list entries that were added. 3. If the policy includes an exclusion path, remove that path from the exclusion list. 4. Save the policy changes and allow up to 1 hour for the changes to propagate to all devices. 5. On a test device, verify that the previously restricted app can now access DLP-protected files without the configured action being enforced.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
