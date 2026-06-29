# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I export the timeline to a CSV file in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Export the timeline to a CSV file.
2. Export is limited to the first 5,000 records and contains the data as displayed in the UI (same filters and columns).

## Validation
1. Open the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Navigate to 'Incidents & alerts' > 'Incidents' and select the relevant incident.
3. Click the 'Timeline' tab.
4. Verify that the 'Export' button is available and click it.
5. Confirm that the exported CSV file contains the expected columns and data as displayed in the UI.
6. Check that the file includes no more than 5,000 records (if the timeline has more entries, only the first 5,000 are exported).
7. Open the CSV file in a text editor or spreadsheet application to ensure it is not corrupted and can be read.

## Rollback
1. If the export fails or produces an incorrect file, close the export dialog and refresh the timeline page.
2. Clear browser cache and cookies, then retry the export.
3. If the issue persists, verify that the user account has the necessary permissions (e.g., 'View data' or 'Manage security settings' roles) as per Microsoft documentation.
4. As a last resort, contact Microsoft support with the incident ID and timestamp of the failed export for further investigation.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
