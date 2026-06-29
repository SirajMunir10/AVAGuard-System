# Governance: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Governance

## Scenario / Query
How do I verify and enforce that mailbox auditing is enabled by default for all new and existing mailboxes in Exchange Online to meet compliance requirements?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Mailbox auditing is enabled by default for all mailboxes created after January 2019. For older mailboxes, auditing must be enabled manually using the Set-Mailbox cmdlet with -AuditEnabled $true.

## Symptoms
- Mailbox audit logs are missing for certain user mailboxes
- Compliance reports show gaps in mailbox access history
- Security team cannot track delegate access or folder operations

## Error Codes
N/A

## Root Causes
1. Mailboxes created before January 2019 do not have auditing enabled by default
2. Audit logging was not explicitly enabled for pre-existing mailboxes

## Remediation Steps
1. Connect to Exchange Online PowerShell
2. Run Get-Mailbox -ResultSize unlimited | Where-Object {$_.AuditEnabled -eq $false} | Set-Mailbox -AuditEnabled $true
3. Verify using Get-Mailbox | Format-Table Name,AuditEnabled
4. For new mailboxes, ensure the default audit settings are not overridden by custom policies

## Validation
Run Get-Mailbox | Format-Table Name,AuditEnabled and confirm all mailboxes show AuditEnabled as True.

## Rollback
To disable mailbox auditing for a specific mailbox, run Set-Mailbox -Identity <MailboxIdentity> -AuditEnabled $false

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-auditing/manage-mailbox-auditing>
