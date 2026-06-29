# Implementation: Attack Surface Reduction Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction Rules
**Incident Type:** Implementation

## Scenario / Query
How to implement the ASR rule 'Use advanced protection against ransomware' in Microsoft Intune or Configuration Manager?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus, Cloud Protection

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure Microsoft Defender Antivirus and Cloud Protection are enabled.
2. Deploy the ASR rule with GUID c1db55ab-c21a-4637-bb3f-a12568109d35 via Intune or Configuration Manager.
3. Note: This rule uses both client and cloud heuristics to determine whether a file resembles ransomware.
4. The rule does not block files that are found to be unharmful in the Microsoft cloud, are valid signed files, or are prevalent enough to not be considered ransomware.
5. If blocks on benign unknown files do not resolve in a timely manner, configure a per-ASR rule exclusion or use the Allow action for an indicator of compromise (IoC).

## Validation
1. Verify Microsoft Defender Antivirus is enabled: Run 'Get-MpComputerStatus | Select-Object AntivirusEnabled' in PowerShell. 2. Confirm cloud protection is enabled: Run 'Get-MpPreference | Select-Object CloudBlockLevel' and ensure it is not 0. 3. Check ASR rule deployment via Intune: In Microsoft Intune, navigate to Endpoint Security > Attack Surface Reduction, select the policy, and confirm the rule 'Use advanced protection against ransomware' (GUID c1db55ab-c21a-4637-bb3f-a12568109d35) is set to 'Block' or 'Audit'. 4. For Configuration Manager: In the Configuration Manager console, go to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard, select the policy, and verify the ASR rule is configured. 5. Validate rule is active on a client: Run 'Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids' and confirm the GUID appears. 6. Test rule behavior: Attempt to run a known ransomware simulator (e.g., from Microsoft) and verify it is blocked.

## Rollback
1. In Intune: Navigate to Endpoint Security > Attack Surface Reduction, select the policy containing the rule, and either remove the rule or set it to 'Not configured' or 'Disabled'. 2. In Configuration Manager: Open the Exploit Guard policy, remove the rule from the ASR rules list, and redeploy the policy. 3. If blocks on benign files occur: Add a per-ASR rule exclusion by running 'Add-MpPreference -AttackSurfaceReductionOnlyExclusions "<path>"' or configure an Allow indicator of compromise (IoC) in Microsoft 365 Defender. 4. Revert cloud protection changes: If cloud protection was enabled solely for this rule, set 'Set-MpPreference -CloudBlockLevel 0' (default). 5. Monitor for any residual blocks: Review Microsoft Defender Antivirus event logs (Event ID 1121) for ASR blocks and adjust exclusions as needed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
