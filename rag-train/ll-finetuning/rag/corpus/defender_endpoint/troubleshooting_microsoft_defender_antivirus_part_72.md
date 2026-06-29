# Troubleshooting: Microsoft Defender Antivirus (0x80501000)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x80501000 in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501000 displayed
- Message displayed: ERROR_MP_UI_CONSOLIDATION_BASE ERROR_MP_UI_CONSOLIDATION_BASE

## Error Codes
- `0x80501000`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for event ID 1000 or 1001 related to error 0x80501000. If none found, the issue is resolved.
4. Run 'Get-MpComputerStatus' in PowerShell as Administrator. Verify 'AntivirusEnabled' is True and 'AMServiceEnabled' is True.
5. Run 'Start-MpScan -ScanType QuickScan' to confirm scanning works without error.

## Rollback
1. If validation fails, restore the previous state:
   - If any registry changes were made, restore from backup or revert to known good values.
   - If service settings were modified, run 'Set-Service WinDefend -StartupType Automatic' and 'Start-Service WinDefend'.
2. Reinstall Microsoft Defender Antivirus via 'DISM /Online /Disable-Feature /FeatureName:Windows-Defender-ApplicationGuard' then re-enable.
3. If issue persists, contact Microsoft Support with event logs and error details.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
