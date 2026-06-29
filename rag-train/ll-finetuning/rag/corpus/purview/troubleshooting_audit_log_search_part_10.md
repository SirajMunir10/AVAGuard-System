# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to search the audit log for activities performed by specific users or all users in the organization?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Purview compliance portal

## Symptoms
- Unable to find specific user activities in audit log
- Need to filter audit log by user or service account

## Error Codes
N/A

## Root Causes
1. User selection box left blank returns entries for all users and service accounts

## Remediation Steps
1. Leave the user selection box blank to return entries for all users (and service accounts) in your organization
2. Select specific users to filter by their activities

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search. 2. Leave the 'User' selection box blank and set a date range covering the period of interest. 3. Click 'Search' and confirm that results include activities from multiple users and service accounts. 4. To verify filtering, select one or more specific users from the 'User' dropdown and repeat the search; confirm that results are limited to activities from those selected users.

## Rollback
1. If the search returns no results or unexpected results, clear all filters and reset the date range to a known active period. 2. Ensure the 'User' selection box is blank to include all users. 3. Verify that audit logging is enabled in the organization (Settings > Audit > Audit log). 4. If issues persist, refer to the official documentation at https://learn.microsoft.com/en-us/purview/audit-log-search for additional troubleshooting steps.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
