# Implementation: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Implementation

## Scenario / Query
How do retention settings for Exchange handle items that are modified or permanently deleted during the retention period?

## Environment Context
- **Tenant Type:** Exchange Online
- **Configuration:** Retention settings set to retain and delete

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When an item is modified or permanently deleted (SHIFT+DELETE or deleted from Deleted Items) during the retention period, the item is moved or copied to the Recoverable Items folder
2. A timer job runs periodically and identifies items whose retention period has expired
3. These items are permanently deleted within 14 days of the end of the retention period (default setting, configurable up to 30 days)

## Validation
1. Use Exchange Online PowerShell to verify that a modified or permanently deleted item is present in the Recoverable Items folder of the user's mailbox. Run: Get-MailboxFolderStatistics -Identity <user> -FolderScope RecoverableItems | Format-Table Folder, ItemsInFolder. 2. Confirm that the retention hold is applied by checking the mailbox's RetentionHoldEnabled property: Get-Mailbox -Identity <user> | fl RetentionHoldEnabled. 3. After the retention period expires, verify that the item is permanently removed by checking the RecoverableItems folder again and confirming the item count decreases within 14 days (or the configured deletion interval).

## Rollback
1. If an item was incorrectly moved to Recoverable Items, restore it to its original location using: Search-Mailbox -Identity <user> -SearchQuery 'Subject:<subject>' -TargetMailbox <admin> -TargetFolder Recovery -DeleteContent. 2. To disable retention hold if it was mistakenly enabled: Set-Mailbox -Identity <user> -RetentionHoldEnabled $false. 3. If the timer job prematurely deleted items, recover them from the secondary Recoverable Items folder (if within the deleted item retention period) using: Get-RecoverableItems -Identity <user> -Subject '<subject>' | Restore-RecoverableItems.

## References
- <https://learn.microsoft.com/en-us/purview/retention-policies-exchange>
