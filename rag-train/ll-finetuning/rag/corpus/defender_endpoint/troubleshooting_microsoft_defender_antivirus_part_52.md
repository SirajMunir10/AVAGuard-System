# Troubleshooting: Microsoft Defender Antivirus (5000)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that Microsoft Defender Antivirus real-time protection is enabled using Event ID 5000?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 5000 with symbolic name MALWAREPROTECTION_RTP_ENABLED appears in event logs

## Error Codes
- `5000`

## Root Causes
1. Microsoft Defender Antivirus real-time protection scanning for malware and other potentially unwanted software was enabled

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Applications and Services Logs' > 'Microsoft' > 'Windows' > 'Windows Defender' > 'Operational'.
3. Look for Event ID 5000 with source 'Windows Defender' and level 'Information'.
4. Confirm the event description contains 'Microsoft Defender Antivirus Real-Time Protection scanning for malware and other potentially unwanted software was enabled.'
5. Alternatively, run in PowerShell: Get-WinEvent -LogName 'Microsoft-Windows-Windows Defender/Operational' | Where-Object { $_.Id -eq 5000 } | Format-List TimeCreated, Message

## Rollback
1. Open Windows Security app (windowsdefender://).
2. Go to 'Virus & threat protection' > 'Virus & threat protection settings'.
3. Turn off 'Real-time protection' (toggle to Off).
4. Confirm the change when prompted by User Account Control.
5. Verify in Event Viewer that Event ID 5001 (Real-Time Protection disabled) appears in the same log.
6. Alternatively, run in PowerShell with admin rights: Set-MpPreference -DisableRealtimeMonitoring $true

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
