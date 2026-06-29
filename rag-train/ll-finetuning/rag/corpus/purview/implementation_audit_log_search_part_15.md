# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to filter audit log search results by specific users?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Microsoft Purview

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Users field and select the names of one or more users to display search results for
2. The audit log entries for the selected activity performed by the users you select are displayed in the list of results
3. Leave this box blank to return entries for all users (and service accounts) in your organization

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search.
2. In the 'Users' field, select one or more specific user names.
3. Click 'Search' and confirm that the results list contains only audit log entries for the selected users.
4. Clear the 'Users' field (leave blank) and click 'Search' again; verify that entries for all users and service accounts appear.

## Rollback
1. In the Audit log search page, clear all selections in the 'Users' field.
2. Click 'Search' to return to the default state showing entries for all users and service accounts.
3. If the issue persists, reset the search filters by clicking 'Clear all filters' or refreshing the page.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
