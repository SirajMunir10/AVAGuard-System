# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
What does the CloudAssignedOobeConfig bitmap value indicate about Autopilot settings?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot OOBE configuration

## Symptoms
- Certain OOBE screens not skipped as expected
- Autopilot profile not applying all configured settings

## Error Codes
N/A

## Root Causes
1. CloudAssignedOobeConfig bitmap does not include expected settings

## Remediation Steps
1. Check registry key: HKLM\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot
2. Read CloudAssignedOobeConfig value and compare against known bitmap values: SkipCortanaOptIn = 1, OobeUserNotLocalAdmin = 2, SkipExpressSettings = 4, SkipOemRegistration = 8, SkipEula = 16
3. Verify that the bitmap includes the expected settings

## Validation
1. On the affected device, open Registry Editor (regedit.exe) and navigate to HKLM\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot. 2. Locate the DWORD value 'CloudAssignedOobeConfig' and note its decimal value. 3. Convert the decimal value to binary or use the known bitmask values (SkipCortanaOptIn=1, OobeUserNotLocalAdmin=2, SkipExpressSettings=4, SkipOemRegistration=8, SkipEula=16) to verify that the expected settings are included. For example, if SkipEula and SkipExpressSettings are expected, the bitmap should include 16+4=20. 4. Confirm that the bitmap value matches the expected combination. 5. Optionally, run 'Get-AutopilotDiagnostics' (if available) or review the Autopilot profile assignment in the Intune portal to ensure the profile is correctly assigned to the device.

## Rollback
1. If the remediation (e.g., re-assigning or modifying the Autopilot profile) caused issues, reapply the original Autopilot profile settings via the Intune portal: navigate to Devices > Windows > Windows enrollment > Deployment profiles, select the affected profile, and reassign it to the device group. 2. If registry changes were made, restore the original CloudAssignedOobeConfig value by setting it back to the previous decimal value (document the original value before any change). 3. Force a new Autopilot session by running 'Get-WindowsAutopilotInfo -Online' or resetting the device using 'Reset this PC' with the option to keep or remove files as needed. 4. Verify that the device re-enrolls and applies the correct OOBE configuration by checking the registry key again after the next Autopilot run.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
