# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to search audit log for activities related to a specific file, folder, or site?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Purview compliance portal

## Symptoms
- Need to find activity for a specific file or folder
- Need to search by URL or site name

## Error Codes
N/A

## Root Causes
1. File, folder, or site field can be left blank to see all activity

## Remediation Steps
1. Enter part or all of a file or folder name to find related activity
2. Enter a full URL or part of one, avoiding special characters or spaces
3. Use * as a wildcard at the end of the URL, e.g., https://<tenantname>.sharepoint.com/sites/site123*
4. Leave the field blank to see activity for all files and folders in your organization

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. In the 'File, folder, or site' field, enter a partial or full file/folder name (e.g., 'report.docx' or 'https://contoso.sharepoint.com/sites/site123*'). 3. Set appropriate date range and other filters. 4. Click Search and confirm that results include activities related to the specified file/folder/site. 5. Repeat with the field left blank and verify that results show activities for all files/folders.

## Rollback
1. Clear the 'File, folder, or site' field. 2. Re-run the audit log search to return to viewing all activities. 3. If the search was modified with other filters (e.g., date range, user), reset those to previous values or default. 4. Verify that the search results now show all activities as before.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
