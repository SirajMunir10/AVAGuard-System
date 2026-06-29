# Governance: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Governance

## Scenario / Query
A security auditor reports that mailbox audit logging is not enabled by default for all user mailboxes in the tenant. How can an administrator verify and enable mailbox audit logging for all mailboxes to meet compliance requirements?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Mailbox audit logging is enabled by default for all organizations created after January 2019, but may be disabled for older tenants or specific mailboxes. The default audit actions include MailboxLogin, Move, SoftDelete, HardDelete, Update, and others.

## Symptoms
- Mailbox audit logs are missing for certain user mailboxes
- Compliance audit reports show gaps in mailbox activity tracking
- Security team cannot review mailbox access or deletion events for all users

## Error Codes
N/A

## Root Causes
1. Mailbox audit logging was not enabled by default for the tenant (created before January 2019)
2. Mailbox audit logging was disabled for specific mailboxes via PowerShell or Exchange admin center
3. Audit log retention period is set to less than the required compliance duration

## Remediation Steps
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline
2. Run Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditEnabled $true to enable audit logging for all mailboxes
3. Run Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditLogAgeLimit 90 to set a retention period of 90 days (or as required by policy)
4. Verify the configuration with Get-Mailbox -ResultSize Unlimited | Select-Object Name, AuditEnabled, AuditLogAgeLimit
5. For new mailboxes, ensure the default audit settings are applied by checking the organization config: Get-OrganizationConfig | Select-Object AuditDisabled

## Validation
Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -eq $false} to confirm no mailboxes have audit logging disabled. Also check the audit log for recent events using Search-MailboxAuditLog.

## Rollback
To disable mailbox audit logging for all mailboxes, run Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditEnabled $false. To revert retention, set AuditLogAgeLimit to the previous value.

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-audit-logging/manage-mailbox-auditing>
