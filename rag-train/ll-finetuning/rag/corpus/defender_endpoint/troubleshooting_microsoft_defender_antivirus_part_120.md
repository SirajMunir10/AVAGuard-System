# Troubleshooting: Microsoft Defender Antivirus (0x80501103)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501103 with message MP_ERROR_CODE_RDEVICE_S_ASYNC_CALL_PENDING in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501103 displayed
- Message: MP_ERROR_CODE_RDEVICE_S_ASYNC_CALL_PENDING

## Error Codes
- `0x80501103`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for Event ID 1006 (detection) or 5007 (configuration change) to confirm antivirus is active.
4. Run 'Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled, AntivirusEnabled' in PowerShell to verify real-time protection is enabled.
5. Run 'Start-MpScan -ScanType QuickScan' to initiate a scan and confirm no error 0x80501103 appears.

## Rollback
1. If the error persists after remediation, restore default settings by running 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Set-MpPreference -DisableBehaviorMonitoring $false' in PowerShell.
2. Reboot the device to clear any pending asynchronous calls.
3. If the issue continues, reinstall Microsoft Defender Antivirus via 'Uninstall-WindowsFeature -Name Windows-Defender' (if applicable) then 'Install-WindowsFeature -Name Windows-Defender'.
4. As a last resort, contact Microsoft Support with the error code and event logs.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
