# Troubleshooting: Jamf Integration

**Domain:** Intune
**Subdomain:** Jamf Integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the error 'Unable to connect to Microsoft Intune. Check your Microsoft Intune Integration configuration' due to expired Jamf license?

## Environment Context
- **Tenant Type:** Microsoft Intune with Jamf integration
- **Configuration:** Jamf Pro integration with Microsoft Intune

## Symptoms
- Unable to connect to Microsoft Intune. Check your Microsoft Intune Integration configuration.

## Error Codes
N/A

## Root Causes
1. Lack of a valid Intune or Jamf license
2. Jamf license is expired

## Remediation Steps
1. Contact Jamf for assistance to obtain a new license for Jamf.
2. Assign the user a valid Intune license or contact Microsoft or your Partner for information about how to obtain a current license.

## Validation
1. In Jamf Pro, navigate to Settings > Global Management > Microsoft Intune Integration and verify the connection status shows 'Connected'.
2. In Microsoft Intune admin center, go to Tenant administration > Connectors and tokens > Microsoft Intune for Jamf and confirm the status is 'Active'.
3. Run the Jamf Pro test connection: curl -X GET 'https://your-jamf-instance.jamfcloud.com/api/v1/intune/integration/status' -H 'Authorization: Bearer <token>' and verify response includes 'connected': true.
4. Check the Intune license assignment for the user: Get-AzureADUser -ObjectId <userUPN> | Select-Object -ExpandProperty AssignedLicenses in Microsoft Graph PowerShell.

## Rollback
1. If the new Jamf license causes issues, contact Jamf support to revert to the previous license key and re-enter it in Jamf Pro under Settings > Global Management > Microsoft Intune Integration.
2. If Intune license assignment causes problems, remove the newly assigned Intune license from the user: Set-MgUserLicense -UserId <userUPN> -RemoveLicenses @('<SkuId>') in Microsoft Graph PowerShell.
3. Re-run the Jamf Pro test connection to confirm the original error returns, indicating rollback to the previous state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
