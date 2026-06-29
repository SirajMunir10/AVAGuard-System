# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate completion of a restore item restoration in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Restoration of an item backed up by Microsoft 365 Backup is completed

## Error Codes
N/A

## Root Causes
1. BackupItemRestoreCompleted activity occurred

## Remediation Steps
1. Review the audit log for BackupItemRestoreCompleted activity
2. Verify the restore operation was authorized

## Validation
Search the unified audit log for BackupItemRestoreCompleted activity. Run: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations BackupItemRestoreCompleted | Format-Table CreationTime, UserIds, Operations, AuditData. Confirm at least one record exists with a valid CreationTime and UserIds. Then inspect the AuditData property for each record to verify the restore operation was authorized (e.g., check that the user who performed the restore has appropriate permissions).

## Rollback
If the restore operation is found to be unauthorized or erroneous, contact the user who performed the restore to confirm intent. If the restore must be reversed, use the Microsoft 365 Backup restore interface to perform a reverse restore (if supported) or manually restore the original item from a backup taken before the unauthorized restore. If no reverse restore is available, restore the original item from a backup taken prior to the unauthorized restore using the standard Microsoft 365 Backup restore process. Document the incident and notify the security team.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
