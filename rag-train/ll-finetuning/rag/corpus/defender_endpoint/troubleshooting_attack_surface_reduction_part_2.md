# Troubleshooting: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ASR rules that are not blocking expected files or processes (false negatives) by switching to Audit mode?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- ASR rule is not blocking files or processes that it should block (false negative)

## Error Codes
N/A

## Root Causes
1. ASR rule was already in Audit mode
2. You were testing another feature and forgot to set the ASR rule back into Block or Warn mode
3. An automated PowerShell script changed the rule mode

## Remediation Steps
1. Use the same method used to distribute ASR rules to devices to set the problematic rules to Audit mode
2. Do the action on the device that causes the issue (e.g., open the file or run the process that isn't blocked but should be blocked)
3. Review the ASR rule activity by filtering Event ID values in Windows Event viewer in the Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational log: Block events: 1121, Audit events: 1122, User override events in Warn mode: 1129, Configuration changes: 5007

## Validation
1. Confirm the ASR rule is currently set to Audit mode using the same method originally used to deploy the rule (e.g., Intune, Group Policy, PowerShell). For example, run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids to list rule IDs and their modes. 2. Reproduce the triggering action (e.g., open the file or run the process that should have been blocked). 3. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 4. Filter by Event ID 1122 (Audit events) to verify that an audit event was generated for the expected rule and file/process. 5. Confirm that no Event ID 1121 (Block events) appears for the same action, indicating the rule is correctly in Audit mode and not blocking.

## Rollback
1. Use the same deployment method (e.g., Intune, Group Policy, PowerShell) to set the ASR rule back to Block or Warn mode as originally intended. For example, in PowerShell: Set-MpPreference -AttackSurfaceReductionRules_Ids <RuleID> -AttackSurfaceReductionRules_Actions Enabled. 2. Verify the change by running Get-MpPreference and checking that the rule mode is now Block or Warn. 3. Reproduce the triggering action again to confirm the rule now blocks (Event ID 1121) or warns (Event ID 1129) as expected. 4. Check Event ID 5007 in the same Operational log to confirm the configuration change was logged.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-asr>
