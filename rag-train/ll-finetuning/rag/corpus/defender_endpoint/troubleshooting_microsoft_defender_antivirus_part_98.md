# Troubleshooting: Microsoft Defender Antivirus (0x80509003)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80509003 with message ERR_RELO_KERNEL_NOT_LOADED in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80509003 displayed
- Message displayed: ERR_RELO_KERNEL_NOT_LOADED ERR_RELO_KERNEL_NOT_LOADED

## Error Codes
- `0x80509003`

## Root Causes
1. The cause isn't clearly defined. This error is internal.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to Virus & threat protection > Virus & threat protection settings. Verify that Real-time protection is turned On. 2. Run the command 'Get-MpComputerStatus' in PowerShell as Administrator and confirm that 'AMServiceEnabled', 'AntivirusEnabled', 'RealTimeProtectionEnabled', and 'IoavProtectionEnabled' all show 'True'. 3. Check the Microsoft Defender Antivirus event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for any new error events with ID 1006, 1007, or 1008 that indicate the error is resolved. 4. Attempt to trigger a scan manually by running 'Start-MpScan -ScanType QuickScan' in PowerShell and verify no error 0x80509003 appears.

## Rollback
1. If the remediation involved modifying registry keys, restore the original values from a backup or export. 2. If services were restarted or disabled, revert to their previous startup type using 'Set-Service -Name WinDefend -StartupType Automatic' and 'Start-Service -Name WinDefend'. 3. If a system file or driver was replaced, restore from a known good backup or use System File Checker (sfc /scannow). 4. If the issue persists after rollback, reapply the original configuration and contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
