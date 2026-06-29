# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure unallowed browsers for Windows devices in Endpoint DLP to restrict file access based on executable names?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP policy with upload-to-cloud services restriction set to block or block override

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Specify the executable names of the web browsers to restrict on Windows devices.
2. Ensure the DLP policy's upload-to-cloud services restriction is set to block or block override.
3. When blocked, end users see a toast notification asking them to open the file through Microsoft Edge.

## Validation
1. Verify that the DLP policy is applied to the target Windows devices by running the following PowerShell command as an administrator on a test device: Get-MpPreference | Select-Object -ExpandProperty DlpPolicy. Confirm the policy GUID matches the one configured in the Purview compliance portal.
2. On a test Windows device, attempt to upload a sensitive file to an unallowed browser (e.g., Chrome.exe) from a cloud service (e.g., OneDrive). Confirm that the upload is blocked and a toast notification appears instructing the user to open the file through Microsoft Edge.
3. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies, select the relevant Endpoint DLP policy, and under 'Locations' confirm that 'Windows devices' is included. Under 'Settings', verify that 'Unallowed browsers' lists the specified executable names (e.g., chrome.exe, firefox.exe) and that 'Upload to cloud services' restriction is set to 'Block' or 'Block with override'.

## Rollback
1. In the Microsoft Purview compliance portal, go to Data Loss Prevention > Policies, select the relevant Endpoint DLP policy, and edit the policy settings.
2. Under 'Advanced Endpoint DLP settings', remove the executable names from the 'Unallowed browsers' list.
3. Change the 'Upload to cloud services' restriction from 'Block' or 'Block with override' to 'Audit only' or 'Allow' as needed.
4. Save the policy and wait for the changes to propagate (up to 24 hours).
5. On a test Windows device, verify that the previous blocking behavior is no longer present by attempting to upload a sensitive file to a previously restricted browser and confirming the upload succeeds or is only audited.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
