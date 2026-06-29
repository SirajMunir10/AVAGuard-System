# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How are DLP policy actions applied when an item matches multiple policies with different actions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies with actions: Block print, Block copy to USB, Block copy to clipboard

## Symptoms
- Item matches multiple DLP policies with differing actions
- Expected action not applied due to policy aggregation

## Error Codes
N/A

## Root Causes
1. When an item matches multiple policies and those policies differ in actions, the aggregate or sum of the most restrictive actions are applied

## Remediation Steps
1. Review the DLP policy actions for each matching policy
2. Identify the most restrictive actions across all matching policies
3. The aggregate of the most restrictive actions will be applied at runtime

## Validation
1. Use the DLP Alerts page in Microsoft Purview compliance portal to identify a test item that matches multiple DLP policies with differing actions (e.g., Policy A blocks print, Policy B blocks copy to USB). 2. Confirm that the item's DLP rule match details show both policies triggered. 3. Verify that the actual enforced actions include the most restrictive combination (e.g., both print and copy to USB are blocked). 4. Run the following PowerShell command to check policy match details: Get-DlpComplianceRule -Identity "<RuleName>" | Select-Object Name, Actions. 5. Review the DLP policy reference documentation at https://learn.microsoft.com/en-us/purview/dlp-policy-reference to confirm that the aggregate of most restrictive actions is applied.

## Rollback
1. If the aggregated actions are too restrictive, modify the conflicting DLP policies to align actions (e.g., change both policies to block the same actions). 2. Use the Microsoft Purview compliance portal to edit each policy: navigate to Data Loss Prevention > Policies, select the policy, and adjust the actions under 'Actions' settings. 3. Alternatively, create a new unified policy that combines the desired actions and disable the conflicting policies. 4. After changes, re-test the item to confirm the expected actions are applied. 5. Monitor DLP alerts to ensure no unintended blocking occurs.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
