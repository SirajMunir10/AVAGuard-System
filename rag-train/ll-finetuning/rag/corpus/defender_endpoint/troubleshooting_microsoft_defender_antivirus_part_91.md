# Troubleshooting: Microsoft Defender Antivirus (0x80508011)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508011 with message ERR_MP_DUPLICATE_SCANID in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508011 displayed
- Message displayed: ERR_MP_DUPLICATE_SCANID

## Error Codes
- `0x80508011`
- `ERR_MP_DUPLICATE_SCANID`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Look for event ID 1006, 1007, or 1008 to confirm no duplicate scan ID errors are logged. 2. Run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled' in PowerShell to verify Microsoft Defender Antivirus is running and up to date. 3. Perform a manual quick scan by running 'Start-MpScan -ScanType QuickScan' and confirm no error 0x80508011 appears.

## Rollback
1. If the error persists, restart the Microsoft Defender Antivirus service by running 'Restart-Service -Name WinDefend' in PowerShell as Administrator. 2. If the issue continues, reset the Microsoft Defender Antivirus configuration by running 'Set-MpPreference -DisableRealtimeMonitoring $false' and then 'Update-MpSignature' to force signature update. 3. As a last resort, reinstall Microsoft Defender Antivirus by running 'Uninstall-WindowsFeature -Name Windows-Defender' followed by 'Install-WindowsFeature -Name Windows-Defender' in PowerShell, then reboot the system.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
