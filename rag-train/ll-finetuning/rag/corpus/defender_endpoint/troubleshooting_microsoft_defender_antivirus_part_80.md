# Troubleshooting: Microsoft Defender Antivirus (0x80501105)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501105 (MP_ERROR_CODE_NO_TARGETOS) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501105
- Message displayed: MP_ERROR_CODE_NO_TARGETOS

## Error Codes
- `0x80501105`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Defender > Operational.
3. Verify that no new events with ID 1006, 1007, or 1008 are logged after remediation.
4. Run 'Get-MpComputerStatus' in PowerShell and confirm that 'AMRunningMode' is 'Normal' and 'AntivirusEnabled' is 'True'.
5. Run 'Start-MpScan -ScanType QuickScan' and confirm the scan completes without error code 0x80501105.

## Rollback
1. If the error persists, restore the previous Microsoft Defender Antivirus policy settings via Group Policy Management Console or Intune.
2. In an elevated PowerShell session, run 'Set-MpPreference -DisableRealtimeMonitoring $false' if real-time monitoring was disabled.
3. Re-register the Microsoft Defender Antivirus service by running '& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Register'.
4. Restart the 'WinDefend' service with 'Restart-Service WinDefend'.
5. If the issue remains, use System Restore to revert to a point before the remediation was applied.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
