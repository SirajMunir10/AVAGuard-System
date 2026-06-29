# Troubleshooting: Microsoft Defender Antivirus (1121)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 1121 when an attack surface reduction rule fires in block mode?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1121 is logged when an attack surface reduction rule fires in block mode

## Error Codes
- `1121`

## Root Causes
1. Attack surface reduction rule triggered in block mode

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 2. Look for Event ID 1121 entries. 3. Confirm that the event details include the rule name, rule ID, and the blocked process. 4. Verify that the action listed is 'Blocked' and not 'Audited'. 5. Optionally, run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids to list all configured ASR rules and their states.

## Rollback
1. If the ASR rule causing the block should be disabled, open PowerShell as Administrator. 2. Run Set-MpPreference -AttackSurfaceReductionRules_Ids <RuleID> -AttackSurfaceReductionRules_Actions Disabled. 3. Alternatively, to set the rule to audit mode, run Set-MpPreference -AttackSurfaceReductionRules_Ids <RuleID> -AttackSurfaceReductionRules_Actions AuditMode. 4. Verify the change by running Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. 5. If needed, re-enable the rule in block mode with Set-MpPreference -AttackSurfaceReductionRules_Ids <RuleID> -AttackSurfaceReductionRules_Actions Enabled.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
