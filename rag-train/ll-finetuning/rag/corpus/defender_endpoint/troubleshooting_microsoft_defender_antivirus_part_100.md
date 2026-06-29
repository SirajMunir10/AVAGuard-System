# Troubleshooting: Microsoft Defender Antivirus (0x8050A002)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x8050A002 with message ERR_MP_BADDB_HEADER in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x8050A002 displayed
- Message displayed: ERR_MP_BADDB_HEADER ERR_MP_BADDB_HEADER

## Error Codes
- `0x8050A002`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Windows Logs > System.
3. Filter for Event ID 1006, 1008, or 1015 from source 'Microsoft Antimalware' or 'Microsoft Defender Antivirus'.
4. Confirm no events with error code 0x8050A002 appear.
5. Run 'Get-MpComputerStatus' in PowerShell as Administrator and verify 'AMServiceEnabled' and 'AntivirusEnabled' are both True.
6. Run 'Start-MpScan -ScanType QuickScan' and confirm no error 0x8050A002 is returned.

## Rollback
1. If validation fails, restore the previous state of Microsoft Defender Antivirus by running 'Set-MpPreference -DisableRealtimeMonitoring $false' if it was disabled.
2. Re-register the Microsoft Defender Antivirus service: '& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Register'.
3. If the issue persists, use System Restore to revert to a point before any changes were made: 'rstrui.exe'.
4. As a last resort, reset Microsoft Defender Antivirus settings to default: 'Set-MpPreference -Force'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
