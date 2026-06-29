# Troubleshooting: Device Check-in

**Domain:** Intune
**Subdomain:** Device Check-in
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when Last check in is more than 24 hours for an Intune device?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Last check in is more than 24 hours

## Error Codes
N/A

## Root Causes
1. Device can't check in
2. Device may be turned off
3. Device may not have a network connection

## Remediation Steps
1. On the Android device, open the Company Portal app > Devices > Choose the device from list > Check Device Settings
2. On the iOS/iPadOS device, open the Company portal app > Devices > Choose the device from list > Check Settings
3. On a Windows device, open Settings > Accounts > Access Work or School > Select the account or MDM enrollment > Info > Sync

## Validation
1. On the Android device: Open Company Portal > Devices > select the device > tap 'Check Device Settings' and confirm the status shows 'Device settings are compliant' or similar success message. 2. On iOS/iPadOS: Open Company Portal > Devices > select the device > tap 'Check Settings' and verify the device status is compliant. 3. On Windows: Go to Settings > Accounts > Access Work or School > select the account > click 'Info' > click 'Sync' and confirm the last sync time updates to within the last 24 hours. 4. In the Intune admin center (https://intune.microsoft.com), navigate to Devices > All devices, select the device, and verify the 'Last check-in' time is less than 24 hours ago.

## Rollback
1. If the device still shows 'Last check-in' > 24 hours after remediation, verify network connectivity on the device (e.g., ensure Wi-Fi or cellular data is enabled and the device can reach the internet). 2. Confirm the device is powered on and not in airplane mode. 3. Restart the device and repeat the validation steps. 4. If the issue persists, re-enroll the device in Intune by removing the device from the Company Portal app (Android/iOS) or from Access Work or School (Windows) and then re-adding it. 5. As a last resort, factory reset the device and re-enroll (note: this will erase all data on the device).

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
