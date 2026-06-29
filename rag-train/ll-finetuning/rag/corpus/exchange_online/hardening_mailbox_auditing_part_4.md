# Hardening: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Hardening

## Scenario / Query
How do I verify and enable mailbox auditing for all user mailboxes in Exchange Online to meet CIS Microsoft 365 Foundations Benchmark control 4.1?

## Environment Context
- **Tenant Type:** Microsoft 365 / Exchange Online
- **Configuration:** Mailbox auditing is not enabled by default for user mailboxes created before January 2019; organization-wide default must be set via Set-OrganizationConfig.

## Symptoms
- Mailbox audit logs are empty or missing expected entries for user mailboxes
- Security team cannot track mailbox access or modifications
- Compliance audit findings indicate mailbox auditing is not enabled

## Error Codes
N/A

## Root Causes
1. Mailbox auditing was not enabled organization-wide via Set-OrganizationConfig -AuditDisabled $false
2. Mailboxes created before January 2019 retain legacy default where auditing is disabled
3. Audit logging was manually disabled on specific mailboxes

## Remediation Steps
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline
2. Run Get-OrganizationConfig | Format-List AuditDisabled to verify current organization-wide setting
3. If AuditDisabled is $true, run Set-OrganizationConfig -AuditDisabled $false to enable mailbox auditing for all mailboxes
4. Run Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditEnabled $true to force enable auditing on existing mailboxes
5. Verify auditing is active by running Get-Mailbox -ResultSize Unlimited | Get-MailboxAuditBypassAssociation

## Validation
Run Get-OrganizationConfig | Format-List AuditDisabled and confirm it returns $false. Then run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -eq $false} to confirm no mailboxes have auditing disabled.

## Rollback
Set-OrganizationConfig -AuditDisabled $true (disables mailbox auditing organization-wide; not recommended for production).

## References
- CIS Microsoft 365 Foundations Benchmark v2.0.0, Control 4.1
- Microsoft Learn: 'Manage mailbox auditing' (https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-auditing/manage-mailbox-auditing)
