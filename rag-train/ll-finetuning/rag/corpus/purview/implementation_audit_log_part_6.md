# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to manage mailbox audit logging retention period for Audit (Standard) logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Default retention period changed from 90 days to 180 days on October 17, 2023

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Audit (Standard) logs generated before October 17, 2023, are retained for 90 days
2. Audit (Standard) logs generated on or after October 17, 2023, follow the new default retention of 180 days

## Validation
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. Run Get-Mailbox -ResultSize Unlimited | Get-MailboxAuditConfig | Format-List Identity,AuditLogRetentionPeriod to confirm the current retention period for each mailbox. 3. For Audit (Standard) logs, verify that logs generated on or after October 17, 2023, show a retention period of 180 days, and logs generated before that date show 90 days. 4. Use Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-180) -EndDate (Get-Date) -RecordType ExchangeAdmin to confirm that logs from the last 180 days are accessible.

## Rollback
1. If the retention period is incorrect, use Set-Mailbox -Identity <MailboxId> -AuditLogRetentionPeriod <DesiredDays> to revert to the previous retention setting (e.g., 90 days). 2. For tenant-wide default, use Set-AdminAuditLogConfig -UnifiedAuditLogRetentionPeriod <DesiredDays> to adjust the default retention period. 3. Verify the change with Get-Mailbox -ResultSize Unlimited | Get-MailboxAuditConfig | Format-List Identity,AuditLogRetentionPeriod. 4. Monitor audit log availability using Search-UnifiedAuditLog with appropriate date ranges to ensure logs are retained as expected.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
