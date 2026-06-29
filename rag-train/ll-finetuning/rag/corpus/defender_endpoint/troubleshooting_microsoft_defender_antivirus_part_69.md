# Troubleshooting: Microsoft Defender Antivirus (0x80508031)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508031 indicating Microsoft Defender Antivirus platform is outdated?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508031
- Message: ERROR_MP_PLATFORM_OUTDATED ERROR_MP_PLATFORM_OUTDATED

## Error Codes
- `0x80508031`

## Root Causes
1. Microsoft Defender Antivirus doesn't support the current version of the platform and requires a new version of the platform.

## Remediation Steps
1. You can only use Microsoft Defender Antivirus in Windows 10 and Windows 11. For Windows 8, Windows 7 and Windows Vista, you can use System Center Endpoint Protection.

## Validation
1. Run 'Get-MpComputerStatus' in PowerShell and verify that 'AMProductVersion' and 'AMEngineVersion' are not empty and show a version that is supported on your Windows 10 or Windows 11 build. 2. Check the Windows version by running 'winver' and confirm it is Windows 10 or Windows 11. 3. Attempt a manual update by running 'Update-MpSignature' and confirm no error 0x80508031 appears. 4. Review the Microsoft Defender Antivirus event log for Event ID 1150 or 1151 indicating successful platform update.

## Rollback
1. If the remediation fails, ensure the device is running Windows 10 or Windows 11; if not, upgrade the OS to a supported version. 2. If the error persists, run 'MpCmdRun.exe -RemoveDefinitions -All' to reset signature definitions, then re-run 'Update-MpSignature'. 3. As a last resort, uninstall and reinstall the Microsoft Defender Antivirus platform by running 'DISM /Online /Disable-Feature /FeatureName:Windows-Defender /Remove' followed by 'DISM /Online /Enable-Feature /FeatureName:Windows-Defender /All' (requires reboot).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
