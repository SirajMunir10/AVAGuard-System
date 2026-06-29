# Troubleshooting: Microsoft Defender Antivirus (1011)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1011 indicating that Microsoft Defender Antivirus deleted an item from quarantine?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1011 is logged with the symbolic name MALWAREPROTECTION_QUARANTINE_DELETE

## Error Codes
- `1011`

## Root Causes
1. Microsoft Defender Antivirus deleted an item from quarantine

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for Event ID 1011 with source 'Microsoft-Windows-Windows Defender' and verify the event details include the file path and threat name of the deleted quarantine item.
4. Confirm that the deletion was intentional by checking the corresponding policy or user action (e.g., manual deletion from quarantine or automatic cleanup based on retention settings).
5. Optionally, run 'Get-MpThreatDetection' in PowerShell to list recent detections and verify the item is no longer present in quarantine.

## Rollback
1. If the deletion was accidental, restore the item from quarantine using the Microsoft Defender Antivirus quarantine interface or PowerShell:
   - Open Windows Security > Virus & threat protection > Protection history.
   - Locate the quarantined item and select 'Restore'.
   - Or run: Restore-MpThreatDetection -ThreatID <ThreatID> (replace <ThreatID> with the ID from the event).
2. If automatic cleanup caused the deletion, adjust the quarantine retention policy:
   - Set the registry key 'HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Quarantine\PurgeItemsAfterDelay' to a higher value (default is 30 days).
3. Verify the restored item is no longer flagged as a threat by running a custom scan on the original file location.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
