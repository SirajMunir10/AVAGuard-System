# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure unallowed browsers for macOS devices in Endpoint DLP by adding the full file path?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP policy for macOS devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the macOS device, open Activity Monitor.
2. Find and double-click the process you want to restrict.
3. Choose the Open Files and Ports tab.
4. Make a note of the full path name, including the name of the app.
5. Add the full file path to the unallowed browsers list in the DLP policy.

## Validation
1. On the macOS device, open Activity Monitor and verify that the process you restricted is no longer listed as an active process. 2. Attempt to open the application using the full file path noted earlier; confirm that the application is blocked and a DLP policy notification is displayed. 3. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Endpoint DLP policy > Policy settings > Unallowed browsers and confirm the full file path appears in the list.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Endpoint DLP policy > Policy settings > Unallowed browsers. 2. Locate the full file path you added and remove it from the list. 3. On the macOS device, verify that the application can now be launched without restriction.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
