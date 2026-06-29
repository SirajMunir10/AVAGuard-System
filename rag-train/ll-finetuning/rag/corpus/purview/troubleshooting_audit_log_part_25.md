# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a triggered granular restore session in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- A granular restore session is triggered in Microsoft 365 Backup

## Error Codes
N/A

## Root Causes
1. GranularRestoreSessionTriggered activity occurred

## Remediation Steps
1. Review the audit log for GranularRestoreSessionTriggered activity
2. Verify the granular restore session trigger was authorized

## Validation
Search the unified audit log for GranularRestoreSessionTriggered activity using Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations GranularRestoreSessionTriggered. Confirm that the audit records show the expected session details (e.g., UserId, CreationTime, Item) and that the session was initiated by an authorized user or service principal.

## Rollback
If the granular restore session was unauthorized or caused issues, contact the Microsoft 365 Backup service admin to cancel the restore session via the Microsoft 365 admin center (Backup > Restore sessions > select session > Cancel). Alternatively, use the Microsoft Graph API to delete the restore session: DELETE https://graph.microsoft.com/v1.0/backupRestore/restoreSessions/{sessionId}. After cancellation, re-run the audit log search to confirm no further GranularRestoreSessionTriggered events appear.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
