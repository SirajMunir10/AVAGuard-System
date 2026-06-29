# Troubleshooting: Microsoft Defender Antivirus (1007)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1007 (MALWAREPROTECTION_MALWARE_ACTION_TAKEN) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1007 is logged with message: The antimalware platform performed an action to protect your system from malware or other potentially unwanted software.

## Error Codes
- `1007`

## Root Causes
1. Microsoft Defender Antivirus took action to protect the machine from malware or other potentially unwanted software.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for Event ID 1007 entries. Verify that the event message includes 'The antimalware platform performed an action to protect your system from malware or other potentially unwanted software.'
4. Confirm that the action taken (e.g., quarantine, remove) is appropriate for the detected threat.
5. Check that no subsequent Event ID 1006 (detection) or 1008 (action failed) events are logged for the same threat.
6. Run the PowerShell command: Get-MpThreatDetection | Where-Object {$_.Action -ne 'NoAction'} | Format-List Action, ThreatName, Resources to verify the action taken matches the event log.

## Rollback
1. If the action taken was incorrect (e.g., false positive), restore the quarantined item:
   - Open Windows Security > Virus & threat protection > Protection history.
   - Select the detected threat and choose 'Allow' or 'Restore'.
   - Alternatively, use PowerShell: Restore-MpThreatDetection -ThreatID <ThreatID>.
2. Add the file or process to the exclusion list to prevent future false positives:
   - Open Windows Security > Virus & threat protection > Manage settings > Exclusions.
   - Add the file, folder, file type, or process.
   - Or use PowerShell: Add-MpPreference -ExclusionPath 'C:\path\to\file'.
3. If the action was taken by a scheduled scan or real-time protection, consider disabling real-time protection temporarily (not recommended for long-term):
   - Open Windows Security > Virus & threat protection > Manage settings > Real-time protection > Off.
   - Or use PowerShell: Set-MpPreference -DisableRealtimeMonitoring $true.
4. Re-enable real-time protection after troubleshooting: Set-MpPreference -DisableRealtimeMonitoring $false.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
