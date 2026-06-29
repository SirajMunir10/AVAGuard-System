# Governance: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Governance

## Scenario / Query
How can an administrator verify that mailbox auditing is enabled by default for all new mailboxes in Exchange Online, and what steps should be taken if auditing is found to be disabled for a subset of mailboxes?

## Environment Context
- **Tenant Type:** Enterprise (E5 or equivalent licensing)
- **Configuration:** OrganizationConfig.DefaultAuditSet

## Symptoms
- Mailbox audit logs are not generated for certain user mailboxes
- Compliance reports show gaps in mailbox access history

## Error Codes
N/A

## Root Causes
1. Mailbox auditing was disabled on a per-mailbox basis using Set-Mailbox -AuditEnabled $false
2. Default audit settings were changed before the default-enablement update in 2019

## Remediation Steps
1. Run Get-OrganizationConfig | Format-List DefaultAuditSet to confirm the default audit set is enabled
2. Run Get-Mailbox -ResultSize unlimited | Where-Object {$_.AuditEnabled -eq $false} | Set-Mailbox -AuditEnabled $true to re-enable auditing on all mailboxes where it is disabled
3. Verify the change with Get-Mailbox -ResultSize unlimited | Where-Object {$_.AuditEnabled -eq $false} to ensure no mailboxes remain with auditing disabled

## Validation
Run Get-Mailbox -ResultSize unlimited | Where-Object {$_.AuditEnabled -eq $false} and confirm the output is empty.

## Rollback
To disable auditing on a specific mailbox, run Set-Mailbox <Identity> -AuditEnabled $false. To revert the organization default, use Set-OrganizationConfig -DefaultAuditSet None (not recommended for compliance).

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-auditing/manage-mailbox-auditing>
