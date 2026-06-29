# Troubleshooting: Microsoft Defender Antivirus (5004)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus when Event ID 5004 is logged indicating real-time protection configuration changes?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 5004 is logged with symbolic name MALWAREPROTECTION_RTP_FEATURE_CONFIGURED
- Message: The real-time protection configuration changed
- Description: Microsoft Defender Antivirus real-time protection feature configuration changed. Feature: Feature. Examples: On Access, IE downloads and Outlook Express attachments, Behavior monitoring, or Network Inspection System Configuration

## Error Codes
- `5004`

## Root Causes
1. Real-time protection feature configuration changed

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Applications and Services Logs' > 'Microsoft' > 'Windows' > 'Windows Defender' > 'Operational'.
3. Verify that Event ID 5004 is no longer logged after the configuration change.
4. Run the PowerShell command: Get-MpPreference | Select-Object -Property DisableRealtimeMonitoring, DisableBehaviorMonitoring, DisableIOAVProtection, DisableScriptScanning, EnableNetworkProtection, EnableControlledFolderAccess
5. Confirm that the returned values match the intended configuration (e.g., DisableRealtimeMonitoring should be False if real-time protection is enabled).
6. Run the PowerShell command: Get-MpComputerStatus | Select-Object -Property AMServiceEnabled, AntispywareEnabled, AntivirusEnabled, BehaviorMonitorEnabled, IoavProtectionEnabled, NisEnabled, OnAccessProtectionEnabled, RealTimeProtectionEnabled
7. Ensure all relevant protection features show 'True' as expected.

## Rollback
1. Open PowerShell as Administrator.
2. To restore real-time protection to its previous state, run: Set-MpPreference -DisableRealtimeMonitoring $false
3. If behavior monitoring was disabled, run: Set-MpPreference -DisableBehaviorMonitoring $false
4. If IOAV protection was disabled, run: Set-MpPreference -DisableIOAVProtection $false
5. If network protection was enabled and needs to be disabled, run: Set-MpPreference -EnableNetworkProtection Disabled
6. If controlled folder access was enabled and needs to be disabled, run: Set-MpPreference -EnableControlledFolderAccess Disabled
7. After reverting, verify the configuration using: Get-MpPreference | Select-Object -Property DisableRealtimeMonitoring, DisableBehaviorMonitoring, DisableIOAVProtection, DisableScriptScanning, EnableNetworkProtection, EnableControlledFolderAccess
8. Confirm that Event ID 5004 is no longer logged unexpectedly.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
