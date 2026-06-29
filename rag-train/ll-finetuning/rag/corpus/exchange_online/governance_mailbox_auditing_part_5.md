# Governance: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Governance

## Scenario / Query
How do I verify that mailbox auditing is enabled for all user mailboxes in Exchange Online, and what are the documented steps to enable it if it is not?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Default mailbox audit logging settings for user mailboxes

## Symptoms
- Mailbox audit logs are not generated for user actions such as Send, Move, or Delete
- Security and Compliance Center audit log search returns no mailbox-level events
- Compliance reports show missing mailbox audit data

## Error Codes
N/A

## Root Causes
1. Mailbox auditing is not enabled by default for user mailboxes created before January 2019
2. Organization-wide mailbox audit settings may have been disabled via Set-OrganizationConfig -AuditDisabled $true

## Remediation Steps
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline
2. Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -eq $false} | Set-Mailbox -AuditEnabled $true to enable auditing on all user mailboxes where it is currently disabled
3. Optionally, run Set-OrganizationConfig -AuditDisabled $false to enable mailbox auditing organization-wide for all new mailboxes

## Validation
Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -eq $false} to confirm no user mailboxes have auditing disabled

## Rollback
Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -eq $true} | Set-Mailbox -AuditEnabled $false to disable mailbox auditing on all user mailboxes (not recommended for compliance)

## References
- <https://learn.microsoft.com/en-us/purview/audit-mailboxes>
