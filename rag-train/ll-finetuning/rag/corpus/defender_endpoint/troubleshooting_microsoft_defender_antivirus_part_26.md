# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret non-remediating threat actions (Allow, No action, None) in Microsoft Defender Antivirus and understand associated events 1116 and 1117?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** ThreatSeverityDefaultAction set to None

## Symptoms
- Threat detected but not remediated based on configured security setting
- Allow action in 1117 event indicates detection without remediation

## Error Codes
N/A

## Root Causes
1. Non-remediating threat actions (Allow, No action, None) configured
2. ThreatSeverityDefaultAction set to None

## Remediation Steps
1. Use standard remediation actions (Clean, Quarantine, or Remove) in all other environments except specialized ones like industrial control systems or critical infrastructure
2. Do not configure Allow, No action, or None when tamper protection is enabled

## Validation
1. Verify current threat severity default actions: Get-MpPreference | Select-Object -Property *ThreatSeverityDefaultAction*
2. Confirm no 'Allow', 'No action', or 'None' values are set: Get-MpPreference | Where-Object { $_.ThreatSeverityDefaultAction -in @('Allow', 'No action', 'None') }
3. Check tamper protection status: Get-MpComputerStatus | Select-Object -Property IsTamperProtected
4. Review recent 1116 and 1117 events: Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; ID=1116,1117} | Select-Object TimeCreated, Id, LevelDisplayName, Message | Format-Table -AutoSize
5. Confirm remediation actions are now set to standard values (e.g., 'Clean', 'Quarantine', 'Remove'): Get-MpPreference | Select-Object -Property *ThreatSeverityDefaultAction*

## Rollback
1. If validation fails or issues arise, restore previous threat severity default actions: Set-MpPreference -ThreatSeverityDefaultAction <previous_value>
2. If tamper protection was disabled, re-enable it: Set-MpPreference -DisableTamperProtection $false
3. If standard remediation actions cause operational issues in specialized environments, revert to non-remediating actions: Set-MpPreference -ThreatSeverityDefaultAction 'None'
4. Monitor events 1116 and 1117 to confirm rollback: Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; ID=1116,1117} | Select-Object TimeCreated, Id, LevelDisplayName, Message | Format-Table -AutoSize

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
