# Optimization: Device Configuration

**Domain:** Intune
**Subdomain:** Device Configuration
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Intune device configuration by removing stale or duplicate device records that no longer check in, and what are the documented steps to clean up these devices?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Intune-managed Windows 10/11 devices with stale records due to device reimaging or decommissioning without proper cleanup

## Symptoms
- Intune device count exceeds actual active devices
- Duplicate device entries for the same physical device
- Devices listed as 'Not evaluated' or 'Inactive' for more than 30 days
- Compliance policy reports show devices that no longer exist

## Error Codes
N/A

## Root Causes
1. Devices were reimaged or replaced without deleting the old Intune record
2. Devices were decommissioned but not removed from Intune
3. Multiple enrollment records for the same device due to user re-enrollment

## Remediation Steps
1. Identify stale devices using the Intune admin center: Devices > All devices > filter by 'Last check-in' older than 30 days
2. Use Microsoft Graph API to bulk delete stale devices: GET /deviceManagement/managedDevices to list, then POST /deviceManagement/managedDevices/{managedDeviceId}/deleteDevice for each stale device
3. Alternatively, use PowerShell script from Microsoft documentation: Get-MgDeviceManagementManagedDevice -Filter 'lastSyncDateTime lt 2023-01-01' | Remove-MgDeviceManagementManagedDevice
4. After deletion, verify device count reduction and confirm no active devices were removed
5. Implement automated cleanup policy using Azure Automation or Logic Apps to regularly remove devices that haven't checked in for 90 days

## Validation
Confirm in Intune admin center that device count matches expected active devices and no duplicate entries remain. Verify that compliance reports no longer show stale devices.

## Rollback
If accidental deletion occurs, re-enroll the device using Company Portal or Windows Autopilot reset. For bulk recovery, restore from tenant backup if available.

## References
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/device-wipe#remove-devices-from-intune-management>
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/manage-stale-devices>
