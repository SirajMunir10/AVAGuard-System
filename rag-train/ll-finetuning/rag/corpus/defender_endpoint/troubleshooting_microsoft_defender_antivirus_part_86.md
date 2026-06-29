# Troubleshooting: Microsoft Defender Antivirus (0x80508004)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508004 with message ERR_MP_BAD_UFS in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508004 displayed
- Message displayed: ERR_MP_BAD_UFS ERR_MP_BAD_UFS

## Error Codes
- `0x80508004`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to 'Virus & threat protection' > 'Protection updates' > 'Check for updates'. Confirm no error is displayed. 2. Run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled' in PowerShell as Administrator and verify the engine version is current and AMServiceEnabled is True. 3. Run 'MpCmdRun -SignatureUpdate' from an elevated command prompt and confirm it completes without error code 0x80508004.

## Rollback
1. If the issue persists, run 'MpCmdRun -RemoveDefinitions -All' from an elevated command prompt to reset signature definitions. 2. Reinstall Microsoft Defender Antivirus by running 'DISM /Online /Disable-Feature /FeatureName:Windows-Defender-ApplicationGuard /Remove /NoRestart' then 'DISM /Online /Enable-Feature /FeatureName:Windows-Defender-ApplicationGuard /All /NoRestart' and restart the device. 3. If the error returns, contact Microsoft Support with the error code and system logs.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
