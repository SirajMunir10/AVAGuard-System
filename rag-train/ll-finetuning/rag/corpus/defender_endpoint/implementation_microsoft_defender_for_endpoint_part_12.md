# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to download a file from a Defender for Endpoint alert?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Download file from the response actions
2. A flyout appears where you can record a reason for downloading the file, and set a password
3. By default, you should be able to download files that are in quarantine

## Validation
1. Navigate to Microsoft Defender for Endpoint portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Alerts and select the specific alert.
3. In the alert details page, under the 'Device' or 'File' tab, locate the file entry.
4. Click on the file name to open its file details page.
5. Verify that the 'Download file' action button is visible and enabled (not grayed out).
6. Click 'Download file' and confirm that a flyout appears prompting for a reason and password.
7. Enter a reason and a password, then submit. Confirm that the file download starts successfully.
8. Check the downloaded file is password-protected as expected.

## Rollback
1. If the download fails or the file is not available, verify the file is still in quarantine by checking its status on the file details page.
2. If the file is no longer in quarantine, re-initiate the download by selecting 'Download file' again, ensuring the file is still present in the alert.
3. If the file cannot be downloaded due to permission issues, confirm the user has the 'Manage settings' or 'Security operations' role assigned in Microsoft 365 Defender.
4. If the download action is missing, refresh the alert page or navigate back to the alert list and re-select the alert.
5. As a last resort, use the Advanced Hunting query to locate the file SHA1 and attempt download via API (if applicable) or contact support.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
