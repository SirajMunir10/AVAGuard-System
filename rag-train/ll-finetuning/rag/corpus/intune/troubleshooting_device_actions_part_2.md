# Troubleshooting: Device Actions

**Domain:** Intune
**Subdomain:** Device Actions
**Incident Type:** Troubleshooting

## Scenario / Query
How do I tell who started a Retire/Wipe action on a device in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Device actions audit logging

## Symptoms
- Unknown initiator of a Retire or Wipe device action

## Error Codes
N/A

## Root Causes
1. The action may have been initiated by the device user via Company Portal or portal.manage.microsoft.com

## Remediation Steps
1. In the Microsoft Intune admin center, go to Tenant administration > Audit logs
2. Check the Initiated By column to identify who started the Retire/Wipe action
3. If no entry is found in Audit logs, the action was initiated by the device user via Company Portal or portal.manage.microsoft.com
4. View details under Devices > Monitor > Device actions

## Validation
1. Navigate to Microsoft Intune admin center > Tenant administration > Audit logs. 2. Filter by date range and activity type 'Retire' or 'Wipe'. 3. Confirm the 'Initiated By' column displays the user or service principal that initiated the action. 4. If no audit log entry exists, go to Devices > Monitor > Device actions and verify the action is listed with the device user as initiator.

## Rollback
1. If the Retire/Wipe action was unintended and the device is still enrolled, contact the device user to re-enroll via Company Portal or portal.manage.microsoft.com. 2. If the device was retired or wiped in error, re-enroll the device using the standard enrollment method (e.g., Windows Autopilot, Apple Automated Device Enrollment, or manual enrollment). 3. If audit logs are missing, enable diagnostic settings to stream audit logs to a Log Analytics workspace for future tracking.

## References
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/troubleshoot-device-actions>
