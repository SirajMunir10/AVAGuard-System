# Optimization: Mailbox Management (554 5.2.2 mailbox full)

**Domain:** Exchange Online
**Subdomain:** Mailbox Management
**Incident Type:** Optimization

## Scenario / Query
A user reports that their mailbox is approaching the storage quota and they cannot send or receive emails. How can an administrator identify mailboxes that are over the issue warning quota and take action to optimize storage?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Default mailbox quotas: IssueWarningQuota = 49 GB, ProhibitSendQuota = 50 GB, ProhibitSendReceiveQuota = 51 GB

## Symptoms
- User receives warning messages about mailbox size approaching quota
- User cannot send new emails
- User cannot receive new emails

## Error Codes
- `554 5.2.2 mailbox full`

## Root Causes
1. Mailbox has exceeded the ProhibitSendReceiveQuota
2. No mail flow rules or retention policies are in place to manage mailbox size

## Remediation Steps
1. Run the Exchange Online PowerShell command: Get-Mailbox -ResultSize unlimited | Get-MailboxStatistics | Where {$_.TotalItemSize -gt (Get-Mailbox $_.MailboxGuid).IssueWarningQuota} | Format-Table DisplayName,TotalItemSize
2. Increase the mailbox quota using: Set-Mailbox <Identity> -IssueWarningQuota <Value> -ProhibitSendQuota <Value> -ProhibitSendReceiveQuota <Value>
3. Enable archiving for the user: Enable-Mailbox <Identity> -Archive
4. Apply a retention policy to automatically move older items to the archive or delete them

## Validation
Run Get-MailboxStatistics for the affected user and verify TotalItemSize is below the new IssueWarningQuota.

## Rollback
To revert quota changes, run Set-Mailbox <Identity> -IssueWarningQuota 49GB -ProhibitSendQuota 50GB -ProhibitSendReceiveQuota 51GB

## References
- <https://learn.microsoft.com/en-us/powershell/module/exchange/get-mailbox>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/set-mailbox>
