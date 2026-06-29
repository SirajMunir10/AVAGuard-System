# Troubleshooting: Microsoft Defender Antivirus (0x8050800F)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x8050800F with message ERR_MP_NOT_SUPPORTED in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x8050800F displayed
- Message displayed: ERR_MP_NOT_SUPPORTED ERR_MP_NOT_SUPPORTED

## Error Codes
- `0x8050800F`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to 'Virus & threat protection' > 'Manage settings' to verify that real-time protection is enabled.
2. Run 'Get-MpComputerStatus' in PowerShell and confirm that 'AMServiceEnabled', 'AntivirusEnabled', and 'RealTimeProtectionEnabled' are all set to True.
3. Execute 'MpCmdRun -GetDeviceHealth' and check that the output shows 'HealthStatus: 0' (Healthy) and no error codes.
4. Trigger a quick scan with 'Start-MpScan -ScanType QuickScan' and verify it completes without error.
5. Check the Microsoft Defender Antivirus event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1150 (scan completed) and no error events.

## Rollback
1. If the remediation involved disabling or modifying a service, re-enable the Microsoft Defender Antivirus service by running 'Set-Service WinDefend -StartupType Automatic' and 'Start-Service WinDefend' in PowerShell.
2. If registry changes were made, restore the original values from a backup or use 'reg delete' to remove any added keys under 'HKLM\SOFTWARE\Policies\Microsoft\Windows Defender'.
3. If group policy settings were altered, revert the policy to 'Not Configured' or the previous state via Group Policy Management Console.
4. If a third-party antivirus was installed, uninstall it and ensure Microsoft Defender Antivirus is active by running 'Set-MpPreference -DisableRealtimeMonitoring $false'.
5. Reboot the device and re-run the validation steps to confirm the error returns to the original state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
