# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate completed site geo moves in a multi-geo environment?

## Environment Context
- **Tenant Type:** SharePoint/OneDrive Multi-Geo
- **Configuration:** Multi-Geo Capabilities

## Symptoms
- Site content appears in unexpected geographic location
- Users report latency or access issues after geo move

## Error Codes
N/A

## Root Causes
1. A site geo move that a global administrator scheduled completed

## Remediation Steps
1. Review audit log for SiteGeoMoveCompleted activity
2. Confirm the target geo location for the moved site
3. Verify user access and permissions in the new geo location

## Validation
1. Connect to Exchange Online PowerShell and run Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations SiteGeoMoveCompleted -Formatted | Format-Table CreationTime, Operation, ObjectId, SiteUrl, TargetGeoLocation -AutoSize. 2. Verify the TargetGeoLocation field matches the expected geo location for the site. 3. For each moved site, run Get-SPOSite -Identity <SiteUrl> | Select-Object Url, GeoLocation to confirm the current geo location. 4. Check user access by running Get-SPOUser -Site <SiteUrl> | Format-Table DisplayName, LoginName, IsSiteAdmin. 5. Validate that users in the new geo location can access the site without latency by performing a test access from a client in that region.

## Rollback
1. If the site is in an incorrect geo location, contact Microsoft Support to request a manual site geo move back to the original location. 2. As a temporary measure, redirect users to the site via a URL that includes the original geo location (e.g., https://contoso.sharepoint.com/sites/site) until the move is reversed. 3. If permissions are broken, run Set-SPOUser -Site <SiteUrl> -LoginName <User> -IsSiteAdmin $true to restore admin access. 4. For latency issues, instruct users to clear their browser cache and DNS cache (ipconfig /flushdns). 5. If the move caused data inconsistency, restore the site from a backup taken before the move using the SharePoint Admin Center or a third-party backup tool.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
