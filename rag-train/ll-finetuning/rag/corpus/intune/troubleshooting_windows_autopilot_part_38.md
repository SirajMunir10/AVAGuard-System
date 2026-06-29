# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve incorrect enrolled date for Windows Autopilot device in Intune?

## Environment Context
- **Tenant Type:** Intune-managed tenant with Windows Autopilot devices
- **Configuration:** Devices registered to Windows Autopilot

## Symptoms
- Enrolled date in Devices | All devices and Windows | Windows devices panes displays the date the device was registered to Windows Autopilot instead of the date it was enrolled to Windows Autopilot

## Error Codes
N/A

## Root Causes
1. The Enrolled date field incorrectly shows the registration date rather than the enrollment date

## Remediation Steps
1. Use the Intune Graph API to query the device: devices?$filter=physicalIds/any(p: startswith(p, '[ZTDID]'))&$select=id,deviceId,displayName,physicalIds,createdDateTime
2. Use the Windows Autopilot deployment report for recently deployed devices

## Validation
1. Run the Graph API query: GET https://graph.microsoft.com/v1.0/deviceManagement/windowsAutopilotDeviceIdentities?$filter=physicalIds/any(p: startswith(p, '[ZTDID]'))&$select=id,deviceId,displayName,physicalIds,createdDateTime
2. Compare the 'createdDateTime' value with the enrolled date shown in the Intune console (Devices > All devices > select the device > check 'Enrolled date').
3. If 'createdDateTime' matches the registration date (not the actual enrollment date), the issue is confirmed.
4. Use the Windows Autopilot deployment report (Reports > Windows Autopilot > Deployment reports) to verify the actual enrollment date for recently deployed devices.
5. Confirm that the enrolled date in the console still shows the registration date, indicating the known issue.

## Rollback
1. No rollback is needed because the remediation steps are diagnostic only (querying the API and viewing reports) and do not change any configuration or data.
2. If the Graph API query or report access fails, verify permissions: ensure the account has at least 'DeviceManagementManagedDevices.Read.All' and 'DeviceManagementServiceConfig.Read.All' roles.
3. If the issue persists, refer to the known issues documentation at https://learn.microsoft.com/en-us/mem/autopilot/known-issues for any updates or workarounds.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
- <https://learn.microsoft.com/en-us/mem/intune/developer/intune-graph-apis>
- <https://learn.microsoft.com/en-us/graph/api/resources/intune-graph-overview>
