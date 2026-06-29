# Troubleshooting: Attack Surface Reduction Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction Rules
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot blocks on benign unknown files by the ASR rule 'Use advanced protection against ransomware'?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus, Cloud Protection

## Symptoms
- Blocks on benign, unknown files by the ASR rule 'Use advanced protection against ransomware'.
- Blocks do not resolve in a timely manner.

## Error Codes
N/A

## Root Causes
1. The file does not yet have a positive reputation in the Microsoft cloud.
2. The file is not found to be unharmful, is not a valid signed file, or is not prevalent enough to not be considered ransomware.

## Remediation Steps
1. Wait for the file's reputation and trust values to incrementally increase as non-problematic usage increases.
2. If blocks do not resolve in a timely manner, configure a per-ASR rule exclusion for this rule.
3. Alternatively, use the Allow action for an indicator of compromise (IoC).

## Validation
1. Open the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Navigate to Endpoints > Reports > Attack surface reduction rules.
3. Filter by the rule 'Use advanced protection against ransomware' and review the last 7 days of blocks.
4. Confirm that the previously blocked file(s) now appear with a status of 'Allowed' or are no longer listed in the block events.
5. Alternatively, run the following PowerShell command on an affected device to check the current state of the rule and any exclusions:
   Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids
   Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions
   Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Exclusions
6. Verify that the file can now be executed without being blocked.

## Rollback
1. If an ASR rule exclusion was added, remove it by running the following PowerShell command on the affected device:
   Remove-MpPreference -AttackSurfaceReductionRules_Exclusions -Path "<full-path-to-excluded-file-or-folder>"
2. If an IoC allow indicator was created, remove it from the Microsoft 365 Defender portal:
   - Go to Settings > Endpoints > Indicators > File hashes.
   - Locate the indicator for the file and select 'Remove'.
3. After removal, monitor the device to ensure the original block behavior resumes as expected.
4. If the file is still blocked and the issue persists, re-apply the original exclusion or indicator as a temporary measure while waiting for cloud reputation to update.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
