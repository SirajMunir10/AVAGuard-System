# Troubleshooting: Microsoft Defender Antivirus (0x80501002)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501002 (ERROR_MP_NOENGINE) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501002 displayed
- Message displayed: ERROR_MP_NOENGINE

## Error Codes
- `0x80501002`
- `ERROR_MP_NOENGINE`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and verify that 'Virus & threat protection' shows 'No action needed' and the shield icon is green.
2. Run 'Get-MpComputerStatus' in PowerShell as Administrator and confirm 'AMServiceEnabled' is True, 'AntivirusEnabled' is True, and 'RealTimeProtectionEnabled' is True.
3. Perform a quick scan using 'Start-MpScan -ScanType QuickScan' and verify it completes without error code 0x80501002.
4. Check the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for any recent events with ID 1000 or 1001 indicating engine load success.

## Rollback
1. If the remediation involved a system restore point, run 'rstrui.exe' and follow the wizard to revert to a point before changes were made.
2. If registry keys were modified (e.g., under HKLM\SOFTWARE\Policies\Microsoft\Windows Defender), restore the previous values from a backup or delete the added keys.
3. If services were stopped and restarted, run 'net start WinDefend' to ensure the service is running, and set startup type to automatic via 'sc config WinDefend start= auto'.
4. If the engine was manually replaced, restore the original mpengine.dll from a backup or run 'Start-MpWDOScan' to trigger a fresh engine download from Microsoft Update.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
