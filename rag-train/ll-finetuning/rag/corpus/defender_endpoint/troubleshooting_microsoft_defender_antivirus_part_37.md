# Troubleshooting: Microsoft Defender Antivirus (Error code: Error code Result code associated with threat status. Standard HRESULT values.)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus platform update failure with Event ID 2006?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2006 with symbolic name MALWAREPROTECTION_PLATFORM_UPDATE_FAILED
- Message: The platform update failed

## Error Codes
- `Error code: Error code Result code associated with threat status. Standard HRESULT values.`

## Root Causes
1. Microsoft Defender Antivirus encountered an error trying to update the platform

## Remediation Steps
N/A

## Validation
1. Check the latest platform update status by running 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled' in PowerShell. Confirm AMProductVersion matches the latest version listed at https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/manage-updates-baselines-microsoft-defender-antivirus. 2. Verify no recent Event ID 2006 errors in Event Viewer under 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational'. 3. Run 'MpCmdRun -ValidateMapsConnection' to confirm connectivity to Microsoft Update services.

## Rollback
1. If the platform update fails, restore the previous platform version by running 'MpCmdRun -RevertPlatform' in an elevated command prompt. 2. If the issue persists, manually download and install the latest platform update from https://www.microsoft.com/en-us/wdsi/defenderupdates. 3. As a last resort, reinstall Microsoft Defender Antivirus by running 'DISM /Online /Disable-Feature /FeatureName:Windows-Defender-ApplicationGuard /Remove /NoRestart' followed by 'DISM /Online /Enable-Feature /FeatureName:Windows-Defender-ApplicationGuard /All /NoRestart' and then restart the device.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
