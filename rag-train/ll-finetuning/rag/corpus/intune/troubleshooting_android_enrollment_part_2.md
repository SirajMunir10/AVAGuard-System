# Troubleshooting: Android enrollment

**Domain:** Intune
**Subdomain:** Android enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to reset the device passcode on Android Enterprise enrolled devices?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Android Enterprise enrollment types: personally owned work profile, corporate-owned work profile, dedicated devices, fully managed devices

## Symptoms
- Device passcode reset not supported for personally owned work profile enrolled devices on Android versions below 8.0
- Device passcode reset not supported for personally owned work profile enrolled devices on Android 8.0 or later if work profile passcode is not managed or device user has not allowed reset

## Error Codes
N/A

## Root Causes
1. For personally owned work profile enrolled devices, passcode reset is only supported on Android 8.0 or later when the work profile passcode is managed and the device user has allowed reset
2. For corporate-owned work profile enrolled devices, only work profile passcode reset is supported
3. For Android Enterprise dedicated devices and fully managed devices, device passcode reset is supported

## Remediation Steps
1. For personally owned work profile enrolled devices on Android 8.0 or later: ensure work profile passcode is managed and device user has allowed reset
2. For corporate-owned work profile enrolled devices: reset work profile passcode only
3. For Android Enterprise dedicated devices and fully managed devices: device passcode reset is supported

## Validation
1. Confirm the device's Android version and enrollment type in Microsoft Intune admin center: Devices > All devices > select device > check 'OS' and 'Enrollment type' fields.
2. For personally owned work profile devices on Android 8.0+: verify that 'Work profile passcode managed' is set to 'Require' in the device compliance policy or configuration profile, and that the device user has granted reset permission via Company Portal app > Settings > 'Allow reset of work profile passcode'.
3. Attempt a passcode reset from Intune: Devices > All devices > select device > ... > Device passcode reset. Confirm success message or error.
4. For corporate-owned work profile devices: verify only work profile passcode reset is offered (device-level reset should not be available).
5. For dedicated/fully managed devices: confirm device passcode reset option is available and executes successfully.

## Rollback
1. If passcode reset fails or causes issues, instruct the device user to manually change the passcode via device settings.
2. For personally owned work profile devices: if reset was attempted but failed, verify work profile passcode management settings and user consent; adjust policy if needed.
3. For corporate-owned work profile devices: if work profile passcode reset fails, use Android Enterprise management tools (e.g., managed Google Play) to reset work profile passcode.
4. For dedicated/fully managed devices: if device passcode reset fails, perform a factory reset via hardware keys or Android Enterprise reset command (if supported).
5. Document the failure and escalate to Microsoft support if necessary.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-android-enrollment>
