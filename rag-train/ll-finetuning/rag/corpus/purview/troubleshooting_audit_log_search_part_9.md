# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when no results are returned from an audit log search due to incorrect operation names?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Microsoft Purview

## Symptoms
- No results are returned from an audit log search

## Error Codes
N/A

## Root Causes
1. Operation names are entered incorrectly

## Remediation Steps
1. Review the audit activities article to find the exact operation name for the activities you want to search for
2. Copy and paste the operation names directly from the article to the operation search field to ensure they're entered correctly and without typos

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Audit > Audit log search.
3. In the 'Activities' filter, select the exact operation names from the official list (e.g., 'UserLoggedIn' or 'FileAccessed') as documented at https://learn.microsoft.com/en-us/purview/audit-log-search.
4. Set a date range that covers known activity (e.g., last 24 hours).
5. Click 'Search' and confirm that results appear for the corrected operation names.
6. Optionally, run a broader search with no operation filter to verify that audit logs are being generated in the tenant.

## Rollback
1. If the corrected operation names still yield no results, revert to the original (incorrect) operation names to confirm the issue is not with the search parameters.
2. Clear the 'Activities' filter entirely and run a search with only a date range to verify that audit logs exist in the tenant.
3. If no logs appear at all, check that audit logging is enabled in the tenant (Settings > Audit > Turn on auditing).
4. If audit logging is off, enable it and wait up to 24 hours for logs to populate.
5. If the issue persists, contact Microsoft Support with the search parameters and tenant ID.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
