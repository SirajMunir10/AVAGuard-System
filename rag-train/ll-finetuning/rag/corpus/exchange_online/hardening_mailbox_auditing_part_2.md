# Hardening: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Hardening

## Scenario / Query
How do I enable mailbox auditing for all user mailboxes in Exchange Online to meet CIS Microsoft 365 Foundation Benchmark control 4.1?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Mailbox auditing is not enabled by default for all users; it must be explicitly enabled via PowerShell.

## Symptoms
- Mailbox audit logs are empty or missing for user mailboxes
- Security and Compliance audit searches return no mailbox-level events
- CIS compliance scan reports failure for control 4.1

## Error Codes
N/A

## Root Causes
1. Mailbox auditing is not enabled by default for all mailboxes in Exchange Online
2. Only mailboxes created after January 2019 have auditing enabled by default; older mailboxes require manual enablement

## Remediation Steps
1. Connect to Exchange Online PowerShell
2. Run the command: Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditEnabled $true
3. Verify with: Get-Mailbox -ResultSize Unlimited | Select-Object DisplayName, AuditEnabled

## Validation
Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.AuditEnabled -ne $true} and confirm the result set is empty.

## Rollback
Run Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditEnabled $false to disable mailbox auditing for all users.

## References
- CIS Microsoft 365 Foundation Benchmark v1.5.0, Control 4.1
