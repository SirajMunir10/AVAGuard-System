# Troubleshooting: App Management

**Domain:** Intune
**Subdomain:** App Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot app installation failures for Microsoft Intune-managed apps?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Managed Apps pane in Intune Troubleshoot portal

## Symptoms
- App installation failures for Intune-managed apps

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Intune Troubleshoot pane to view failure details, including details about managed apps, to address user help requests.
2. In the Managed Apps pane, find information about the end-to-end lifecycle of an app for each individual device.
3. View installation issues, such as when the app was created, modified, targeted, and delivered to a device.
4. For specific app installation error code information, refer to the Intune app installation error reference.

## Validation
1. Navigate to the Intune Troubleshoot pane in the Microsoft Intune admin center. 2. Select the affected user and device. 3. In the Managed Apps pane, verify that the app status shows 'Installed' or 'Available' and that the installation date is recent. 4. Confirm that no error codes or failure messages are displayed in the app details. 5. Optionally, run the following PowerShell command to check app installation status: Get-IntuneManagedApp -UserId <user@domain.com> -DeviceId <deviceId> | Select-Object AppName, Status, LastSyncDateTime.

## Rollback
1. If the remediation fails, revert to the previous app assignment or configuration by editing the app assignment in Intune to remove the problematic policy. 2. For a specific app, delete and re-add the app assignment from the Microsoft Intune admin center. 3. If issues persist, use the Intune Troubleshoot pane to identify the error code and refer to the Intune app installation error reference at https://learn.microsoft.com/en-us/mem/intune/apps/troubleshoot-app-install for targeted recovery steps. 4. As a last resort, uninstall the app from the device and reinstall it manually or via Intune.

## References
- <https://learn.microsoft.com/en-us/mem/intune/apps/troubleshoot-app-install>
