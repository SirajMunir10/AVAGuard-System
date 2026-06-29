# Troubleshooting: Microsoft Defender Antivirus (0x8050801)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x8050801 with message ERR_MP_REMOVE_FAILED in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x8050801 displayed
- Message displayed: ERR_MP_REMOVE_FAILED ERR_MP_REMOVE_FAILED

## Error Codes
- `0x8050801`

## Root Causes
1. This error is internal. It might be triggered when malware removal isn't successful.

## Remediation Steps
N/A

## Validation
Run the following command in an elevated PowerShell prompt to check the current status of Microsoft Defender Antivirus: Get-MpComputerStatus. Verify that the AMProductVersion, AMServiceEnabled, and AntivirusEnabled fields show expected values. Then perform a quick scan using Start-MpScan -ScanType QuickScan and confirm no errors appear. Finally, check the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for any new error events with ID 1006 or 1007 that would indicate removal failures.

## Rollback
If the remediation fails, restore the default Microsoft Defender Antivirus configuration by running Set-MpPreference -DisableRealtimeMonitoring $false and Update-MpSignature. Then re-run the full scan using Start-MpScan -ScanType FullScan. If the issue persists, reset the Microsoft Defender Antivirus platform by running "C:\ProgramData\Microsoft\Windows Defender\Platform\<version>\MpCmdRun.exe" -RemoveDefinitions -All and then "C:\ProgramData\Microsoft\Windows Defender\Platform\<version>\MpCmdRun.exe" -SignatureUpdate. Finally, restart the service with Restart-Service WinDefend.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
