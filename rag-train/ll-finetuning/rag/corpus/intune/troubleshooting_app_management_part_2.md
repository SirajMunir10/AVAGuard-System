# Troubleshooting: App Management

**Domain:** Intune
**Subdomain:** App Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to get app troubleshooting details for a specific user's device in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Microsoft Intune admin center

## Symptoms
- App installation failure for a required app

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Intune admin center.
2. Select Troubleshoot + support.
3. Click Select user to go to the Select users pane.
4. Type the name or email address of the user you want to troubleshoot, and then click Select at the bottom of the pane.
5. Select the device that you want to troubleshoot from the Devices list.
6. Select Managed Apps from selected device pane.
7. Select an app from the list where Installation Status indicates a failure.
8. If an installation failure occurs for a required app, either you or your help desk will be able to sync the device and retry the app install.

## Validation
1. Sign in to the Microsoft Intune admin center. 2. Navigate to Troubleshoot + support. 3. Click Select user and enter the user's name or email address, then click Select. 4. From the Devices list, select the device that was previously failing. 5. In the selected device pane, select Managed Apps. 6. Verify that the previously failing app now shows an Installation Status of 'Installed' or 'Success'. 7. Optionally, confirm the app appears in the user's device app inventory or that the user can launch the app successfully.

## Rollback
1. Sign in to the Microsoft Intune admin center. 2. Navigate to Apps > All apps and select the problematic app. 3. Under Manage, select Assignments and remove the user or device assignment that caused the required app installation. 4. Alternatively, if the app was assigned via a group, remove the device or user from that group in Azure AD. 5. To revert a sync action, no direct rollback exists; instead, wait for the next scheduled Intune sync or instruct the user to manually sync from the Company Portal app to reset the retry state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/apps/troubleshoot-app-install>
