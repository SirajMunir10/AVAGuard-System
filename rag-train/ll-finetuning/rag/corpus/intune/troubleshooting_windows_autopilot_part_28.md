# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the Windows out-of-box experience (OOBE) not running as expected during Windows Autopilot?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Windows Autopilot OOBE not running as expected

## Error Codes
N/A

## Root Causes
1. Device did not receive a Windows Autopilot profile
2. Settings in the Windows Autopilot profile are incorrect

## Remediation Steps
1. Check if the device received a Windows Autopilot profile
2. If the device did receive a Windows Autopilot profile, verify that the settings in the profile are correct

## Validation
1. On the affected device, open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin. Look for event ID 1 or 2 indicating receipt of an Autopilot profile. 2. In the Microsoft Intune admin center, go to Devices > Windows > Windows enrollment > Windows Autopilot deployment profiles. Select the assigned profile and verify settings (e.g., deployment mode, privacy settings, local admin account). 3. On the device, run 'Get-AutopilotInfo' (from the Autopilot module) to confirm the profile was applied. 4. Check the device's Autopilot status in Intune under Devices > Windows > Windows enrollment > Windows Autopilot devices.

## Rollback
1. If the device did not receive a profile, ensure the device is registered in Autopilot (check hardware hash in Intune under Devices > Windows > Windows enrollment > Windows Autopilot devices). If not registered, re-import the hardware hash. 2. If profile settings are incorrect, edit the Autopilot deployment profile in Intune (Devices > Windows > Windows enrollment > Windows Autopilot deployment profiles) to correct settings (e.g., change deployment mode from user-driven to self-deploying, adjust privacy settings). 3. If the device received a corrupted profile, delete the device from Autopilot in Intune, re-register it, and reassign the profile. 4. Reset the device to factory settings and reattempt OOBE.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
