# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the 'Company Portal Temporarily Unavailable' error during device enrollment in Intune?

## Environment Context
- **Tenant Type:** Microsoft Entra ID integrated
- **Configuration:** Device enrollment limits

## Symptoms
- Users receive a Company Portal Temporarily Unavailable error on their device

## Error Codes
N/A

## Root Causes
1. The Company Portal app on the device is out of date or corrupted
2. User is attempting to enroll more devices than device enrollment is configured to allow

## Remediation Steps
1. Remove the Intune Company Portal app from the device
2. On the device, open the browser, browse to https://portal.manage.microsoft.com, and try a user login
3. If the user fails to sign in, they should try another network
4. If that fails, validate that the user's credentials have synced correctly with Microsoft Entra ID
5. If the user successfully logs in, an iOS/iPadOS device will prompt you to install the Intune Company Portal app and enroll
6. On an Android device, manually install the Intune Company Portal app, after which you can retry enrolling
7. If these steps do not resolve the issue, follow the solution steps for 'Device cap reached'

## Validation
1. Confirm the user can sign in at https://portal.manage.microsoft.com without errors. 2. On iOS/iPadOS, verify the Company Portal app installs and enrollment completes. 3. On Android, verify the manually installed Company Portal app allows enrollment. 4. Check the user’s device count in Microsoft Entra ID (Azure AD) under Users > device settings to ensure it is below the enrollment limit.

## Rollback
1. If validation fails, reinstall the original Company Portal app from the device’s app store. 2. If the issue persists, check Microsoft Entra ID sync status and force a sync if needed. 3. If the device cap is reached, increase the per-user device limit in Microsoft Entra ID > Devices > Device settings or remove an existing device from the user’s device list.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
