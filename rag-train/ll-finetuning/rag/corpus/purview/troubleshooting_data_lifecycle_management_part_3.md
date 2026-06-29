# Troubleshooting: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Troubleshooting

## Scenario / Query
Why are expired items not being permanently deleted within the expected timeframe from Exchange mailboxes?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Retention policies with delete action

## Symptoms
- Items whose retention period has expired are not permanently deleted within 14 days of the end of the retention period.

## Error Codes
N/A

## Root Causes
1. The default deletion grace period is 14 days but may be configured up to 30 days.

## Remediation Steps
1. Verify the configured deletion grace period setting (default 14 days, configurable up to 30 days).
2. Wait for the periodic process that runs on all folders in the mailbox to identify and permanently delete expired items.

## Validation
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. Run Get-MailboxFolderStatistics -Identity <user> -FolderScope RecoverableItems | ft Name, ItemsInFolder, FolderAndSubfolderSize. 3. Check the 'Purges' folder count; if expired items remain, they have not been permanently deleted. 4. Verify the deletion grace period by running Get-Mailbox -Identity <user> | fl RetentionPolicy,RetentionHoldEnabled. 5. Confirm the retention policy assigned to the mailbox by running Get-RetentionPolicy -Identity <policy> | fl RetentionPolicyName,RetentionPolicyAction. 6. Wait at least 14 days (or the configured grace period) after the retention period ends, then re-run the folder statistics to confirm the Purges folder count decreases.

## Rollback
1. If the deletion grace period was changed from the default 14 days to a longer value (up to 30 days), revert it by setting the mailbox's retention policy to a policy with the default grace period using Set-Mailbox -Identity <user> -RetentionPolicy <defaultPolicy>. 2. If the issue persists, temporarily place the mailbox on retention hold using Set-Mailbox -Identity <user> -RetentionHoldEnabled $true to prevent permanent deletion while troubleshooting. 3. Contact Microsoft Support if the periodic cleanup process does not run as expected, as this is a backend service behavior not directly configurable.

## References
- <https://learn.microsoft.com/en-us/purview/retention-policies-exchange>
