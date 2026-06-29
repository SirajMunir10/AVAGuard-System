# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to retrieve more than 50 records from the Windows Autopilot deployment report or AutopilotEvents Graph API?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Intune 2411 release or later

## Symptoms
- Windows Autopilot deployment report only shows 50 records at a time
- AutopilotEvents Microsoft Graph API only returns 50 records at a time

## Error Codes
N/A

## Root Causes
1. In Intune's 2411 release, the backend infrastructure of the Windows Autopilot deployment report was updated for consistency with other Intune reports, limiting results to 50 records per page

## Remediation Steps
1. Use the skipToken parameter to get additional pages of data with the Windows AutopilotEvents Graph API
2. Use the export API with reportName AutopilotV1DeploymentStatus to get all records

## Validation
1. Run the following Graph API query to confirm pagination works: GET https://graph.microsoft.com/beta/deviceManagement/autopilotEvents?$top=50&$skipToken={skipToken}. Verify that the response includes a '@odata.nextLink' property with a new skipToken value, indicating additional pages are available. 2. Execute the export API: POST https://graph.microsoft.com/beta/deviceManagement/reports/exportJobs with JSON body {"reportName": "AutopilotV1DeploymentStatus", "localization": "en-US"}. Confirm the response contains an 'id' and 'status' property. 3. Poll the export job status using GET https://graph.microsoft.com/beta/deviceManagement/reports/exportJobs/{exportJobId} until 'status' is 'completed'. Then download the report using the 'url' property and verify it contains more than 50 records.

## Rollback
1. If pagination fails, revert to the previous method of using the AutopilotEvents API without the skipToken parameter: GET https://graph.microsoft.com/beta/deviceManagement/autopilotEvents?$top=50. 2. If the export API fails, stop polling the export job and delete the export job if created: DELETE https://graph.microsoft.com/beta/deviceManagement/reports/exportJobs/{exportJobId}. 3. If both methods fail, contact Microsoft Support and reference the Intune 2411 release known issue documented at https://learn.microsoft.com/en-us/mem/autopilot/known-issues.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
