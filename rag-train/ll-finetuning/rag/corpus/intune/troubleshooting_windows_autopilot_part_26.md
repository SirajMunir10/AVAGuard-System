# Troubleshooting: Windows Autopilot (Ran into trouble. Please sign in with an administrator account to see why and reset manually.)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why does Windows Autopilot Reset fail immediately with an error?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Windows Autopilot Reset fails immediately
- Error message: Ran into trouble. Please sign in with an administrator account to see why and reset manually.

## Error Codes
- `Ran into trouble. Please sign in with an administrator account to see why and reset manually.`

## Root Causes
N/A

## Remediation Steps
1. See Windows Autopilot Reset: Troubleshooting for more help

## Validation
1. Confirm that the device is properly registered in Windows Autopilot by running the following PowerShell command as an administrator on the affected device: (Get-WindowsAutopilotInfo).SerialNumber. Verify the serial number matches the device. 2. Check the Autopilot profile assignment in the Microsoft Intune admin center: navigate to Devices > Windows > Windows enrollment > Enrollment status page > Autopilot deployment profiles, select the profile assigned to the device, and verify the 'Reset' option is enabled under 'Device name template' settings. 3. Review the device's event logs for Autopilot reset errors: open Event Viewer, navigate to Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin, and look for Event ID 500 or 501 indicating reset failure details. 4. Ensure the user performing the reset has local administrator privileges on the device: run 'net localgroup administrators' in Command Prompt as administrator and confirm the user account is listed.

## Rollback
1. If the reset fails and the device is stuck, perform a manual reset by booting from Windows installation media, selecting 'Repair your computer', then 'Troubleshoot', 'Reset this PC', and choose 'Keep my files' or 'Remove everything' as appropriate. 2. Re-register the device in Autopilot by removing and re-adding its hardware hash: in Intune, go to Devices > Windows > Windows enrollment > Autopilot devices, select the device, click 'Delete', then re-import the hardware hash obtained via 'Get-WindowsAutoPilotInfo.ps1' script. 3. If the Autopilot profile assignment was changed, reassign the original profile by navigating to Devices > Windows > Windows enrollment > Autopilot deployment profiles, selecting the profile, and under 'Assignments', add the device group containing the affected device. 4. As a last resort, perform a cloud reset by signing in to https://portal.azure.com, go to Microsoft Intune > Devices > All devices, select the device, click 'More' > 'Autopilot Reset', and follow the prompts to initiate a fresh reset.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
