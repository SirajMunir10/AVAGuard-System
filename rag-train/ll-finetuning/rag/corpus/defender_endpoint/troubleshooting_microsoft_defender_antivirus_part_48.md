# Troubleshooting: Microsoft Defender Antivirus (2042)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Event ID 2042 indicating the antimalware engine no longer supports the operating system and is no longer protecting the system from malware?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware engine no longer supports this operating system, and is no longer protecting your system from malware.

## Error Codes
- `2042`

## Root Causes
1. The support for your operating system has expired. Microsoft Defender Antivirus is no longer supported on your operating system, has stopped functioning, and isn't protecting against malware threats.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Verify that no new Event ID 2042 entries appear after remediation. 2. Run 'Get-MpComputerStatus' in PowerShell and confirm that 'AMServiceEnabled' and 'AntivirusEnabled' both show 'True'. 3. Check the Windows Security app to confirm that 'Virus & threat protection' shows a green checkmark and 'Real-time protection' is 'On'.

## Rollback
1. If the remediation involved upgrading the operating system, restore the previous OS version from backup or revert the upgrade using system recovery options. 2. If the remediation involved re-enabling Defender via registry or Group Policy, revert those changes: delete or set 'DisableAntiSpyware' to '0' (or remove the policy) and restart the 'WinDefend' service. 3. If the remediation involved installing an older engine version, reinstall the current engine via 'MpCmdRun -RemoveDefinitions -All' followed by 'MpCmdRun -SignatureUpdate'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
