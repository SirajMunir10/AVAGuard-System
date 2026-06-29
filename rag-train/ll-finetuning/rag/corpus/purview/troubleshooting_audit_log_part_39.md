# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate site deletions in SharePoint?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** Site management

## Symptoms
- SharePoint site is missing or inaccessible
- Users report site deletion

## Error Codes
N/A

## Root Causes
1. Site administrator deleted a site

## Remediation Steps
1. Check audit log for SiteDeleted activity
2. Identify who deleted the site
3. Restore the site from the SharePoint recycle bin or backup if available

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) and navigate to Audit > Audit log search. 2. Set the Date range to cover the time of the reported deletion. 3. In the Activities list, select 'Deleted site' under 'SharePoint site activities'. 4. Click Search and confirm that one or more 'SiteDeleted' events appear in the results. 5. For each event, verify the 'User' field shows the account that performed the deletion and the 'Item' field shows the URL of the deleted site. 6. In SharePoint Admin Center (https://admin.microsoft.com/SharePoint), go to Sites > Deleted sites and confirm the deleted site appears in the list with a 'Restore' option. 7. If the site is not in the recycle bin, check the second-stage recycle bin or backup (e.g., via SharePoint Online Management Shell: Get-SPODeletedSite -IncludePersonalSite $false).

## Rollback
1. If the audit log search returns no 'SiteDeleted' events, verify the audit log is enabled (Settings > Audit log in Purview) and that the correct date range and activities are selected. 2. If the site is not found in the SharePoint recycle bin, check the second-stage recycle bin (Site Collection Administrator > Recycle Bin > Second-stage recycle bin) or use SharePoint Online Management Shell: Restore-SPODeletedSite -Identity <SiteURL>. 3. If the site cannot be restored from recycle bin, restore from a backup (e.g., using a third-party backup solution or Microsoft 365 backup if configured). 4. If the deletion was accidental and the site is critical, contact Microsoft Support for advanced recovery options. 5. As a preventive measure, consider enabling retention policies or backup solutions for SharePoint sites.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
