# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How are DLP policy override options applied when an item matches multiple policies with different override configurations?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies with override options: No override, Allow override

## Symptoms
- Item matches multiple DLP policies with different override options
- Override behavior not as expected

## Error Codes
N/A

## Root Causes
1. When an item matches multiple policies and those policies differ in the override option, actions are applied in this order: No override > Allow override

## Remediation Steps
1. Check the override options configured on each matching DLP policy
2. If any policy has 'No override', that takes precedence over 'Allow override'
3. The most restrictive override option (No override) will be applied

## Validation
1. Identify the DLP policies that match the item by running: Get-DlpComplianceRule | Where-Object {$_.Mode -eq 'Enable'} | Select-Object Name, Policy, OverrideOption. 2. For each matching policy, confirm the OverrideOption value: if any policy shows 'NoOverride', that policy's restriction will apply. 3. Simulate a DLP policy match using Test-DlpPolicyMatch -ItemUrl '<item_url>' and verify the resulting action includes 'BlockAccess' or 'Block' with no override prompt. 4. Check audit logs: Search-UnifiedAuditLog -Operations 'DLPRuleMatch' -StartDate (Get-Date).AddHours(-1) -EndDate (Get-Date) | Format-Table CreationTime, Operations, AuditData -Wrap and confirm the 'OverrideOption' field in the AuditData shows 'NoOverride' for the applied action.

## Rollback
1. Identify the DLP policy that has 'NoOverride' set and change it to 'AllowOverride' using: Set-DlpComplianceRule -Identity '<RuleName>' -OverrideOption AllowOverride. 2. If the policy with 'NoOverride' is required, remove the conflicting policy from the scope of the item by editing the policy's locations or conditions: Set-DlpCompliancePolicy -Identity '<PolicyName>' -ExchangeLocation @{Remove='<user@domain.com>'}. 3. After changes, re-run validation steps to confirm override behavior is now as expected. 4. If rollback of the entire remediation is needed, restore the original DLP policy configuration from backup or reapply the original settings using Set-DlpComplianceRule with the original OverrideOption value.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
