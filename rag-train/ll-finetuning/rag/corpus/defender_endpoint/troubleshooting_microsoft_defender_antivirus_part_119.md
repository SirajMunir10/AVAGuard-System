# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify Controlled folder access events in Windows Event Log?

## Environment Context
- **Tenant Type:** on-premises
- **Configuration:** Controlled folder access enabled or in audit mode

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Block disk modification only mode: logs can be found in Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational > ID 1123.
2. For Audit disk modification only mode: logs can be found in Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational > ID 1124.

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Check for event ID 1123 (block mode) or 1124 (audit mode) to confirm Controlled folder access events are being logged.
4. Alternatively, run the following PowerShell command to query the log:
   Get-WinEvent -LogName Microsoft-Windows-Windows Defender/Operational | Where-Object { $_.Id -eq 1123 -or $_.Id -eq 1124 }

## Rollback
1. If Controlled folder access is enabled and causing issues, disable it via Group Policy or PowerShell:
   - Group Policy: Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Controlled Folder Access > Configure Controlled Folder Access > set to 'Disabled'.
   - PowerShell: Set-MpPreference -EnableControlledFolderAccess Disabled
2. If in audit mode and logs are excessive, switch to block mode or disable audit:
   - Set-MpPreference -EnableControlledFolderAccess AuditMode (to keep audit) or Disabled (to stop logging).
3. Restart the Microsoft Defender Antivirus service if needed: Restart-Service -Name WinDefend

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
