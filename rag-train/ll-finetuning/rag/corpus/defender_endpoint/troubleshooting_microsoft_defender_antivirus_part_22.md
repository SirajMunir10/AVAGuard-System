# Troubleshooting: Microsoft Defender Antivirus (1013)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1013 (MALWAREPROTECTION_MALWARE_HISTORY_DELETE) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1013 is logged in the event viewer
- Message: The antimalware platform deleted history of malware and other potentially unwanted software

## Error Codes
- `1013`

## Root Causes
1. Microsoft Defender Antivirus removed history of malware and other potentially unwanted software

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 1013 is present with the message: 'The antimalware platform deleted history of malware and other potentially unwanted software.'
4. Confirm that no related errors (e.g., Event ID 1006, 1007, 1008) appear in the same log.
5. Run the PowerShell command: Get-MpThreatDetection | Where-Object {$_.Action -eq 'HistoryDeleted'} to confirm the deletion action was recorded.

## Rollback
1. If Event ID 1013 indicates unintended deletion of history, restore the default antimalware policy by running: Set-MpPreference -DisableArchiveScanning $false -DisableBehaviorMonitoring $false -DisableBlockAtFirstSeen $false -DisableCatchupFullScan $false -DisableCatchupQuickScan $false -DisableCpuThrottleOnIdleScans $false -DisableDatagramProcessing $false -DisableDnsOverTcpParsing $false -DisableEmailScanning $false -DisableGradualRelease $false -DisableHttpParsing $false -DisableInboundConnectionFiltering $false -DisableNetworkProtection $false -DisablePrivacyMode $false -DisableRealtimeMonitoring $false -DisableRemovableDriveScanning $false -DisableRestorePoint $false -DisableScanningMappedNetworkDrivesForFullScan $false -DisableScanningNetworkFiles $false -DisableScriptScanning $false -EnableControlledFolderAccess Disabled -EnableNetworkProtection Disabled -PUAProtection Disabled -SubmitSamplesConsent NeverSend.
2. If the issue persists, reset the Windows Defender service by running: sc config WinDefend start=auto && net start WinDefend.
3. As a last resort, re-register the antimalware platform by running: 'C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24080.9-0\MpCmdRun.exe' -RemoveDefinitions -All && 'C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24080.9-0\MpCmdRun.exe' -SignatureUpdate.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
