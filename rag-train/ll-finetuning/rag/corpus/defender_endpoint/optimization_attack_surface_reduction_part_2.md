# Optimization: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Optimization

## Scenario / Query
How to monitor ASR rule be9ba2d9-53ea-4cdc-84e5-9b1eeee46550 using advanced hunting?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use advanced hunting action type AsrExecutableEmailContentAudited for audited events
2. Use advanced hunting action type AsrExecutableEmailContentBlocked for blocked events

## Validation
Run the following Kusto query in Microsoft 365 Defender advanced hunting to confirm that ASR rule be9ba2d9-53ea-4cdc-84e5-9b1eeee46550 is generating events:

DeviceEvents
| where ActionType in ("AsrExecutableEmailContentAudited", "AsrExecutableEmailContentBlocked")
| where AdditionalFields contains "be9ba2d9-53ea-4cdc-84e5-9b1eeee46550"
| summarize count() by ActionType, bin(Timestamp, 1h)
| order by Timestamp desc

If results appear with either ActionType, the rule is being monitored correctly.

## Rollback
If the query returns no results or unexpected behavior occurs, verify that the ASR rule is enabled and properly configured. To disable the rule temporarily, run the following PowerShell command as an administrator on the device:

Set-MpPreference -AttackSurfaceReductionRules_Ids "be9ba2d9-53ea-4cdc-84e5-9b1eeee46550" -AttackSurfaceReductionRules_Actions Disabled

Then re-enable it in audit or block mode as needed:

Set-MpPreference -AttackSurfaceReductionRules_Ids "be9ba2d9-53ea-4cdc-84e5-9b1eeee46550" -AttackSurfaceReductionRules_Actions AuditMode

or

Set-MpPreference -AttackSurfaceReductionRules_Ids "be9ba2d9-53ea-4cdc-84e5-9b1eeee46550" -AttackSurfaceReductionRules_Actions Enabled

Finally, rerun the validation query to confirm events appear.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
