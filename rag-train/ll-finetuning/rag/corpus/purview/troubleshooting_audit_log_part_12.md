# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify when a form owner deletes all responses in Microsoft Forms?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- All form responses missing
- Response data lost

## Error Codes
N/A

## Root Causes
1. Form owner deleted all response data

## Remediation Steps
1. Search audit log for 'Deleted all responses' activity
2. Check if response data can be recovered from backup

## Validation
1. Sign in to the Microsoft 365 Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Audit > Audit log search.
3. Set the Date range to cover the time of the incident.
4. In the Activities list, select 'Deleted all responses' under Forms activities.
5. Click Search and confirm that one or more audit log entries appear with the activity 'Deleted all responses'.
6. For each matching entry, verify the User field shows the form owner's account and the Item field shows the form name.
7. If the form owner has a backup (e.g., from Microsoft Forms export or a third-party backup), confirm the backup file exists and can be restored.

## Rollback
1. If the audit log search returns no results, verify that audit logging is enabled in the Purview portal (Audit > Audit log search > Settings).
2. If audit logging is disabled, enable it by running: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true (requires Exchange Online PowerShell).
3. If the 'Deleted all responses' activity is found but no backup exists, contact Microsoft Support to inquire about data recovery options (note: Microsoft does not guarantee recovery of deleted form responses).
4. If the form owner accidentally deleted responses, advise them to check the Recycle Bin in Microsoft Forms (if available) or restore from a previously exported Excel workbook.
5. As a last resort, recreate the form and manually re-enter responses from any printed or saved copies.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
