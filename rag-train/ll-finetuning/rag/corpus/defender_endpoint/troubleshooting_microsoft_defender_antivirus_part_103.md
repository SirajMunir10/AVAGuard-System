# Troubleshooting: Microsoft Defender Antivirus (0x8050A005)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x8050A005 with message ERR_MP_BADDB_NOTSIGNED in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x8050A005 displayed
- Message: ERR_MP_BADDB_NOTSIGNED

## Error Codes
- `0x8050A005`
- `ERR_MP_BADDB_NOTSIGNED`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to Virus & threat protection. Verify that 'Real-time protection' is turned On and no warning banners are displayed. 2. Run the PowerShell command: Get-MpComputerStatus | Select-Object AMServiceEnabled, AMServiceVersion, AntispywareEnabled, AntivirusEnabled. Confirm all four properties show True. 3. Run the PowerShell command: Get-MpThreatDetection. Confirm no active threats with error code 0x8050A005 are listed. 4. Run the PowerShell command: Start-MpScan -ScanType QuickScan. Confirm the scan completes without error code 0x8050A005. 5. Check the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1000 or 1001 with no error code 0x8050A005.

## Rollback
1. If validation fails, restore the previous state by running: Set-MpPreference -DisableRealtimeMonitoring $false (if real-time protection was disabled). 2. If a signature update was applied, roll back to the previous signature version using: Update-MpSignature -Rollback. 3. If a system file or registry change was made, restore from a known good backup or use System Restore to a point before remediation. 4. If the issue persists, reinstall Microsoft Defender Antivirus by running: Uninstall-WindowsFeature -Name Windows-Defender; Restart-Computer; Install-WindowsFeature -Name Windows-Defender. 5. Contact Microsoft Support if rollback steps do not resolve the error.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
