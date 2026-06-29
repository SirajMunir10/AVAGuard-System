# Troubleshooting: Windows Autopilot (0x80180014)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is error code 0x80180014 occurring when trying to re-enroll a previously enrolled device?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Windows Autopilot self-deployment mode or pre-provisioning mode

## Symptoms
- Error code 0x80180014 during re-enrollment of a previously enrolled device

## Error Codes
- `0x80180014`

## Root Causes
1. Microsoft Intune changed the Windows Autopilot self-deployment mode and pre-provisioning mode experience. To reuse a device, the device record created by Intune must be deleted.

## Remediation Steps
1. Sign into the Microsoft Intune admin center.
2. In the Home screen, select Devices in the left hand pane.
3. In the Devices | Overview screen, under By platform, select Windows.
4. In the Windows | Windows devices screen, under Device onboarding, select Enrollment.
5. In the Windows | Enrollment screen, under Windows Autopilot, select Devices.
6. Select the device that is experiencing the error, and then in the toolbar select Unblock device.
7. Redeploy the Windows Autopilot deployment profile.

## Validation
A success message might not display after selecting Unblock device, but the device is ready to be used again.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
