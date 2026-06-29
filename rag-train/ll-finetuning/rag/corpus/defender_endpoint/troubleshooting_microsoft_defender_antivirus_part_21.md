# Troubleshooting: Microsoft Defender Antivirus (1012)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when Microsoft Defender Antivirus cannot delete an item from quarantine with Event ID 1012?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware platform couldn't delete an item from quarantine.

## Error Codes
- `1012`

## Root Causes
1. Microsoft Defender Antivirus encountered an error trying to delete an item from quarantine.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Verify that no new Event ID 1012 errors appear after remediation.
2. Run 'Get-MpThreatDetection' in PowerShell to confirm the specific threat is no longer listed.
3. Run 'Get-MpThreat' to ensure no threats remain in quarantine for the affected item.
4. Attempt to manually delete the quarantined item using 'Remove-MpThreat -ThreatID <ThreatID>' and confirm success with no errors.

## Rollback
1. If validation fails, restore the original quarantine state by running 'Restore-MpThreat -ThreatID <ThreatID>' for each affected threat.
2. Reapply any custom exclusions or policies that were modified during remediation using 'Set-MpPreference'.
3. Restart the 'WinDefend' service with 'Restart-Service WinDefend' to revert any service changes.
4. If registry changes were made, restore the previous values from a backup or use 'reg delete' to remove added keys.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
