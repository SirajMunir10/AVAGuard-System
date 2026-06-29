# Incident Response: Mailbox Audit Logging

**Domain:** Exchange Online
**Subdomain:** Mailbox Audit Logging
**Incident Type:** Incident Response

## Scenario / Query
A user reports that a mailbox was accessed by an unknown actor. How can an administrator use Exchange Online mailbox audit logging to identify the unauthorized access, and what steps are needed to enable and search the audit log?

## Environment Context
- **Tenant Type:** Enterprise E5
- **Configuration:** Mailbox audit logging is enabled by default for all organizations created after January 2019; for older tenants, it may need to be enabled per mailbox.

## Symptoms
- User reports suspicious emails marked as read or moved to Deleted Items
- Mailbox folder permissions changed without user knowledge
- Unusual sign-in activity from unfamiliar IP addresses

## Error Codes
N/A

## Root Causes
1. Mailbox audit logging not enabled for the specific mailbox
2. Audit log retention period too short to capture the incident
3. Insufficient permissions to search the audit log

## Remediation Steps
1. Enable mailbox audit logging for the affected mailbox using: Set-Mailbox -Identity <MailboxId> -AuditEnabled $true
2. Search the mailbox audit log using: Search-MailboxAuditLog -Identity <MailboxId> -StartDate <date> -EndDate <date> -ShowDetails
3. Review the audit log entries for operations such as 'MoveToDeletedItems', 'UpdateFolderPermissions', 'SendAs', or 'SendOnBehalf'
4. If unauthorized access is confirmed, reset the user's password and revoke any suspicious app permissions
5. Enable unified audit logging in the Microsoft 365 Defender portal to retain logs for longer periods

## Validation
Run Search-MailboxAuditLog again after remediation to confirm no further unauthorized operations appear

## Rollback
Disable mailbox audit logging only if performance impact is unacceptable, using: Set-Mailbox -Identity <MailboxId> -AuditEnabled $false

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-audit-logging/manage-mailbox-audit-logging>
