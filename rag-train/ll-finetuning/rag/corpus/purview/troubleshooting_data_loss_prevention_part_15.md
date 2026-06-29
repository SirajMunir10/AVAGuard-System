# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How are DLP policy actions applied when an item matches multiple policies with different authorization group configurations?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies with authorization groups: Auth group A - Block, Auth group A - Block with override, Auth group B - Block

## Symptoms
- Item matches multiple DLP policies with different authorization group actions
- Authorization group behavior not as expected

## Error Codes
N/A

## Root Causes
1. When an item matches multiple policies and those policies differ in authorization group actions, the most restrictive actions are applied per group

## Remediation Steps
1. Review the authorization group actions configured on each matching DLP policy
2. For each authorization group, identify the most restrictive action across all matching policies
3. The aggregate of the most restrictive actions per authorization group will be applied at runtime

## Validation
1. Use the Microsoft Purview compliance portal to identify a test item that matches multiple DLP policies with different authorization group actions (e.g., Auth group A - Block, Auth group A - Block with override, Auth group B - Block).
2. Simulate a DLP policy match for that item by triggering the defined conditions (e.g., sharing sensitive content externally).
3. Verify that for Auth group A, the most restrictive action (Block) is applied and the override option is not available.
4. Verify that for Auth group B, the Block action is applied as configured.
5. Check the DLP activity explorer to confirm the enforced actions per authorization group match the expected most restrictive behavior.

## Rollback
1. If the aggregated actions are not as expected, review each DLP policy's authorization group actions to ensure they are correctly set.
2. Adjust the authorization group actions on the conflicting policies to align with the desired behavior (e.g., change Auth group A from 'Block' to 'Block with override' if override should be allowed).
3. Re-test the item to confirm the new actions are applied correctly.
4. If the issue persists, temporarily disable one of the conflicting DLP policies to isolate the behavior, then re-enable after adjustments.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
