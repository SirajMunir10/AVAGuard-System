# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
A user receives a 'Profile installation failed' error during device enrollment in Intune.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- User receives a 'Profile installation failed' error

## Error Codes
N/A

## Root Causes
1. User is not assigned an appropriate license for the version of the Intune service
2. Device is already enrolled with another MDM provider
3. Device already has a management profile installed
4. For iOS/iPadOS devices: Safari is not the default browser or cookies are not enabled
5. For Android devices: Chrome is not the default browser or cookies are not enabled

## Remediation Steps
1. Confirm that the user is assigned an appropriate license for the version of the Intune service that you're using.
2. Confirm that the device isn't already enrolled with another MDM provider.
3. Confirm that the device doesn't already have a management profile installed.
4. For iOS/iPadOS devices, confirm that Safari is the default browser and that cookies are enabled.
5. For Android devices, confirm that Chrome is the default browser and that cookies are enabled.

## Validation
1. In the Microsoft Intune admin center, go to 'Users' > select the affected user > 'Licenses' and verify that the user is assigned a license that includes Intune (e.g., Microsoft 365 E3, E5, or standalone Intune). 2. On the device, navigate to 'Settings' > 'General' > 'Device Management' (iOS/iPadOS) or 'Settings' > 'Accounts' (Android) and confirm no existing MDM profile is installed. 3. For iOS/iPadOS: Open Safari, go to 'Settings' > 'Safari' and ensure 'Block All Cookies' is off. 4. For Android: Open Chrome, tap the three-dot menu > 'Settings' > 'Site settings' > 'Cookies' and ensure 'Allow cookies' is enabled.

## Rollback
1. If the user was assigned a new license, remove that license assignment in the Microsoft 365 admin center under 'Users' > select user > 'Licenses and apps' > uncheck the Intune license. 2. If a management profile was removed from the device, re-enroll the device by following the enrollment steps for the platform (e.g., for iOS/iPadOS, go to 'Settings' > 'General' > 'Device Management' and install the management profile from the Company Portal). 3. If browser settings were changed, revert them: on iOS/iPadOS, re-enable 'Block All Cookies' in Safari settings; on Android, disable cookies in Chrome settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
