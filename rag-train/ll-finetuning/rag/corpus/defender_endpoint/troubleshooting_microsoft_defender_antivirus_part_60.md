# Troubleshooting: Microsoft Defender Antivirus (5100)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus expiration warning event ID 5100?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 5100 with symbolic name MALWAREPROTECTION_EXPIRATION_WARNING_STATE is logged
- Message: The antimalware platform expires soon
- Microsoft Defender Antivirus entered a grace period and will soon expire
- After expiration, this program will disable protection against viruses, spyware, and other potentially unwanted software

## Error Codes
- `5100`

## Root Causes
1. Expiration Reason: The reason Microsoft Defender Antivirus expires
2. Expiration Date: The date Microsoft Defender Antivirus expires

## Remediation Steps
N/A

## Validation
1. Run 'Get-MpComputerStatus' in PowerShell and verify that 'AMProductVersion' and 'AMEngineVersion' are not null and show a current version. 2. Check the 'AntivirusSignatureLastUpdated' field to confirm signatures are up to date. 3. Review the System event log for Event ID 5100; ensure no new occurrences appear after remediation. 4. Confirm that Microsoft Defender Antivirus real-time protection is enabled by running 'Get-MpPreference | Select-Object -Property DisableRealtimeMonitoring' and verifying it returns 'False'.

## Rollback
1. If the remediation involved updating the platform, revert to the previous version by running 'Uninstall-WindowsUpdate -KBArticleId <KB_ID>' (if applicable) or reinstall the previous version from a backup. 2. If a registry change was made, restore the original value from a backup or set it back to the pre-remediation state. 3. If a service was restarted or stopped, restart the service using 'Start-Service WinDefend' and set its startup type to 'Automatic' via 'Set-Service WinDefend -StartupType Automatic'. 4. If a policy change was applied, revert the policy to its previous configuration using Group Policy Management Console or Intune.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
