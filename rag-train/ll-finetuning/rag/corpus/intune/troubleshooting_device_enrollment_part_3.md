# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot device enrollment issues in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Initial troubleshooting steps before starting

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Check to make sure that you've configured Intune properly to enable enrollment.
2. Read about configuration requirements in documentation: Set up Intune, Enroll iOS/iPadOS devices in Intune, Set up enrollment for macOS devices in Intune, Set up enrollment for Windows devices in Intune, Enroll Android devices in Intune - No additional steps required

## Validation
1. Verify that Intune is configured for enrollment by navigating to Microsoft Intune admin center > Devices > Enroll Devices > Enrollment restrictions. Ensure that default enrollment restrictions allow the platform you are testing (e.g., iOS, Android, Windows, macOS).
2. Confirm that the required Intune licenses are assigned to the user attempting enrollment. In Microsoft Entra admin center > Users > select the user > Licenses, verify an Intune license is assigned.
3. On a test device, attempt enrollment by following the platform-specific steps (e.g., for iOS: Settings > General > Device Management > sign in with the user's work or school account). Ensure the device appears in Intune admin center > Devices > All devices within a few minutes.
4. Check Intune admin center > Devices > Enroll Devices > Enrollment logs for any errors or warnings related to the test enrollment attempt.

## Rollback
1. If enrollment fails due to restrictions, temporarily remove or modify enrollment restrictions: In Intune admin center > Devices > Enroll Devices > Enrollment restrictions, edit the default restriction to allow all platforms for testing, then reattempt validation.
2. If the issue is license-related, assign an Intune license to the test user in Microsoft Entra admin center > Users > select user > Licenses > Assignments > select Intune license.
3. If the device was partially enrolled, remove it from Intune: In Intune admin center > Devices > All devices > select the device > Delete, then on the device itself, go to Settings > General > Device Management > Remove Management.
4. Restore any changed enrollment restrictions to their original state after testing.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
