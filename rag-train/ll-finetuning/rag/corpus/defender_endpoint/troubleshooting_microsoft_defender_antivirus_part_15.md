# Troubleshooting: Microsoft Defender Antivirus (Event ID 1002)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot a cancelled antimalware scan in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- An antimalware scan was stopped before it finished.

## Error Codes
- `Event ID 1002`
- `MALWAREPROTECTION_SCAN_CANCELLED`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Verify that no new Event ID 1002 with source 'MALWAREPROTECTION_SCAN_CANCELLED' appears after initiating a new scan.
2. Run 'Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled, AntispywareEnabled, BehaviorMonitorEnabled' in PowerShell to confirm all protection features are enabled.
3. Execute 'Start-MpScan -ScanType QuickScan' and monitor the scan progress using 'Get-MpScanStatus' until it completes without cancellation.
4. Check the Microsoft Defender Antivirus client UI to ensure no 'Scan cancelled' notifications are present.

## Rollback
1. If validation fails, restore the default Microsoft Defender Antivirus configuration by running 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Set-MpPreference -DisableBehaviorMonitoring $false' in PowerShell.
2. Reset the Microsoft Defender Antivirus service by executing 'net stop WinDefend' followed by 'net start WinDefend' in an elevated command prompt.
3. If the issue persists, re-register the Microsoft Defender Antivirus DLLs by running 'regsvr32 /s %ProgramFiles%\Windows Defender\MpClient.dll' and 'regsvr32 /s %ProgramFiles%\Windows Defender\MpOAV.dll' in an elevated command prompt.
4. As a last resort, perform a system restore to a point before the scan cancellation issue occurred using 'rstrui.exe'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
