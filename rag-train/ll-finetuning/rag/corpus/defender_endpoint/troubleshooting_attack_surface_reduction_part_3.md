# Troubleshooting: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot an ASR rule that is not working as expected?

## Environment Context
- **Tenant Type:** Windows E5 subscription
- **Configuration:** ASR rules configured

## Symptoms
- ASR rule does not work as expected
- False positives or false negatives

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For false positives, add the file or path as an exclusion to the ASR rule. For more information, see File and folder exclusions for ASR rules.
2. Use the Microsoft Security Intelligence web-based submission form to report a false negative or false positive for ASR rules.
3. With a Windows E5 subscription, you can also provide a link to any associated alert.
4. Collect and submit diagnostic data to help troubleshoot the issue.

## Validation
1. Verify that the ASR rule is enabled and in the correct mode (block/audit/warn) by running: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. 2. Confirm the exclusion was applied correctly: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions. 3. Test the rule by triggering the behavior that was previously blocked/allowed and check the event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for event ID 1121 (blocked) or 5007 (settings change). 4. If using the submission form, verify the submission was received via the Microsoft Security Intelligence portal. 5. For Windows E5 subscriptions, confirm that alert links are accessible and show the expected status.

## Rollback
1. Remove the exclusion added for false positives: Set-MpPreference -AttackSurfaceReductionRules_Exclusions @{Remove='<path or file>'} (replace with actual path). 2. If the ASR rule was disabled during troubleshooting, re-enable it: Add-MpPreference -AttackSurfaceReductionRules_Ids <RuleId> -AttackSurfaceReductionRules_Actions Enabled. 3. If diagnostic data was submitted, no rollback is needed; however, you can revert any temporary configuration changes made to collect data. 4. If alert links were shared, no rollback is required. 5. Restore the original ASR rule configuration from backup if a full rollback is necessary.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-asr>
