# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to filter audit log search results by specific users in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview Audit Log Search

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Users field
2. Select the names of one or more users to display search results for
3. The audit log entries for the selected activity performed by the selected users are displayed in the list of results
4. Leave this box blank to return entries for all users (and service accounts) in your organization

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search. 2. In the 'Users' field, enter the specific user principal names (e.g., user@contoso.com) separated by semicolons. 3. Click 'Search'. 4. Confirm that the results list contains only audit log entries where the user matches the specified names. 5. Optionally, run a second search with the 'Users' field left blank and verify that the results now include entries from all users and service accounts.

## Rollback
1. Clear the 'Users' field in the Audit log search page. 2. Click 'Search' to return results for all users and service accounts. 3. Verify that the results list now includes entries from all users and service accounts, effectively reverting to the default unfiltered state.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
