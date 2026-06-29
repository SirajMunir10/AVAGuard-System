# Hardening: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Hardening

## Scenario / Query
How to monitor and audit SharePoint site collection administrator changes for security hardening?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Unauthorized elevation of privileges to site collection admin
- Potential insider threat or compromised account activity

## Error Codes
N/A

## Root Causes
1. Site collection administrator or owner adds a person as site collection administrator (SiteCollectionAdminAdded)
2. Admin gives themselves access to a user's OneDrive account via SharePoint admin center or Microsoft 365 admin center

## Remediation Steps
1. Search audit log for SiteCollectionAdminAdded events
2. Search audit log for SiteCollectionAdminRemoved events
3. Review the app@sharepoint user context for activities performed on behalf of users or admins

## Validation
1. Run the following audit log search command in the Microsoft 365 Purview compliance portal or via Search-UnifiedAuditLog in Exchange Online PowerShell:
   Search-UnifiedAuditLog -Operations "SiteCollectionAdminAdded", "SiteCollectionAdminRemoved" -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date)
   Confirm that the output lists only authorized site collection administrator changes and no unexpected additions.
2. Verify that the app@sharepoint user context is not performing unauthorized activities by searching:
   Search-UnifiedAuditLog -Operations "FileAccessed", "FileModified", "FileDeleted" -UserId "app@sharepoint" -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date)
   Ensure no suspicious file access patterns exist.
3. Check that audit logging is enabled in the Microsoft 365 Defender portal under Audit log settings; confirm the status is 'On'.

## Rollback
1. If an unauthorized SiteCollectionAdminAdded event is found, remove the unauthorized administrator by running:
   Remove-SPOUser -Site <SiteURL> -LoginName <UnauthorizedUserUPN> -Group "Site Collection Administrators"
   (Requires SharePoint Online Management Shell and appropriate permissions.)
2. If the app@sharepoint user context performed unauthorized actions, revoke any delegated permissions granted to the SharePoint admin center or Microsoft 365 admin center by reviewing and removing app permissions in Azure AD under Enterprise applications > SharePoint Online > Permissions.
3. If audit logging was disabled, re-enable it in the Microsoft 365 Defender portal under Audit log settings by toggling 'Audit log' to 'On'.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
