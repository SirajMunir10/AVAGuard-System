# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify when a SharePoint group is created or deleted in the audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Unexpected SharePoint groups appearing or disappearing
- Changes in site access due to group membership changes

## Error Codes
N/A

## Root Causes
1. Group created: site administrator or owner creates a group, or a task results in group creation (e.g., first time sharing a file creates a system group)
2. Group deleted: user deletes a group from a site (GroupRemoved)

## Remediation Steps
1. Search audit log for GroupRemoved events
2. Search audit log for group creation events (not explicitly named but implied by context)

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with appropriate permissions. 2. Navigate to Audit > Search. 3. Set the Date range to cover the period of unexpected group changes. 4. In the Activities list, select 'GroupRemoved' under 'SharePoint site administration' to search for group deletion events. 5. For group creation, select 'Added group to site' (or equivalent activity under 'SharePoint site administration') as per the documentation. 6. Run the search and verify that the expected events appear for the affected sites. 7. Optionally, use PowerShell: `Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations 'GroupRemoved', 'Added group to site' -ResultSize 1000` and confirm the output includes the relevant entries.

## Rollback
1. If a group was incorrectly deleted, recreate it via SharePoint site settings: Go to Site Settings > People and groups > Create group, or use PowerShell: `New-SPOSiteGroup -Site <SiteURL> -Group 'GroupName' -PermissionLevel 'Contribute'`. 2. If a group was incorrectly created, remove it via SharePoint site settings: Site Settings > People and groups > select the group > Actions > Delete, or use PowerShell: `Remove-SPOSiteGroup -Site <SiteURL> -Group 'GroupName'`. 3. Verify group membership and permissions are restored to the desired state using SharePoint UI or `Get-SPOSiteGroup -Site <SiteURL>`. 4. If the issue persists, review the audit log again to identify any other unexpected events and repeat remediation as needed.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
