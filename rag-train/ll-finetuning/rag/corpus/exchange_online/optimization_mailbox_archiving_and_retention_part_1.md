# Optimization: Mailbox Archiving and Retention

**Domain:** Exchange Online
**Subdomain:** Mailbox Archiving and Retention
**Incident Type:** Optimization

## Scenario / Query
An organization has enabled archive mailboxes for all users but notices that the total archive storage is approaching the default quota limit. They want to optimize storage by enabling auto-expanding archiving. How can they verify and enable this feature for the tenant?

## Environment Context
- **Tenant Type:** Enterprise (E3 or E5)
- **Configuration:** Archive mailboxes enabled for all users; default archive quota of 100 GB is nearly full

## Symptoms
- Archive mailboxes are approaching the 100 GB default quota
- Users receive quota warnings for their archive mailbox
- No automatic expansion of archive storage is occurring

## Error Codes
N/A

## Root Causes
1. Auto-expanding archiving is not enabled at the tenant level
2. The archive mailbox quota is still set to the default 100 GB limit

## Remediation Steps
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline
2. Run the command: Set-OrganizationConfig -AutoExpandingArchiveEnabled $true
3. Wait up to 30 days for the auto-expanding archive to be provisioned for each mailbox (Microsoft automatically manages the expansion)
4. Optionally, verify the setting with: Get-OrganizationConfig | Format-List AutoExpandingArchiveEnabled

## Validation
Run Get-Mailbox -ResultSize Unlimited | Where-Object {$_.ArchiveStatus -eq 'Active' -and $_.AutoExpandingArchiveEnabled -eq $true} to confirm that auto-expanding archiving is enabled for mailboxes.

## Rollback
Disable auto-expanding archiving for the tenant by running: Set-OrganizationConfig -AutoExpandingArchiveEnabled $false. Note: This does not reduce the size of already expanded archives but prevents further automatic expansion.

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-storage/enable-auto-expanding-archiving>
