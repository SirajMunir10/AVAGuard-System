# Optimization: Mailbox Archiving

**Domain:** Exchange Online
**Subdomain:** Mailbox Archiving
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Exchange Online mailbox storage by enabling and configuring the archive mailbox with a custom retention policy, and verify that the archive is functioning correctly?

## Environment Context
- **Tenant Type:** Enterprise E3/E5
- **Configuration:** Mailboxes with auto-expanding archive enabled, default retention policy applied

## Symptoms
- Mailbox size approaching or exceeding the 100 GB primary mailbox quota
- Users unable to send or receive email due to mailbox full errors
- Compliance or eDiscovery searches returning incomplete results because older items are not retained

## Error Codes
N/A

## Root Causes
1. Archive mailbox not enabled for users
2. Default retention policy does not move items to archive automatically
3. Auto-expanding archive not enabled, limiting archive to 100 GB

## Remediation Steps
1. 1. Enable the archive mailbox for each user using the Exchange admin center or PowerShell: Enable-Mailbox -Identity <User> -Archive
2. 2. Create a custom retention policy with a retention tag that moves items to archive after a specified period (e.g., 2 years) using New-RetentionPolicyTag and New-RetentionPolicy
3. 3. Apply the custom retention policy to the userâ€™s mailbox: Set-Mailbox -Identity <User> -RetentionPolicy <PolicyName>
4. 4. Enable auto-expanding archive to allow unlimited archive storage: Set-Mailbox -Identity <User> -AutoExpandingArchive $true
5. 5. Start the Managed Folder Assistant to apply the policy immediately: Start-ManagedFolderAssistant -Identity <User>

## Validation
Run Get-MailboxStatistics -Identity <User> | FL ArchiveSize to confirm archive storage usage. Run Get-MailboxFolderStatistics -Identity <User> -FolderScope RecoverableItems to verify retention policy is moving items. Check the archive mailbox in Outlook on the web or Outlook desktop to see archived items.

## Rollback
Disable the archive mailbox: Disable-Mailbox -Identity <User> -Archive. Remove the custom retention policy: Remove-RetentionPolicy -Identity <PolicyName>. Disable auto-expanding archive: Set-Mailbox -Identity <User> -AutoExpandingArchive $false.

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-archiving/enable-archive-mailboxes>
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/auto-expanding-archiving>
