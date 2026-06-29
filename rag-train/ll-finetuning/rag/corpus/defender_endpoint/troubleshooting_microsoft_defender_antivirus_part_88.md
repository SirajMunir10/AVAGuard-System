# Troubleshooting: Microsoft Defender Antivirus (0x8050800E)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x8050800E with message ERR_MP_OBSOLETE in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x8050800E displayed
- Message displayed: ERR_MP_OBSOLETE ERR_MP_OBSOLETE

## Error Codes
- `0x8050800E`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc) and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Look for event ID 1000 or 1001 that indicates the engine is up to date. 2. Run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, NISEngineVersion' in PowerShell to confirm the antivirus engine versions are current. 3. Run 'Start-MpScan -ScanType QuickScan' to verify a scan completes without error 0x8050800E.

## Rollback
1. If the engine update caused issues, run 'Uninstall-WindowsFeature -Name Windows-Defender' (if applicable) or use 'Add-WindowsFeature -Name Windows-Defender' to reinstall. 2. Restore previous engine version by running 'Set-MpPreference -DisableRealtimeMonitoring $true' then manually install an older engine package from Microsoft Update Catalog. 3. Reboot the device and verify the error returns by running 'Start-MpScan -ScanType QuickScan'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
