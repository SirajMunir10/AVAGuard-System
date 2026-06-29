# Troubleshooting: Microsoft Defender Antivirus (0x80508002)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508002 with message ERR_MP_BAD_DATABASE in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508002 displayed
- Message displayed: ERR_MP_BAD_DATABASE ERR_MP_BAD_DATABASE

## Error Codes
- `0x80508002`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to Virus & threat protection > Protection updates > Check for updates. Confirm no error appears. 2. Run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled' in PowerShell as Administrator and verify AMServiceEnabled is True and version fields are populated. 3. Run 'MpCmdRun -ValidateMapsConnection' and confirm output shows 'Successfully validated MAPS connection'. 4. Run a quick scan with 'Start-MpScan -ScanType QuickScan' and verify no error 0x80508002 is returned.

## Rollback
1. If validation fails, restore the previous Microsoft Defender Antivirus engine and platform versions by running 'MpCmdRun -RemoveDefinitions -All' to reset to default definitions, then run 'MpCmdRun -SignatureUpdate' to re-download latest. 2. If the issue persists, use System Restore to revert to a point before the remediation was applied. 3. As a last resort, reinstall Microsoft Defender Antivirus via 'DISM /Online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart' followed by 'DISM /Online /Enable-Feature /FeatureName:Windows-Defender /All /NoRestart' and restart.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
