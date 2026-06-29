# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to retrieve a new Windows Autopilot profile during OOBE if a blank profile is cached locally?

## Environment Context
- **Tenant Type:** Azure AD/Entra ID tenant with Windows Autopilot
- **Configuration:** Windows Autopilot profile must exist in tenant

## Symptoms
- Blank Windows Autopilot profile cached locally on device
- Device not applying correct Autopilot profile during OOBE

## Error Codes
N/A

## Root Causes
1. Windows Autopilot profile did not exist in tenant at time of first boot
2. Device cached a blank profile

## Remediation Steps
1. Press Shift-F10 to open a command prompt window
2. Enter shutdown.exe /r /t 0 to restart immediately
3. Alternatively, enter shutdown.exe /s /t 0 to shut down immediately

## Validation
1. After the device restarts, observe the OOBE screen to confirm that the correct Windows Autopilot profile is now displayed. 2. Verify in the Microsoft Intune admin center (https://intune.microsoft.com) that the device is listed under Devices > Windows > Windows enrollment > Windows Autopilot deployment profiles and that the profile status shows 'Assigned' or 'Success'. 3. Check the device's Event Viewer under Applications and Services Logs > Microsoft > Windows > Autopilot for operational events indicating a successful profile download.

## Rollback
1. If the device still shows a blank profile after restart, press Shift-F10 to open a command prompt. 2. Run 'shutdown.exe /s /t 0' to shut down the device immediately. 3. Power on the device again and observe the OOBE to see if the correct profile is now applied. 4. If the issue persists, verify that the Windows Autopilot profile exists and is correctly assigned to the device in the Intune admin center, then repeat the restart or shutdown steps.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
