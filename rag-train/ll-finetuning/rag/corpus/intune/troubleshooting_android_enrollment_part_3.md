# Troubleshooting: Android Enrollment

**Domain:** Intune
**Subdomain:** Android Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
Company Portal not prompting users to enroll on Android devices

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Android enrollment with Company Portal app

## Symptoms
- Enrollment checklist not displayed as expected when users launch the Company Portal app

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Tap on the notification bell in the upper-right corner of the Company Portal app
2. Tap the notification to bring up the enrollment checklist

## Validation
1. On an Android device that is not yet enrolled, launch the Company Portal app. 2. Observe the upper-right corner for a notification bell icon. 3. Tap the notification bell and confirm that a notification appears. 4. Tap the notification and verify that the enrollment checklist is displayed. 5. Complete the enrollment checklist and confirm that the device appears as enrolled in the Microsoft Intune admin center under Devices > All devices.

## Rollback
1. If the enrollment checklist does not appear after tapping the notification, instruct the user to close and reopen the Company Portal app. 2. If the issue persists, have the user clear the Company Portal app cache and data via Android Settings > Apps > Company Portal > Storage > Clear Cache and Clear Data. 3. Re-launch the Company Portal app and attempt enrollment again. 4. If enrollment still fails, refer to the official troubleshooting guide at https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-android-enrollment for further steps.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-android-enrollment>
