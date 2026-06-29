# Incident Response: Mailbox Audit Logging

**Domain:** Exchange Online
**Subdomain:** Mailbox Audit Logging
**Incident Type:** Incident Response

## Scenario / Query
A user reports that a mailbox was accessed by an unknown actor. How can an administrator enable mailbox auditing for all mailboxes and search the audit log to identify the unauthorized access?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise (E5 or E3 with add-on)
- **Configuration:** Mailbox audit logging is not enabled by default for all mailboxes; organization-wide audit must be turned on via Exchange Online PowerShell.

## Symptoms
- User reports suspicious activity such as deleted or forwarded emails
- No mailbox audit records appear in the unified audit log
- Mailbox audit logging is disabled on the affected mailbox

## Error Codes
N/A

## Root Causes
1. Mailbox audit logging is not enabled by default for all mailboxes in the organization
2. The mailbox was not individually enabled for audit logging

## Remediation Steps
1. Connect to Exchange Online PowerShell using an account with the Organization Management role
2. Run the command: Set-OrganizationConfig -AuditDisabled $false to enable mailbox audit logging for all mailboxes
3. Wait up to 60 minutes for the change to propagate, then verify with: Get-OrganizationConfig | Format-List AuditDisabled
4. Search the unified audit log in the Microsoft 365 Defender portal or via Search-UnifiedAuditLog for Operations such as 'MailboxLogin' or 'UpdateInboxRules'
5. If needed, enable audit logging for a specific mailbox with: Set-Mailbox -Identity <user> -AuditEnabled $true

## Validation
Run Get-Mailbox -ResultSize Unlimited | Get-MailboxAuditLogEntry to confirm audit events are being generated for the mailbox.

## Rollback
To disable mailbox audit logging organization-wide, run: Set-OrganizationConfig -AuditDisabled $true. To disable for a single mailbox, run: Set-Mailbox -Identity <user> -AuditEnabled $false.

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-audit-logging/manage-mailbox-audit-logging>
