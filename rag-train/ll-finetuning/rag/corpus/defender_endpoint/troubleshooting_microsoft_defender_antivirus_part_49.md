# Troubleshooting: Microsoft Defender Antivirus (2050)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
What does Event ID 2050 indicate in Microsoft Defender Antivirus and what action is required?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2050 is logged with symbolic name MALWAREPROTECTION_SAMPLESUBMISSION_UPLOADED
- Message: The antimalware platform submitted a file for sample analysis
- Description: A file was submitted to the cloud for further analysis as part of the automatic sample submission feature

## Error Codes
- `2050`

## Root Causes
1. The file was submitted based on the sample submission consent configuration
2. By default, Microsoft Defender Antivirus automatically sends files that don't contain personally identifiable information (PII)

## Remediation Steps
N/A

## Validation
1. Confirm that Event ID 2050 is logged with the expected details: Open Event Viewer > Windows Logs > System. Look for Event ID 2050 from source 'Microsoft-Windows-Windows Defender' with message containing 'MALWAREPROTECTION_SAMPLESUBMISSION_UPLOADED' and 'The antimalware platform submitted a file for sample analysis'. 2. Verify the automatic sample submission configuration: Run 'Get-MpPreference' in PowerShell as Administrator and check the value of 'SubmitSamplesConsent'. If set to 1 (Send safe samples automatically) or 2 (Send all samples automatically), the event is expected. 3. Ensure no other related errors (e.g., Event ID 2051 for submission failure) are present in the same timeframe.

## Rollback
1. If the automatic sample submission is causing unintended data sharing, disable it: Run 'Set-MpPreference -SubmitSamplesConsent 0' in PowerShell as Administrator. 2. To revert to default behavior, set the consent back to the default value: 'Set-MpPreference -SubmitSamplesConsent 1' (send safe samples automatically). 3. If the event was triggered by a specific file and you want to prevent future submissions of similar files, configure exclusions: Use 'Add-MpPreference -ExclusionPath "<path>"' or 'Add-MpPreference -ExclusionExtension "<extension>"'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
