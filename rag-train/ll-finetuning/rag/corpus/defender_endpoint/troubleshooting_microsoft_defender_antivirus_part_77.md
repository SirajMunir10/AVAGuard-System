# Troubleshooting: Microsoft Defender Antivirus (0x80501101)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501101 with message ERROR_LUA_CANCELLATION in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501101 displayed
- Message displayed: ERROR_LUA_CANCELLATION

## Error Codes
- `0x80501101`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that no new events with ID 1006, 1007, or 1008 related to error 0x80501101 appear after remediation.
4. Run a manual scan: Start-MpScan -ScanType QuickScan in PowerShell (as Admin).
5. Confirm the scan completes without error code 0x80501101.
6. Check the protection status: Get-MpComputerStatus | select AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled.

## Rollback
1. If the error persists, restore the default Microsoft Defender Antivirus configuration:
   - In PowerShell (Admin): Set-MpPreference -DisableRealtimeMonitoring $false
   - Reset all preferences: Remove-MpPreference
2. Re-register the Windows Defender service:
   - Run: 'C:\Program Files\Windows Defender\MpCmdRun.exe' -RemoveDefinitions -All
   - Then: 'C:\Program Files\Windows Defender\MpCmdRun.exe' -SignatureUpdate
3. If the issue remains, use System Restore to revert to a point before changes were made.
4. As a last resort, reset Windows Security app via Settings > Apps > Microsoft Defender > Advanced options > Reset.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
