# Troubleshooting: Microsoft Defender Antivirus (5010)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 5010 indicating that Microsoft Defender Antivirus scanning for malware and other potentially unwanted software is disabled?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Scanning for malware and other potentially unwanted software is disabled

## Error Codes
- `5010`

## Root Causes
1. Microsoft Defender Antivirus scanning for malware and other potentially unwanted software is disabled

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. Verify that Event ID 5010 is no longer present after remediation.
2. Run the PowerShell command: Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled. Confirm that all three properties return True.
3. Run the PowerShell command: Get-MpPreference | Select-Object DisableRealtimeMonitoring, DisableBehaviorMonitoring, DisableBlockAtFirstSeen. Confirm that all three properties return False.
4. Run the PowerShell command: Start-MpScan -ScanType QuickScan. Verify that the scan completes without errors and returns a clean result.

## Rollback
1. If the remediation involved enabling a disabled service, re-disable it by running: Set-MpPreference -DisableRealtimeMonitoring $true (or the specific preference that was changed).
2. If group policy was modified, revert the policy to its previous state using Group Policy Management Console (GPMC) or by restoring the backed-up policy file.
3. If registry keys were changed, restore the original values from backup or set them back to the disabled state (e.g., reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f).
4. Restart the Microsoft Defender Antivirus service by running: Restart-Service WinDefend. Then confirm the original error reoccurs by checking Event ID 5010 in Event Viewer.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
