# Troubleshooting: Device Actions

**Domain:** Intune
**Subdomain:** Device Actions
**Incident Type:** Troubleshooting

## Scenario / Query
What happens if I start a retire/wipe on an offline device or a device that hasn't communicated with the service in a while?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Device remains in Retire/Wipe Pending state

## Error Codes
N/A

## Root Causes
1. Device is offline or hasn't communicated with the service recently
2. MDM certificate has expired

## Remediation Steps
1. Wait for the device to check in before the MDM certificate expires (MDM certificate lasts for one year from enrollment and automatically renews every year)
2. If the device checks in before the MDM certificate expires, it will be retired/wiped
3. If the device doesn't check in before the MDM certificate expires, it won't be able to check in to the service
4. 180 days after the MDM certificate expires, the device will be automatically removed from the Azure portal

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > All devices and select the device. Verify the device status shows 'Retire Wipe Pending' and check the 'Last check-in' time. 2. Confirm the device's MDM certificate expiration date by reviewing the device's enrollment details or using the Graph API: GET https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/{deviceId} and inspect the 'enrolledDateTime' property (certificate valid for one year from enrollment). 3. If the device checks in, verify the device is removed from the device list or shows a wiped/retired state. 4. If 180 days have passed since certificate expiration, confirm the device is automatically removed from Azure AD using Azure AD audit logs or the Azure portal.

## Rollback
1. If the device checks in and the retire/wipe action completes, there is no rollback; the device must be re-enrolled. 2. If the device remains pending and you need to cancel the action, use the 'Cancel Retire/Wipe' option in the Intune admin center under the device's actions. 3. If the device cannot check in due to expired MDM certificate, re-enroll the device by resetting it or using a new enrollment method. 4. If the device was automatically removed after 180 days, re-register the device in Azure AD and re-enroll in Intune.

## References
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/troubleshoot-device-actions>
