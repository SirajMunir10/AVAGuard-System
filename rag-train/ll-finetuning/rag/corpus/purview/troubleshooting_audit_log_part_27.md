# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for WebContentFiltering activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** WebContentFiltering feature in Microsoft Edge

## Symptoms
- Need to audit browsing activities related to WebContentFiltering

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Activities filter to search for specific activities.
2. To list all WebContentFiltering activities, select WebContentFiltering in the Record type filter.
3. Use the date range boxes and the Users list to scope the search results further if needed.

## Validation
1. Navigate to Microsoft 365 Purview compliance portal > Audit > Search. 2. Set the 'Record type' filter to 'WebContentFiltering'. 3. Confirm that the search results return entries with 'WebContentFiltering' as the record type. 4. Optionally, verify that filtering by a specific user or date range returns expected results.

## Rollback
1. Clear the 'Record type' filter by selecting 'Clear all filters' or resetting it to 'All'. 2. Remove any custom date range or user filters to restore the default search scope. 3. If the search was saved, delete the saved search query. 4. Confirm that the audit log search returns to its default state showing all record types.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
