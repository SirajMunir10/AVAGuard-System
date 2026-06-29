# Governance: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Governance

## Scenario / Query
An organization needs to verify that mailbox auditing is enabled by default for all Exchange Online mailboxes, and to identify any mailboxes where auditing is disabled.

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Default mailbox auditing is enabled in Exchange Online for organizations created after January 2019; for older tenants, mailbox auditing may be disabled by default.

## Symptoms
- Mailbox audit logs are empty or missing expected entries
- Compliance team cannot review mailbox access or actions
- Audit records for mailbox operations are not generated

## Error Codes
N/A

## Root Causes
1. Mailbox auditing is disabled at the organization level or on individual mailboxes
2. Tenant was created before the default mailbox auditing change and was not updated

## Remediation Steps
1. Run Get-OrganizationConfig | Format-List AuditDisabled to check if auditing is disabled at the organization level
2. If AuditDisabled is $true, run Set-OrganizationConfig -AuditDisabled $false to enable auditing organization-wide
3. Run Get-Mailbox -ResultSize Unlimited | Get-MailboxAuditBypassAssociation to identify mailboxes with auditing bypassed
4. For each mailbox returned, run Set-MailboxAuditBypassAssociation -Identity <Mailbox> -AuditBypassEnabled $false to remove the bypass
5. Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -eq $false} to find mailboxes with auditing disabled, then enable with Set-Mailbox -Identity <Mailbox> -AuditEnabled $true

## Validation
Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -eq $false} to confirm no mailboxes have auditing disabled; run Get-OrganizationConfig | Format-List AuditDisabled to confirm organization-level auditing is enabled.

## Rollback
To disable mailbox auditing on a specific mailbox, run Set-Mailbox -Identity <Mailbox> -AuditEnabled $false; to disable organization-wide, run Set-OrganizationConfig -AuditDisabled $true.

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-auditing/manage-mailbox-auditing>
