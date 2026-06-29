# Troubleshooting: Jamf Pro Integration

**Domain:** Intune
**Subdomain:** Jamf Pro Integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Jamf Pro integration failure due to incorrect API permissions in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Jamf Pro integration
- **Configuration:** Jamf Pro enterprise application API permissions

## Symptoms
- Jamf Pro integration with Intune fails or does not work correctly

## Error Codes
N/A

## Root Causes
1. Jamf Pro enterprise application in Azure has the wrong permission or has more than one permission

## Remediation Steps
1. Review and if necessary correct the permissions for the Jamf app
2. Remove all default API permissions from the Jamf Pro enterprise application in Azure
3. Assign Intune a single permission of update_device_attributes

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) as a Global Administrator. 2. Navigate to 'Microsoft Entra ID' > 'Enterprise applications' > 'Jamf Pro' (or the name of your Jamf Pro enterprise application). 3. Under 'Manage', select 'API permissions'. 4. Verify that the only permission listed is 'update_device_attributes' under 'Microsoft Graph' (or 'Intune' depending on the API). 5. Confirm there are no other permissions (e.g., 'DeviceManagementManagedDevices.ReadWrite.All' or any default permissions). 6. In the Jamf Pro console, navigate to 'Settings' > 'Global Management' > 'Microsoft Intune Integration' and click 'Test Connection'. 7. Confirm the test returns a success message. 8. In Intune, go to 'Tenant administration' > 'Connectors and tokens' > 'Jamf Pro' and verify the connection status shows 'Active'.

## Rollback
1. Sign in to the Azure portal (https://portal.azure.com) as a Global Administrator. 2. Navigate to 'Microsoft Entra ID' > 'Enterprise applications' > 'Jamf Pro'. 3. Under 'Manage', select 'API permissions'. 4. Click 'Add a permission', then select 'Microsoft Graph' (or the appropriate API). 5. Add the previously removed permissions (e.g., 'DeviceManagementManagedDevices.ReadWrite.All' or any default permissions that were removed). 6. Click 'Grant admin consent for [tenant name]' to reapply consent. 7. In the Jamf Pro console, navigate to 'Settings' > 'Global Management' > 'Microsoft Intune Integration' and click 'Test Connection' to confirm the original failure state returns. 8. If the rollback is due to a failure, re-run the original remediation steps to ensure only 'update_device_attributes' is assigned.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
