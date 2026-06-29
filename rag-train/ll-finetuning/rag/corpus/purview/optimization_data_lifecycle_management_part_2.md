# Optimization: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Optimization

## Scenario / Query
A Microsoft 365 tenant has retention policies that are not being applied to Exchange mailboxes as expected. The policies are published but items are not being retained or deleted according to the configured settings. How can the admin verify and optimize the application of retention policies to Exchange mailboxes?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview
- **Configuration:** Retention policies configured for Exchange mailboxes; policies show as 'On (pending)' or 'On (success)' but items are not being retained/deleted as expected.

## Symptoms
- Retention policies show as 'On (pending)' for an extended period
- Items in user mailboxes are not being retained or deleted according to policy
- Managed Folder Assistant (MFA) is not processing mailboxes

## Error Codes
N/A

## Root Causes
1. Managed Folder Assistant is not running or is not processing the mailbox
2. Retention policy has not been applied to the mailbox (mailbox not in policy scope)
3. Large mailbox size or high item count causing processing delays

## Remediation Steps
1. Verify that the retention policy is published and the mailbox is included in the policy scope using the Exchange admin center or PowerShell
2. Start the Managed Folder Assistant for the affected mailbox using the PowerShell command: Start-ManagedFolderAssistant -Identity <mailbox>
3. Monitor the processing status with: Get-MailboxFolderStatistics -Identity <mailbox> | fl ItemsInFolder, FolderSize
4. If the mailbox is large, consider splitting the mailbox into smaller archives or adjusting the policy to reduce processing load

## Validation
Run Get-ManagedFolderAssistantStatus to confirm the assistant is processing the mailbox and check that retention tags are applied to folders.

## Rollback
If the Managed Folder Assistant causes unexpected deletions, stop it with: Stop-ManagedFolderAssistant -Identity <mailbox>

## References
- <https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-permissions-for-recipients/start-the-managed-folder-assistant>
