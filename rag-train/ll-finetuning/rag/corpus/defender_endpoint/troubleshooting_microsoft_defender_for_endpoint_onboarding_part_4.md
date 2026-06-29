# Troubleshooting: Microsoft Defender for Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when the onboarding script fails to find the needed onboarding status registry value?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The script failed to find needed onboarding status registry value

## Error Codes
N/A

## Root Causes
1. When the SENSE service starts for the first time, it writes onboarding status to the registry location HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status. The script failed to find it after several seconds.

## Remediation Steps
1. You can manually test it and check if it's there.
2. For more information on events and errors related to SENSE, see Review events and errors using Event viewer.

## Validation
1. Open Registry Editor (regedit.exe) as Administrator. 2. Navigate to HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status. 3. Verify that the key exists and contains values such as 'OnboardingState' (expected: 1) and 'OrgId'. 4. Alternatively, run from an elevated command prompt: reg query "HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status" /s. 5. Confirm the SENSE service is running: sc query sense | find "STATE". 6. Review Event Viewer under Applications and Services Logs > Microsoft > Windows > SENSE for any errors.

## Rollback
1. If the registry key is missing or incorrect, re-run the onboarding script from an elevated command prompt. 2. If the SENSE service fails to start, restart it: net start sense. 3. If issues persist, check Event Viewer for SENSE operational logs and consult 'Review events and errors using Event viewer' as referenced in the documentation. 4. As a last resort, reinstall the Microsoft Defender for Endpoint agent using the official deployment package.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
