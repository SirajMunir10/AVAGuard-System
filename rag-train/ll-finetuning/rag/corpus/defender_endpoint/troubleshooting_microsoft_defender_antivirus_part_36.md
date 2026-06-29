# Troubleshooting: Microsoft Defender Antivirus (Event ID 2005)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 2005 indicating the antimalware engine failed to load because the antimalware platform is out of date?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2005 with symbolic name MALWAREPROTECTION_ENGINE_UPDATE_PLATFORMOUTOFDATE
- Message: The antimalware engine failed to load because the antimalware platform is out of date. The antimalware platform loads the last-known good antimalware engine and attempt to update.
- Description: Microsoft Defender Antivirus couldn't load antimalware engine because current platform version isn't supported. Microsoft Defender Antivirus reverts back to the last known-good engine and a platform update will be attempted.

## Error Codes
- `Event ID 2005`
- `MALWAREPROTECTION_ENGINE_UPDATE_PLATFORMOUTOFDATE`

## Root Causes
1. The antimalware platform is out of date.

## Remediation Steps
N/A

## Validation
1. Run 'Get-MpComputerStatus' in PowerShell to verify the AMProductVersion and AMEngineVersion fields show the latest platform and engine versions. 2. Check the Microsoft Defender Antivirus event log for Event ID 2005; confirm it no longer appears after remediation. 3. Run 'Get-MpPreference' to ensure DisableRealtimeMonitoring is set to False. 4. Verify the service 'WinDefend' is running using 'Get-Service WinDefend'.

## Rollback
1. If the platform update fails, restore the previous platform version by running 'Start-MpWDOScan' to force a scan and update attempt. 2. If issues persist, reinstall the antimalware platform using 'Uninstall-WindowsFeature -Name Windows-Defender' followed by 'Install-WindowsFeature -Name Windows-Defender' (requires reboot). 3. Alternatively, use 'MpCmdRun.exe -RemoveDefinitions -All' to reset engine definitions, then run 'MpCmdRun.exe -SignatureUpdate' to re-download. 4. As a last resort, restore from a system backup or use System Restore to a point before the update.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
