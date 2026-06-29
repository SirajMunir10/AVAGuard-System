# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How does DLP determine which rule to enforce when content matches multiple rules?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies for Exchange, SharePoint, OneDrive, and Endpoint

## Symptoms
- Content matches multiple DLP rules but only one rule's actions are applied
- Unexpected rule enforcement behavior

## Error Codes
N/A

## Root Causes
1. Rules are evaluated in priority order (creation order) and the first rule with the most restrictive action is enforced
2. For hosted service locations, the rule created first has highest priority
3. For Endpoint DLP, the aggregate or sum of most restrictive actions is applied

## Remediation Steps
1. Review rule priority order: the rule created first has first priority, second has second priority, etc.
2. When content matches multiple rules, identify the rule with the most restrictive action (e.g., Rule 3: notifies users, restricts access, and doesn't allow user overrides)
3. Check that the highest priority rule with the most restrictive action is the one you intend to enforce
4. For Endpoint DLP, verify that the aggregate of most restrictive actions from all matching rules is applied

## Validation
Check DLP reports and audit logs to confirm which rule was applied and that matches for all rules are recorded

## Rollback
Adjust rule priority by recreating rules in desired order or modifying rule conditions

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
