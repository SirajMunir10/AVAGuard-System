# Troubleshooting: Microsoft Defender Antivirus (0x80501001)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501001 (ERROR_MP_ACTIONS_FAILED) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501001 displayed
- Message displayed: ERROR_MP_ACTIONS_FAILED ERROR_MP_ACTIONS_FAILED

## Error Codes
- `0x80501001`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to 'Virus & threat protection' > 'Protection updates' > 'Check for updates'. Confirm no error is displayed.
2. Run 'Get-MpComputerStatus' in PowerShell as Administrator and verify 'AMServiceEnabled', 'AntivirusEnabled', and 'RealTimeProtectionEnabled' are all True.
3. Run 'Start-MpScan -ScanType QuickScan' in PowerShell as Administrator and confirm the scan completes without error code 0x80501001.
4. Check the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1000 or 1001 indicating successful scan completion.

## Rollback
1. If validation fails, restore any modified registry keys from backup: regedit.exe > File > Import the backup .reg file.
2. Re-run the Microsoft Defender Antivirus uninstall/reinstall commands if applicable: 'DISM /Online /Disable-Feature /FeatureName:Windows-Defender-ApplicationGuard /Remove' then re-enable via 'DISM /Online /Enable-Feature /FeatureName:Windows-Defender-ApplicationGuard /All'.
3. Reset Microsoft Defender Antivirus settings to default using PowerShell: 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Set-MpPreference -DisableBehaviorMonitoring $false'.
4. Reboot the device and re-attempt the original remediation steps.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
