# Troubleshooting: Microsoft Defender Antivirus (1014)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 1014 where Microsoft Defender Antivirus cannot delete history of malware and other potentially unwanted software?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1014 is logged with message: The antimalware platform couldn't delete history of malware and other potentially unwanted software.

## Error Codes
- `1014`

## Root Causes
1. Microsoft Defender Antivirus encountered an error trying to remove history of malware and other potentially unwanted software.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that no new Event ID 1014 errors appear after remediation.
4. Run the PowerShell command: Get-MpThreatDetection | Where-Object {$_.InitialDetectionTime -gt (Get-Date).AddHours(-1)} to confirm no recent detection failures.
5. Check the Microsoft Defender Antivirus client version: Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled.

## Rollback
1. If the remediation involved resetting the Microsoft Defender Antivirus scan history, restore the previous state by running: & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Restore -ListAll | ForEach-Object { & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Restore -FilePath $_.Path }.
2. If registry changes were made, restore the backed-up registry key (e.g., HKLM\SOFTWARE\Microsoft\Windows Defender\Scan\DisableRestorePoint) to its original value.
3. Re-enable any disabled services: Set-Service WinDefend -StartupType Automatic; Start-Service WinDefend.
4. Reapply any group policy settings that were temporarily removed.
5. Reboot the system if required to revert to the previous operational state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
