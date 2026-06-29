# Troubleshooting: Windows Enrollment (0x80180022)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
Autopilot device enrollment failed with error HRESULT = 0x80180022

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Autopilot device enrollment failed

## Error Codes
- `0x80180022`

## Root Causes
1. The device being provisioned is running Windows Home Edition

## Remediation Steps
1. Update the device to Pro edition or higher

## Validation
1. Verify the current Windows edition on the device by running 'winver' or 'systeminfo | findstr /C:"OS Name"'. Confirm it shows 'Windows 10 Pro' or 'Windows 11 Pro' (or higher).
2. Attempt a fresh Autopilot enrollment by resetting the device (Settings > Update & Security > Recovery > Reset this PC) and re-running the enrollment process. Confirm no 0x80180022 error appears.
3. In the Microsoft Intune admin center, navigate to Devices > Enroll Devices > Windows enrollment > Enrollment status page and verify the device appears as enrolled without errors.

## Rollback
1. If the upgrade to Pro edition fails or causes issues, reinstall the original Windows Home edition using the device manufacturer's recovery media or a Windows 10/11 Home installation ISO.
2. After reinstallation, ensure the device is not enrolled in Intune by checking Settings > Accounts > Access work or school and disconnecting any existing enrollment.
3. Confirm the device returns to its original state by running 'systeminfo' and verifying the OS name shows 'Windows 10 Home' or 'Windows 11 Home'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
