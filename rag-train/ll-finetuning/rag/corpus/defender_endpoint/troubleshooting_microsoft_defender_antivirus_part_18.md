# Troubleshooting: Microsoft Defender Antivirus (1009)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1009 when Microsoft Defender Antivirus restores an item from quarantine?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1009 is logged with message: The antimalware platform restored an item from quarantine.

## Error Codes
- `1009`

## Root Causes
1. Microsoft Defender Antivirus restored an item from quarantine.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 1009 is present with the message: 'The antimalware platform restored an item from quarantine.'
4. Confirm the restored file path and timestamp match the expected restoration activity.
5. Optionally, run Get-MpThreatDetection | Where-Object {$_.Resources -like '*<filepath>*'} in PowerShell to verify the detection history shows the item as restored.

## Rollback
1. If the restoration was unintended, immediately run Add-MpThreat -ThreatID <ThreatID> -Action Quarantine in PowerShell to re-quarantine the item.
2. Alternatively, use the Windows Security app: go to Virus & threat protection > Protection history, locate the restored item, and select 'Quarantine'.
3. Verify the action by checking Event ID 1009 is no longer logged for that item and that Event ID 1006 (detection) or 1008 (remediation) appears instead.
4. If the item was restored due to a false positive, submit the file to Microsoft for analysis via the Microsoft 365 Defender portal.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
