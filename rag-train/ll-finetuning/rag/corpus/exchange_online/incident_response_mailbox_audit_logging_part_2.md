# Incident Response: Mailbox Audit Logging

**Domain:** Exchange Online
**Subdomain:** Mailbox Audit Logging
**Incident Type:** Incident Response

## Scenario / Query
A user reports that a mailbox was accessed by an unknown actor. How do I enable mailbox audit logging retroactively and search the audit log for non-owner mailbox access events?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise (E5)
- **Configuration:** Mailbox audit logging is enabled by default for all organizations created after January 2019, but may be disabled for some mailboxes in older tenants.

## Symptoms
- User reports suspicious activity in their mailbox (e.g., emails marked as read, deleted items restored).
- No audit records found when searching the unified audit log for mailbox operations.
- Mailbox audit logging is not enabled for the affected user's mailbox.

## Error Codes
N/A

## Root Causes
1. Mailbox audit logging is not enabled for the specific mailbox (common in tenants created before default enablement).
2. Audit log search may not include the correct date range or operations.
3. The user performing the search lacks the necessary permissions (e.g., Audit Logs role or View-Only Audit Logs role).

## Remediation Steps
1. Enable mailbox audit logging for the affected mailbox using Exchange Online PowerShell: Set-Mailbox -Identity <UserPrincipalName> -AuditEnabled $true
2. Configure the audit log age limit (default 90 days) to ensure logs are retained: Set-Mailbox -Identity <UserPrincipalName> -AuditLogAgeLimit 365
3. Search the unified audit log for non-owner mailbox access events: Search-UnifiedAuditLog -StartDate <date> -EndDate <date> -Operations MailboxLogin, MailboxPermissionChange, UpdateInboxRules, MoveToDeletedItems, SoftDelete, HardDelete
4. If using the Microsoft 365 Defender portal, navigate to Audit > Search and filter by Workload: Exchange and Activities: MailboxLogin, MailboxPermissionChange.

## Validation
Run Get-Mailbox -Identity <UserPrincipalName> | Format-List AuditEnabled, AuditLogAgeLimit to confirm audit logging is enabled and retention is set. Then re-run the audit log search to verify events appear.

## Rollback
Disable mailbox audit logging for the mailbox: Set-Mailbox -Identity <UserPrincipalName> -AuditEnabled $false. Note: This is not recommended for security monitoring.

## References
- <https://learn.microsoft.com/en-us/powershell/module/exchange/set-mailbox>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/search-unifiedauditlog>
