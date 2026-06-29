# Hardening: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Hardening

## Scenario / Query
How do I enable mailbox auditing for all user mailboxes in Exchange Online to meet CIS Microsoft 365 Foundation Benchmark control 4.1?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise (E3/E5)
- **Configuration:** Mailbox auditing is enabled by default for new mailboxes since January 2019, but may be disabled for mailboxes created before that date.

## Symptoms
- Mailbox audit logs are not generated for certain user mailboxes
- Security and Compliance Center audit log searches return no mailbox-level events for some users
- CIS benchmark compliance scan reports failure for control 4.1

## Error Codes
N/A

## Root Causes
1. Mailbox auditing was not enabled by default for mailboxes created before January 2019
2. Mailbox auditing was explicitly disabled by an administrator via Set-Mailbox -AuditEnabled $false

## Remediation Steps
1. Connect to Exchange Online PowerShell using the EXO V2 module
2. Run the following command to enable mailbox auditing for all user mailboxes: Get-Mailbox -ResultSize Unlimited -Filter {RecipientTypeDetails -eq 'UserMailbox'} | Set-Mailbox -AuditEnabled $true
3. Optionally, configure audit logging age limit: Set-Mailbox -AuditLogAgeLimit 180 (or as required by policy)
4. Verify the change: Get-Mailbox -ResultSize Unlimited -Filter {RecipientTypeDetails -eq 'UserMailbox'} | Format-Table Name, AuditEnabled

## Validation
Run the command: Get-Mailbox -ResultSize Unlimited -Filter {RecipientTypeDetails -eq 'UserMailbox'} | Where-Object {$_.AuditEnabled -eq $false}. No mailboxes should be returned.

## Rollback
To disable mailbox auditing for all user mailboxes: Get-Mailbox -ResultSize Unlimited -Filter {RecipientTypeDetails -eq 'UserMailbox'} | Set-Mailbox -AuditEnabled $false

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-auditing/enable-mailbox-auditing>
- <https://www.cisecurity.org/benchmark/microsoft_365>
