# Implementation: Attack Surface Reduction Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction Rules
**Incident Type:** Implementation

## Scenario / Query
How to implement the ASR rule 'Block Win32 API calls from Office macros' in Microsoft Intune or Configuration Manager?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus, Antimalware Scan Interface (AMSI), cloud-delivered protection must be enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable cloud-delivered protection for Microsoft Defender Antivirus.
2. Deploy the ASR rule with GUID 92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b via Intune or Configuration Manager.
3. Note: This rule is not supported when deployed via Microsoft Intune to Windows Server 2012 R2 or Windows Server 2016 using the modern unified solution.
4. Configure per-ASR rule exclusions or use the Allow action for an indicator of compromise (IoC) if benign unknown files are blocked and do not resolve in a timely manner.

## Validation
1. Verify cloud-delivered protection is enabled: Run 'Get-MpPreference | Select-Object CloudBlockLevel, CloudTimeout' in PowerShell. Confirm CloudBlockLevel is not 0 and CloudTimeout is set appropriately. 2. Confirm the ASR rule is deployed: In Intune, navigate to Endpoint Security > Attack Surface Reduction, select the policy, and verify the rule 'Block Win32 API calls from Office macros' (GUID 92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b) is set to 'Block' or 'Audit'. In Configuration Manager, check the ASR policy under Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard > Attack Surface Reduction. 3. Test the rule: On a managed device, open an Office app (e.g., Word) and attempt to run a macro that calls Win32 APIs. The macro should be blocked and an event (e.g., Event ID 1121) should appear in Microsoft-Windows-Windows Defender/Operational log. 4. Review Microsoft 365 Defender portal: Go to Reports > Attack surface reduction rules and confirm the rule is generating alerts or blocks.

## Rollback
1. Disable the ASR rule: In Intune, edit the ASR policy, set the rule 'Block Win32 API calls from Office macros' to 'Disabled' or 'Not configured', and save. In Configuration Manager, modify the ASR policy to remove the rule or set it to 'Disabled'. 2. If cloud-delivered protection was enabled solely for this rule and needs to be disabled, run 'Set-MpPreference -CloudBlockLevel 0' in PowerShell. 3. Remove any per-rule exclusions or Allow indicators added for this rule: In Microsoft 365 Defender, go to Settings > Endpoints > Indicators, and delete any entries with the rule GUID 92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b. 4. Force policy refresh: On affected devices, run 'Start-MpWDOScan' or wait for the next policy sync (typically every 8 hours).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
