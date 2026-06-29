# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How does DLP handle rule priority when an item matches multiple rules in a policy with identical actions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with multiple rules

## Symptoms
- Item matches multiple rules within the same policy but only one rule's actions are applied

## Error Codes
N/A

## Root Causes
1. When rules have identical actions, the actions from the highest priority rule are applied

## Remediation Steps
1. Review the priority order of rules within the policy (creation order)
2. Ensure the highest priority rule has the desired actions
3. If needed, recreate rules in the desired priority order

## Validation
Check DLP reports to confirm which rule's actions were applied

## Rollback
Adjust rule priority by recreating rules in desired order

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
