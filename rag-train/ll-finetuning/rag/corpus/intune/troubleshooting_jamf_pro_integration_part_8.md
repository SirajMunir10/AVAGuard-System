# Troubleshooting: Jamf Pro Integration (Could not retrieve the access token for Microsoft Graph API)

**Domain:** Intune
**Subdomain:** Jamf Pro Integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the error 'Could not retrieve the access token for Microsoft Graph API' when integrating Jamf Pro with Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune with Jamf Pro integration
- **Configuration:** Microsoft Intune Integration configuration in Jamf Pro

## Symptoms
- Error message: Could not retrieve the access token for Microsoft Graph API. Check the configuration for Microsoft Intune Integration.

## Error Codes
- `Could not retrieve the access token for Microsoft Graph API`

## Root Causes
1. The source of this error can be one of the following causes: (specific causes not listed in excerpt)

## Remediation Steps
N/A

## Validation
1. In Jamf Pro, navigate to Settings > Global Management > Microsoft Intune Integration. 2. Verify that the 'Tenant Name' field contains the correct Azure AD tenant ID (not the tenant name). 3. Confirm that the 'Client ID' and 'Client Secret' values match the application registration in Azure AD. 4. In the Azure portal, go to Azure Active Directory > App registrations, select the Jamf Pro enterprise application, and ensure the 'Client credentials' (client ID and secret) are valid and not expired. 5. Under 'Certificates & secrets', verify that the client secret has not expired and that the application has the required API permissions (e.g., Microsoft Graph API permissions for 'DeviceManagementManagedDevices.ReadWrite.All' and 'DeviceManagementServiceConfig.ReadWrite.All'). 6. In Jamf Pro, click 'Test Connection' to confirm the integration can retrieve an access token. 7. Check the Jamf Pro logs for any subsequent errors related to token retrieval.

## Rollback
1. If the validation fails or the integration breaks, revert any changes made to the Jamf Pro Microsoft Intune Integration configuration by restoring the previous tenant name, client ID, and client secret values. 2. If a new client secret was generated in Azure AD, re-enter the original client secret in Jamf Pro. 3. If API permissions were modified, reset them to the previous state (e.g., remove any newly added permissions and re-add any removed ones). 4. In Azure AD, if the application registration was altered, restore it from a backup or re-register the Jamf Pro enterprise application using the original settings. 5. After reverting, repeat the validation steps to confirm the integration is working again. 6. If the issue persists, contact Microsoft Support with the error details and the steps taken.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
