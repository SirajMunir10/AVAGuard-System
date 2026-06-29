# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to detect and investigate orphaned hub site deletions?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** Hub sites

## Symptoms
- Hub site no longer has associated sites
- Users unable to associate sites to a hub

## Error Codes
N/A

## Root Causes
1. A SharePoint or global administrator deleted an orphan hub site, which is a hub site that doesn't have any sites associated with it, likely caused by deletion of the original hub site

## Remediation Steps
1. Review audit log for HubSiteOrphanHubDeleted activity
2. Identify the deleted hub site
3. Recreate the hub site if needed and reassociate sites

## Validation
1. Run the following command in the SharePoint Online Management Shell to verify the current hub sites: Get-SPOHubSite | Select-Object -Property SiteId, SiteUrl, Title, AssociatedSiteIds. Confirm that the previously orphaned hub site is either absent (if deletion was intended) or present with associated sites (if recreated).
2. In the Microsoft Purview compliance portal, search the audit log for the date range of the incident using the activity 'HubSiteOrphanHubDeleted'. Verify that the deletion event is recorded and that the deleted hub site's URL matches the one identified.
3. If the hub site was recreated, run Get-SPOHubSite -Identity <new-hub-site-url> and confirm that the AssociatedSiteIds property lists the expected site IDs.
4. As a test, attempt to associate a site to the hub using Set-SPOSite -Identity <test-site-url> -HubSite <hub-site-url>. Verify success with no errors.

## Rollback
1. If the hub site was incorrectly deleted and needs to be restored, first check if the hub site's underlying site collection is still in the SharePoint recycle bin (tenant recycle bin) using Get-SPODeletedSite. If found, restore it with Restore-SPODeletedSite -Identity <site-id>.
2. If the site collection is permanently deleted, create a new site collection using New-SPOSite -Url <original-url> -Owner <admin> -StorageQuota <value> -Template <template>.
3. Register the new site as a hub site using Register-SPOHubSite -Site <new-site-url> -Principals <admin>.
4. Reassociate the previously orphaned sites to the new hub using Set-SPOSite -Identity <orphaned-site-url> -HubSite <new-hub-site-url>.
5. Verify the associations by running Get-SPOHubSite -Identity <new-hub-site-url> and checking the AssociatedSiteIds property.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
