# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate site collection creation in SharePoint or OneDrive?

## Environment Context
- **Tenant Type:** SharePoint/OneDrive
- **Configuration:** Site collection provisioning

## Symptoms
- Unexpected site collections appearing in the organization
- Users provisioning OneDrive sites without authorization

## Error Codes
N/A

## Root Causes
1. A SharePoint or global administrator created a site collection or a user provisioned their OneDrive site

## Remediation Steps
1. Check audit log for SiteCollectionCreated activity
2. Identify who created the site collection
3. Review site collection permissions and settings
4. Delete unauthorized site collections if necessary

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a global administrator or compliance administrator. 2. Navigate to Audit > Search. 3. Under Activities, select 'Created site collection' (SiteCollectionCreated activity). 4. Set the date range to cover the period of unexpected site collections. 5. Click Search. 6. In the results, verify that the SiteCollectionCreated events match only authorized site collections. 7. For each unexpected site collection, click the record to view details, confirming the user who created it and the site URL. 8. Optionally, run the SharePoint Online Management Shell command: `Get-SPOSite -Identity <SiteURL> | Select Owner, Status` to confirm the site is unauthorized.

## Rollback
1. If a site collection was incorrectly deleted or disabled, restore it from the SharePoint admin center Recycle Bin (up to 93 days) by navigating to Active sites, selecting the deleted site, and clicking Restore. 2. If permissions were changed incorrectly, use the SharePoint admin center to reapply the original permission settings or use `Set-SPOSite -Identity <SiteURL> -Owner <OriginalOwner>` in SharePoint Online Management Shell. 3. If a site collection was created by an unauthorized user, follow the remediation steps to delete it: in SharePoint admin center, select the site and click Delete, or run `Remove-SPOSite -Identity <SiteURL> -Confirm:$false`. 4. If the audit log search fails to return results, verify that audit logging is enabled in the Purview portal under Audit > Audit log settings.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
