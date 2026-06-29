# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle expired certificates in the management profile during iOS/iPadOS enrollment in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** iOS/iPadOS enrollment with management profile

## Symptoms
- Expired certificates appear within the management profile on iOS/iPadOS devices
- Unverified expired certificates may be visible on enrolled devices

## Error Codes
N/A

## Root Causes
1. The IOSProfileSigning.manage.microsoft.com certificate expires but remains on devices due to iOS/iPadOS platform design
2. Certificate is only needed for initial enrollment and is not removed after use

## Remediation Steps
1. No remediation needed for existing enrollments as they will work as expected
2. New enrollments will automatically receive the same certificate with a new date

## Validation
1. On an iOS/iPadOS device that is already enrolled, navigate to Settings > General > Device Management and verify that the management profile is present and shows a status of 'Verified' or 'Managed' despite the expired certificate. 2. Confirm that the device can still receive policies and apps from Intune by checking the Company Portal app for a successful sync. 3. For a new enrollment, perform a fresh enrollment of an iOS/iPadOS device and verify that the management profile installs successfully and the certificate date is updated. 4. Review the Intune console under Devices > iOS/iPadOS > Enrollment to ensure no enrollment failures are reported.

## Rollback
1. If an existing enrollment is affected, remove the device from Intune by going to Devices > iOS/iPadOS > select the device > Delete. 2. On the device, go to Settings > General > Device Management and tap 'Remove Management' to clear the profile. 3. Re-enroll the device by installing the Company Portal app and following the enrollment prompts. 4. If new enrollments fail, verify that the Intune service is healthy by checking the Service Health dashboard in the Microsoft 365 admin center. 5. As a last resort, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
