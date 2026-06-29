# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Windows Autopilot out-of-box experience (OOBE) issues?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows Autopilot deployment profile

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Collect MDM logs
2. Collect diagnostics from a Windows device

## Validation
1. On the affected Windows device, open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin. Verify that no critical errors (Event ID 100, 200, 300) related to Autopolicy or MDM enrollment are present. 2. Run the command 'Get-AutopilotInfo' from an elevated PowerShell prompt on the device and confirm that the Autopilot profile is correctly assigned (ProfileAssigned = True) and that the EnrollmentState is 'Enrolled'. 3. Check the MDM diagnostic logs at %ProgramData%\Microsoft\MDM\Logs and ensure the most recent log file shows a successful enrollment completion (look for 'Enrollment succeeded' or 'Sync completed' entries). 4. On the Intune portal, navigate to Devices > Enroll Devices > Windows enrollment > Windows Autopilot deployment profiles, select the relevant profile, and verify that the device is listed under 'Assigned devices' with status 'Assigned'.

## Rollback
1. If the collected MDM logs indicate a failed enrollment due to a misconfigured profile, remove the device from the Autopilot deployment profile: In Intune, go to Devices > Windows > Windows enrollment > Devices, select the device, and click 'Delete' to remove its Autopilot hash. 2. Re-register the device by obtaining a new hardware hash via the command 'Get-WindowsAutoPilotInfo.ps1 -OutputFile C:\DeviceHash.csv' from an elevated PowerShell prompt on the device, then upload the CSV file to Intune under Devices > Windows > Windows enrollment > Devices > Import. 3. If diagnostics show a network or connectivity issue, reset the device's network stack by running 'netsh int ip reset' and 'netsh winsock reset' from an elevated command prompt, then reboot. 4. As a last resort, perform a full device reset via Windows Recovery Environment (WinRE) by holding Shift while clicking Restart, then selecting Troubleshoot > Reset this PC > Remove everything, and re-initiate the Autopilot OOBE.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
