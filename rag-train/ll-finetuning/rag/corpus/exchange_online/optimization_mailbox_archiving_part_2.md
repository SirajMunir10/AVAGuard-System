# Optimization: Mailbox Archiving

**Domain:** Exchange Online
**Subdomain:** Mailbox Archiving
**Incident Type:** Optimization

## Scenario / Query
A user reports that their mailbox is approaching the storage limit, but the archive mailbox is not enabled. How can I enable the archive mailbox and configure the archive policy to automatically move older items to the archive?

## Environment Context
- **Tenant Type:** Enterprise (E3 or E5 license required for archiving)
- **Configuration:** Mailbox has been licensed with Exchange Online Plan 2 or Exchange Online Archiving add-on; archive auto-expanding is available for mailboxes exceeding 100 GB.

## Symptoms
- User receives warnings about mailbox size nearing the quota (default 50 GB for Exchange Online Plan 1, 100 GB for Plan 2).
- Archive mailbox is not visible in Outlook or Outlook on the web.
- No archive policy (default retention tag) is assigned to the mailbox.

## Error Codes
N/A

## Root Causes
1. Archive mailbox is not enabled on the user's mailbox.
2. Default archive policy (Default MRM Policy) is not applied, so items are not automatically moved to the archive.

## Remediation Steps
1. 1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline.
2. 2. Enable the archive mailbox: Enable-Mailbox -Identity <UserPrincipalName> -Archive.
3. 3. Verify the archive is enabled: Get-Mailbox -Identity <UserPrincipalName> | Format-List ArchiveStatus, ArchiveDatabase.
4. 4. Apply the default MRM policy to automatically move items older than two years to the archive: Set-Mailbox -Identity <UserPrincipalName> -RetentionPolicy "Default MRM Policy".
5. 5. Wait for the Managed Folder Assistant to process the mailbox, or start it manually: Start-ManagedFolderAssistant -Identity <UserPrincipalName>.
6. 6. Confirm the archive policy is applied: Get-Mailbox -Identity <UserPrincipalName> | Format-List RetentionPolicy.

## Validation
Run Get-Mailbox -Identity <UserPrincipalName> | Format-List ArchiveStatus, ArchiveDatabase to confirm ArchiveStatus is 'Active'. In Outlook or Outlook on the web, the user should see an 'In-Place Archive' folder.

## Rollback
To disable the archive: Set-Mailbox -Identity <UserPrincipalName> -Archive -Disabled. To remove the retention policy: Set-Mailbox -Identity <UserPrincipalName> -RetentionPolicy $null.

## References
- Microsoft Learn: 'Enable archive mailboxes in Exchange Online'
- Microsoft Learn: 'Default Retention Policy in Exchange Online' - https://learn.microsoft.com/en-us/exchange/security-and-compliance/messaging-records-management/default-retention-policy
