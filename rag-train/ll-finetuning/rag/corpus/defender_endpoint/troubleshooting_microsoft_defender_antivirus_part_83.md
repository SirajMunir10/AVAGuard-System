# Troubleshooting: Microsoft Defender Antivirus (0x80501108)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501108 with message MP_ERROR_SIG_BACKUP_DISABLED in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501108 displayed
- Message: MP_ERROR_SIG_BACKUP_DISABLED

## Error Codes
- `0x80501108`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to 'Virus & threat protection' > 'Manage settings' to verify real-time protection is on. 2. Run 'Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled, AntispywareEnabled' in PowerShell to confirm all protection features are enabled. 3. Check for the specific error code by running 'Get-MpThreatDetection | Where-Object {$_.ErrorCode -eq 0x80501108}' to ensure no active detections with that error. 4. Verify the Microsoft Defender Antivirus service status with 'Get-Service WinDefend' to confirm it is running. 5. Review the latest Microsoft Defender Antivirus event logs (Event ID 1006, 1007, 1008) in Event Viewer under 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational' to confirm no recurrence of error 0x80501108.

## Rollback
1. If validation fails or issues arise, restore the previous Microsoft Defender Antivirus configuration by running 'Set-MpPreference -DisableRealtimeMonitoring $false' to re-enable real-time protection if it was disabled. 2. Revert any changes to group policies or registry keys related to Microsoft Defender Antivirus by restoring from a backup or setting them to their original values. 3. If the service was restarted, ensure it is running with 'Start-Service WinDefend'. 4. If the error persists, consider running the Microsoft Support and Recovery Assistant for Office 365 or performing a system restore to a point before the remediation was applied. 5. As a last resort, reset Microsoft Defender Antivirus settings to default using 'Set-MpPreference -Force' and then reapply any custom configurations.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
