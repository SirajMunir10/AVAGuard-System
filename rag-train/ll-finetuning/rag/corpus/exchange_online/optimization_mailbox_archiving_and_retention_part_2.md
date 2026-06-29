# Optimization: Mailbox Archiving and Retention

**Domain:** Exchange Online
**Subdomain:** Mailbox Archiving and Retention
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Exchange Online mailbox storage by enabling and configuring the archive mailbox and retention policies to automatically move older emails to the archive?

## Environment Context
- **Tenant Type:** Enterprise (E3/E5 licenses required for archive)
- **Configuration:** Mailboxes with large primary mailbox sizes approaching storage limits; no archive mailbox enabled; no retention policy tags applied

## Symptoms
- Users receive warnings or are unable to send/receive due to mailbox size limits
- Primary mailbox storage quota is consistently near or at the limit
- IT help desk tickets for mailbox size issues increase

## Error Codes
N/A

## Root Causes
1. Archive mailbox not enabled for users
2. No retention policy or retention tags configured to move items to archive automatically
3. Default MRM policy not assigned or not applied

## Remediation Steps
1. 1. Verify that users have an Exchange Online Plan 2 or Exchange Online Archiving add-on license assigned.
2. 2. Enable the archive mailbox using the Exchange admin center (EAC): go to Recipients > Mailboxes, select a user, and under Mailbox > Manage mailbox archive, turn on the archive.
3. 3. Alternatively, use PowerShell: Enable-Mailbox -Identity <user> -Archive.
4. 4. Assign the default MRM policy (e.g., 'Default MRM Policy') to the mailbox using PowerShell: Set-Mailbox -Identity <user> -RetentionPolicy 'Default MRM Policy'.
5. 5. Verify the policy is applied and that retention tags (e.g., 'Default 2 year move to archive') are set to move items to the archive after a specified period.
6. 6. Monitor mailbox usage via the EAC or Get-MailboxStatistics cmdlet.

## Validation
Run Get-Mailbox -Identity <user> | fl ArchiveStatus, ArchiveDatabase, RetentionPolicy to confirm archive is enabled and policy is assigned. Check that the archive mailbox appears in Outlook on the web.

## Rollback
Disable the archive mailbox using PowerShell: Disable-Mailbox -Identity <user> -Archive. Remove the retention policy assignment: Set-Mailbox -Identity <user> -RetentionPolicy $null.

## References
- <https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/enable-archive-mailboxes>
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/messaging-records-management/retention-tags-and-retention-policies>
