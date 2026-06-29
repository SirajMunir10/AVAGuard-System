# Troubleshooting: Microsoft Defender Antivirus (5007)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate unexpected Event ID 5007 indicating antimalware platform configuration changes in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 5007 is logged with MALWAREPROTECTION_CONFIG_CHANGED message
- Antimalware platform configuration changed unexpectedly

## Error Codes
- `5007`

## Root Causes
1. The event might be the result of malware

## Remediation Steps
1. Review the settings as the event might be the result of malware

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 2. Verify that Event ID 5007 entries show the expected configuration changes (e.g., from policy updates or user actions) and not unexpected modifications. 3. Run 'Get-MpComputerStatus' in PowerShell to confirm current antimalware platform version and signature state. 4. Check for any active malware alerts in Microsoft Defender for Endpoint portal (security.microsoft.com) under Incidents & Alerts.

## Rollback
1. If malware is suspected, run a full scan with 'Start-MpScan -ScanType FullScan' and follow remediation steps for any detected threats. 2. Restore any changed settings to their original values using Group Policy or 'Set-MpPreference' commands. 3. If the platform was updated unexpectedly, reinstall the previous version using 'Uninstall-WindowsFeature -Name Windows-Defender' (if applicable) or contact support for rollback guidance. 4. Review and reapply security baselines from Microsoft Security Compliance Toolkit.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
