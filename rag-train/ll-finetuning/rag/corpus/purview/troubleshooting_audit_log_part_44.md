# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot unexpected sharing behavior by auditing sharing inheritance changes?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Items no longer inherit sharing permissions from parent
- Unexpected sharing links or access

## Error Codes
N/A

## Root Causes
1. SharingInheritanceBroken event: an item was changed so it no longer inherits sharing permissions from its parent

## Remediation Steps
1. Search audit log for SharingInheritanceBroken events
2. Review the item and user who performed the action

## Validation
1. Connect to Exchange Online PowerShell: Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
2. Search the audit log for SharingInheritanceBroken events within the relevant time range: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations SharingInheritanceBroken -ResultSize 1000 | Format-Table CreationTime, UserIds, Operations, Item, ObjectId
3. Confirm that the specific item identified in the remediation no longer appears in the search results after re-inheriting permissions (if re-inheritance was performed).
4. Verify the item's current sharing permissions using: Get-MailboxFolderStatistics -Identity <user> -FolderScope All | Where-Object {$_.FolderPath -like '*<item>*'} | Get-MailboxFolderPermission

## Rollback
1. If the remediation involved breaking inheritance to fix an issue, restore inheritance for the affected item: Set-MailboxFolder -Identity <item> -InheritPermissionEnabled $true
2. If the remediation involved removing a sharing link, re-create the sharing link using: New-SharingLink -Identity <item> -Type <Edit|View> -ExpirationTime (Get-Date).AddDays(30)
3. If the remediation involved changing permissions, re-apply the original permissions using: Add-MailboxFolderPermission -Identity <item> -User <user> -AccessRights <rights>
4. Re-run the validation steps to confirm the rollback restored the previous state.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
