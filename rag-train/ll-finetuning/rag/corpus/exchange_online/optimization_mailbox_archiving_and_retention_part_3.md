# Optimization: Mailbox Archiving and Retention

**Domain:** Exchange Online
**Subdomain:** Mailbox Archiving and Retention
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Exchange Online mailbox storage by enabling and configuring archive mailboxes and retention policies to reduce the load on primary mailboxes?

## Environment Context
- **Tenant Type:** Enterprise E3/E5
- **Configuration:** Mailbox archiving is not enabled for all users; default retention policies are not applied.

## Symptoms
- Primary mailboxes approaching or exceeding storage quotas
- Users reporting inability to send or receive email due to mailbox size limits
- High storage consumption in Exchange Online leading to increased costs

## Error Codes
N/A

## Root Causes
1. Archive mailboxes are not enabled for users
2. Retention policies are not configured to move older items to the archive automatically

## Remediation Steps
1. Enable archive mailboxes for all users via the Exchange admin center or PowerShell: Enable-Mailbox -Identity <user> -Archive
2. Create or modify a retention policy to move items older than a specified period (e.g., 2 years) to the archive using the New-RetentionPolicy cmdlet
3. Apply the retention policy to mailboxes using Set-Mailbox -Identity <user> -RetentionPolicy <policy name>
4. Verify archive mailbox provisioning and retention policy application

## Validation
Run Get-Mailbox -Archive to confirm archive mailboxes are enabled; use Get-MailboxStatistics -Archive to check archive storage usage.

## Rollback
Disable archive mailboxes using Disable-Mailbox -Identity <user> -Archive; remove or reassign retention policies using Set-Mailbox -Identity <user> -RetentionPolicy $null

## References
- <https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/enable-archive-mailboxes>
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/messaging-records-management/retention-tags-and-policies>
