# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a triggered granular restore for a backup item in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- A granular restore is triggered for a backup item in a granular restore session

## Error Codes
N/A

## Root Causes
1. BackupItemGranularRestoreTriggered activity occurred

## Remediation Steps
1. Review the audit log for BackupItemGranularRestoreTriggered activity
2. Verify the granular restore trigger was authorized

## Validation
Search the unified audit log for BackupItemGranularRestoreTriggered activity using the Search-UnifiedAuditLog cmdlet in Exchange Online PowerShell. Run: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations BackupItemGranularRestoreTriggered | Format-Table CreationTime, UserIds, Operations, AuditData. Confirm that the audit records show the expected granular restore trigger, including the user who initiated it and the target backup item. Verify that the AuditData field contains details such as the restore session ID, backup item ID, and timestamp. If the activity is present and matches the expected restore session, the remediation is successful.

## Rollback
If the granular restore trigger is found to be unauthorized or erroneous, revoke the permissions of the user who initiated the restore by removing their role assignments in the Microsoft 365 Defender portal under Roles & scopes. For the specific restore session, cancel the in-progress granular restore by using the Stop-M365BackupRestore cmdlet in Exchange Online PowerShell: Stop-M365BackupRestore -SessionId <SessionId> -Confirm:$false. Then, re-run the audit log search to confirm no further BackupItemGranularRestoreTriggered activities appear for that session. If the restore was already completed, restore the backup item from a pre-restore snapshot using the Start-M365BackupRestore cmdlet with the original backup version.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
