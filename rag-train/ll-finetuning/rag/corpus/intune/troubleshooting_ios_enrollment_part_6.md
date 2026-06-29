# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the 'Workplace Join failed' error during iOS enrollment in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** iOS enrollment with Company Portal app

## Symptoms
- Workplace Join failed error during enrollment

## Error Codes
N/A

## Root Causes
1. Company Portal app is out of date or corrupted

## Remediation Steps
1. Remove the Company Portal app from the device
2. Download and install the Microsoft Intune Company Portal app from App Store
3. Re-enroll the device

## Validation
1. On the iOS device, go to Settings > General > Device Management and confirm no management profile is listed. 2. Open the App Store, search for 'Microsoft Intune Company Portal', and verify the app is installed and up to date. 3. Open the Company Portal app, sign in with the user's work or school account, and confirm the device appears as compliant in the Microsoft Intune admin center under Devices > All devices.

## Rollback
1. If the re-enrollment fails, on the iOS device go to Settings > General > Device Management and remove any management profile. 2. Reinstall the previous version of the Company Portal app from the App Store if available, or contact Microsoft Support to restore the app. 3. Attempt enrollment again using the original Company Portal app version. If issues persist, reinstall the latest Company Portal app from the App Store and retry enrollment.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
