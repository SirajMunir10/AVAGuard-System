# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How does DLP handle policy priority when an item matches multiple policies with identical actions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Multiple DLP policies with overlapping scopes

## Symptoms
- Item matches multiple DLP policies but only one policy's actions are applied

## Error Codes
N/A

## Root Causes
1. When policies have identical actions, the actions from the highest priority policy are applied

## Remediation Steps
1. Identify the priority order of the policies
2. Ensure the highest priority policy has the desired actions
3. If needed, adjust policy priority to change which policy's actions are applied

## Validation
Check DLP reports to confirm which policy's actions were applied

## Rollback
Change policy priority or modify actions to achieve desired enforcement

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
