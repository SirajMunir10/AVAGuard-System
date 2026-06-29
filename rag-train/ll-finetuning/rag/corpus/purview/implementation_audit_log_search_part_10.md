# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to search for audit log activity related to a specific file, folder, or site in Microsoft Purview?

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
1. Enter part or all of a file or folder name to find related activity
2. This returns results for matching files, folders, and sites
3. You can also enter a full URL or part of one, just avoid special characters or spaces
4. You can use * as a wildcard at the end of the URL, for example: https://<tenantname>.sharepoint.com/sites/site123*
5. Leave the field blank to see activity for all files and folders in your organization

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Audit > Audit log search.
3. In the 'File, folder, or site' field, enter a known file or folder name (e.g., 'report.docx' or '/sites/ProjectX').
4. Set an appropriate date range and click 'Search'.
5. Confirm that the results include audit records for activities on that specific file, folder, or site.
6. Repeat the search using a partial URL with a wildcard (e.g., 'https://contoso.sharepoint.com/sites/*') and verify that results are returned for matching sites.
7. Leave the field blank and search; confirm that results include activities for all files and folders in the organization.

## Rollback
1. If the search returns unexpected or no results, verify that the input does not contain special characters or spaces (except the wildcard '*' at the end of a URL).
2. Ensure the date range is correct and that audit logging is enabled for the tenant.
3. If the issue persists, clear the 'File, folder, or site' field and perform a broad search to confirm that audit log search is functioning.
4. If necessary, reset the search parameters to default (blank field, last 7 days) and re-run the search.
5. For further troubleshooting, refer to the official documentation: https://learn.microsoft.com/en-us/purview/audit-log-search

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
