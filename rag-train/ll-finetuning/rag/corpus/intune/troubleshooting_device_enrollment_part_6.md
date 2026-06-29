# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to run diagnostics for Intune enrollment issues when a user-based device fails to enroll?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** User-based device enrollment

## Symptoms
- User-based device fails to enroll in Intune

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run the diagnostics as an administrator.
2. Select the appropriate diagnostic for the device platform: Intune Windows enrollment, Intune iOS/iPadOS enrollment, Intune Android enrollment, or Intune macOS enrollment.

## Validation
1. On the affected device, open the Intune Company Portal app and verify that the device now appears as 'Enrolled' under Devices. 2. In the Microsoft Intune admin center, navigate to Devices > All devices, locate the device, and confirm its enrollment status is 'Enrolled' and the compliance state is 'Compliant'. 3. Run the Intune Management Extension diagnostics by opening a command prompt as administrator and executing: 'cd %ProgramFiles(x86)%\Microsoft Intune Management Extension\ && .\IntuneManagementExtension.exe -ShowInfo'. Verify that the output shows 'Enrollment State: Enrolled' and 'Device State: Active'.

## Rollback
1. If the device is now enrolled but experiencing issues, unenroll the device by going to Settings > Accounts > Access work or school, selecting the work or school account, and clicking 'Disconnect'. 2. In the Intune admin center, navigate to Devices > All devices, select the device, and click 'Delete' to remove it from Intune. 3. Re-run the enrollment diagnostics by selecting the appropriate diagnostic for the device platform (e.g., Intune Windows enrollment) and following the on-screen prompts to identify and resolve the original issue before attempting enrollment again.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
