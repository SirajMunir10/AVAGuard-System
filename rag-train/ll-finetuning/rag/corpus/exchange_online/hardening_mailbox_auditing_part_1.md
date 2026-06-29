# Hardening: Mailbox Auditing

**Domain:** Exchange Online
**Subdomain:** Mailbox Auditing
**Incident Type:** Hardening

## Scenario / Query
How do I enable mailbox auditing for all users in Exchange Online to meet CIS Microsoft 365 Foundations Benchmark control 4.1?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Mailbox auditing is not enabled by default for all users; it must be explicitly enabled via PowerShell.

## Symptoms
- Mailbox audit logs are empty or missing expected entries
- Security team cannot track mailbox access or actions
- Compliance audit reports show mailbox auditing is disabled

## Error Codes
N/A

## Root Causes
1. Mailbox auditing is not enabled for all users in the organization
2. Default audit settings only apply to users created after January 2019

## Remediation Steps
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline
2. Run: Set-OrganizationConfig -AuditDisabled $false
3. Run: Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditEnabled $true -AuditLogAgeLimit 180 -AuditAdmin Update, Move, Copy, SoftDelete, HardDelete, FolderBind, SendAs, SendOnBehalf -AuditDelegate Update, Move, Copy, SoftDelete, HardDelete, FolderBind, SendAs, SendOnBehalf -AuditOwner Update, Move, Copy, SoftDelete, HardDelete, FolderBind
4. Verify with: Get-Mailbox | Select DisplayName, AuditEnabled

## Validation
Run Get-OrganizationConfig | Select AuditDisabled to confirm it is False; run Get-Mailbox | Where {$_.AuditEnabled -ne $true} to confirm no mailboxes remain with auditing disabled.

## Rollback
Set-OrganizationConfig -AuditDisabled $true and Get-Mailbox -ResultSize Unlimited | Set-Mailbox -AuditEnabled $false

## References
- <https://www.cisecurity.org/benchmark/microsoft_365>
