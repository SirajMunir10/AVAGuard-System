# Troubleshooting: Microsoft Defender Antivirus (1008)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 1008 (MALWAREPROTECTION_MALWARE_ACTION_FAILED) where Microsoft Defender Antivirus failed to perform an action on malware or potentially unwanted software?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware platform attempted to perform an action to protect your system from malware or other potentially unwanted software, but the action failed.

## Error Codes
- `1008`

## Root Causes
1. Microsoft Defender Antivirus encountered an error when taking action on malware or other potentially unwanted software.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for Event ID 1008 entries after remediation. If none appear, the issue is resolved.
4. Run 'Get-MpThreatDetection' in PowerShell to confirm no recent detection failures.
5. Verify Microsoft Defender Antivirus is up to date: 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled'.

## Rollback
1. If remediation introduced issues, restore previous Microsoft Defender Antivirus settings via Group Policy or local registry backup.
2. Revert any exclusion changes: Remove added file/folder/process exclusions using 'Set-MpPreference -ExclusionPath @()' or Group Policy.
3. If signature updates were forced, roll back to previous engine version using 'Set-MpPreference -DisableRealtimeMonitoring $true' temporarily, then re-enable after restoring signatures.
4. Restore default Microsoft Defender Antivirus configuration: 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Update-MpSignature -Rollback'.
5. Reboot the device if services were restarted or modified.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
