# Troubleshooting: App Installation

**Domain:** Intune
**Subdomain:** App Installation
**Incident Type:** Troubleshooting

## Scenario / Query
User Group targeted app installation does not reach device

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** App deployed with Available intent; Windows BYOD devices require Work account; iOS/iPadOS ADE devices

## Symptoms
- App does not display in the Company Portal

## Error Codes
N/A

## Root Causes
1. App not deployed with Available intent
2. User accessing Company Portal with unsupported device type
3. Windows BYOD device missing Work account
4. User over Microsoft Entra device limit
5. iOS/iPadOS ADE device user not listed as Enrolled by User

## Remediation Steps
1. Ensure the app is deployed with Available intent and that the user is accessing the Company Portal with the device type supported by the app
2. For Windows BYOD devices, the user needs to add a Work account to the device
3. Navigate to Microsoft Entra Device Settings. Make note of the value set for Maximum devices per user. Navigate to Microsoft Entra users. Select the affected user and click Devices. If user is over the set limit then delete any stale records that are no longer needed
4. For iOS/iPadOS ADE devices, ensure that the user is listed as Enrolled by User in the Intune devices Overview pane. If it shows NA, then deploy a config policy for the Intune Company Portal

## Validation
1. Verify the app deployment intent: In Microsoft Intune, navigate to Apps > All apps, select the app, then click Properties. Under Assignments, confirm the intent is set to 'Available for enrolled devices' for the target user group.
2. Check user device type: In Company Portal, confirm the device type (Windows, iOS/iPadOS) matches the app's supported platform.
3. For Windows BYOD devices: Open Settings > Accounts > Access work or school. Verify a Work account is added and connected to the organization.
4. Check Microsoft Entra device limit: In Microsoft Entra admin center, go to Devices > Device Settings, note 'Maximum devices per user'. Then go to Users, select the affected user, click Devices, and count the devices. Ensure the count is below the limit.
5. For iOS/iPadOS ADE devices: In Intune, go to Devices > All devices, select the device, and in the Overview pane check the 'Enrolled by User' field. Confirm it shows a user name, not 'NA'.

## Rollback
1. If app intent was incorrectly changed: Revert the assignment intent to the original setting (e.g., 'Required' or 'Uninstall') under Apps > All apps > [App] > Properties > Assignments.
2. If a Work account was added incorrectly: On the Windows device, go to Settings > Accounts > Access work or school, select the account, and click Disconnect.
3. If stale device records were deleted in error: In Microsoft Entra admin center, go to Devices > All devices, click New device, and re-register the device using its original details (if available). Alternatively, have the user re-enroll the device.
4. If a Company Portal configuration policy was deployed incorrectly: In Intune, go to Apps > App configuration policies, select the policy, and delete or disable it. Then redeploy the correct policy as needed.

## References
- <https://learn.microsoft.com/en-us/mem/intune/apps/troubleshoot-app-install>
