# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate when a restore item restoration is triggered in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Restore is triggered for an item backed up with Microsoft 365 Backup

## Error Codes
N/A

## Root Causes
1. BackupItemRestoreTriggered activity occurred

## Remediation Steps
1. Review the audit log for BackupItemRestoreTriggered activity
2. Verify the restore trigger was authorized

## Validation
Search the unified audit log for BackupItemRestoreTriggered events in the last 24 hours using: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -Operations BackupItemRestoreTriggered | Format-Table CreationTime, UserIds, Operations, AuditData. Confirm the event appears with expected user and timestamp. Then verify the AuditData JSON contains valid parameters such as BackupItemId, BackupPolicyId, and RestorePointId.

## Rollback
If the restore was unauthorized or caused issues, contact the user who triggered the restore to confirm intent. If the restore must be reversed, use the Microsoft 365 Backup admin center to initiate a reverse restore (if supported) or restore the original item from a backup taken before the unintended restore. For audit-only issues, no rollback is needed; instead, update access policies to restrict BackupItemRestoreTriggered permissions to authorized administrators only.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
