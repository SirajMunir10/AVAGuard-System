# Troubleshooting: App Deployment

**Domain:** Intune
**Subdomain:** App Deployment
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose why a user's application deployment does not complete due to various failures in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** App deployment policies

## Symptoms
- User's application deployment does not complete

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run the diagnostic as an administrator.
2. Use the Intune app deployment diagnostic to identify the cause of the issue.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com) with an account that has the Intune Administrator role.
2. Navigate to Troubleshooting + support > App deployment diagnostic.
3. Enter the user's UPN (user principal name) and select the app that failed to deploy.
4. Review the diagnostic results for any error messages or status codes indicating installation failure.
5. Confirm that the app deployment status now shows 'Installed' or 'Success' for the targeted user.
6. Optionally, run the following PowerShell command as an administrator to verify the app installation status on the device: Get-WinEvent -LogName Microsoft-Windows-AppLocker/EXE and DLL -MaxEvents 10 | Where-Object { $_.Message -like '*<AppName>*' }

## Rollback
1. If the remediation caused issues, sign in to the Intune admin center and navigate to Apps > All apps.
2. Select the problematic app and choose 'Uninstall' from the assignment actions for the affected user or device group.
3. Alternatively, modify the app assignment to 'Not assigned' for the user or group to stop further deployment attempts.
4. If the diagnostic tool was used and changes were made (e.g., re-syncing policies), instruct the user to sync their device: Settings > Accounts > Access work or school > Select the account > Sync.
5. For persistent issues, remove the device from Intune management and re-enroll it: In the Intune admin center, go to Devices > All devices, select the device, and choose 'Delete'. Then have the user re-enroll via Settings > Accounts > Access work or school > Connect.

## References
- <https://learn.microsoft.com/en-us/mem/intune/apps/troubleshoot-app-install>
