# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit changes to site permission levels and access request settings?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Permission levels modified or removed on site collections
- Access request settings changed unexpectedly

## Error Codes
N/A

## Root Causes
1. PermissionLevelModified: a permission level was changed on a site collection
2. PermissionLevelRemoved: a permission level was removed from a site collection
3. WebRequestAccessModified: access request settings were modified on a site

## Remediation Steps
1. Search audit log for PermissionLevelModified events
2. Search audit log for PermissionLevelRemoved events
3. Search audit log for WebRequestAccessModified events

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. Set 'Activities' filter to 'PermissionLevelModified', 'PermissionLevelRemoved', and 'WebRequestAccessModified'. 3. Set date range to cover the incident period. 4. Click 'Search'. 5. Confirm that the search returns audit records for each selected activity. 6. For each returned record, verify the 'Item' field shows the affected site collection URL and the 'User' field shows the account that performed the change.

## Rollback
1. For each PermissionLevelModified event: Use SharePoint Online Management Shell to run 'Set-SPOSite -Identity <SiteURL> -DenyAddAndCustomizePages <original value>' if the change affected page customization permissions. 2. For each PermissionLevelRemoved event: Use SharePoint Online Management Shell to run 'Add-SPOSitePermissionLevel -Identity <SiteURL> -PermissionLevel <removed level>' to restore the removed permission level. 3. For each WebRequestAccessModified event: Use SharePoint Online Management Shell to run 'Set-SPOSite -Identity <SiteURL> -DisableSharingForNonOwners <original value>' or adjust access request settings via SharePoint admin center > Site settings > Access requests.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
