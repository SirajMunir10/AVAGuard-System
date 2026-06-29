# Troubleshooting: Device Enrollment (DeviceCapReached)

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
A user receives an error during enrollment, such as 'DeviceCapReached' or a general message such as 'Company Portal Temporarily Unavailable'. How do I resolve this?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Device enrollment restrictions, device limit restrictions

## Symptoms
- User receives error 'DeviceCapReached' during enrollment
- User receives general message 'Company Portal Temporarily Unavailable'

## Error Codes
- `DeviceCapReached`

## Root Causes
1. User is trying to enroll more devices than the device enrollment limit

## Remediation Steps
1. In the Microsoft Intune admin center, choose Devices > Enrollment restrictions > Device limit restrictions. Note the value in the Device limit column.
2. In the Microsoft Intune admin center, choose Users > All users > select the user > Devices. Note the number of devices the user has enrolled.
3. If the user's number of enrolled devices already equals their device limit restriction, they can't enroll anymore until: Existing devices are removed, or You increase the device limit by setting device restrictions.
4. To avoid hitting device caps, be sure to remove stale device records.
5. You can avoid the device enrollment cap by using Device Enrollment Manager account, as described in Enroll corporate-owned devices with the Device Enrollment Manager in Microsoft Intune.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
