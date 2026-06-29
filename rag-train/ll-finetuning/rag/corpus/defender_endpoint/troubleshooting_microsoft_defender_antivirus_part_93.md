# Troubleshooting: Microsoft Defender Antivirus (0x80508013)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508013 with message ERR_MP_BAD_USERDB_VERSION in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508013 displayed
- Message: ERR_MP_BAD_USERDB_VERSION ERR_MP_BAD_USERDB_VERSION

## Error Codes
- `0x80508013`
- `ERR_MP_BAD_USERDB_VERSION`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Applications and Services Logs' > 'Microsoft' > 'Windows' > 'Windows Defender' > 'Operational'.
3. Verify that no new events with ID 1006, 1007, or 1008 related to error 0x80508013 appear after remediation.
4. Run 'Get-MpComputerStatus' in PowerShell as Administrator and confirm 'AMServiceEnabled' and 'AntivirusEnabled' are both 'True'.
5. Perform a quick scan using 'Start-MpScan -ScanType QuickScan' and confirm it completes without error.

## Rollback
1. If the remediation involved registry changes, restore the previous registry state from a backup or export.
2. If the remediation involved reinstallation, reinstall Microsoft Defender Antivirus via 'Enable-WindowsOptionalFeature -Online -FeatureName Windows-Defender-ApplicationGuard' or use DISM.
3. Restore default security settings by running 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Set-MpPreference -DisableBehaviorMonitoring $false'.
4. Reboot the system to ensure all changes are reverted.
5. Verify the original error 0x80508013 reappears by checking Event Viewer for the same error events.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
