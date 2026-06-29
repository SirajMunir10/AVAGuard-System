# Troubleshooting: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Troubleshooting

## Scenario / Query
Why are items not being permanently deleted from the Recoverable Items folder after the retention period ends?

## Environment Context
- **Tenant Type:** Exchange Online
- **Configuration:** Retention policies or labels applied to Exchange data

## Symptoms
- Items remain in the Recoverable Items folder beyond the expected retention period
- Timer job does not delete items as scheduled

## Error Codes
N/A

## Root Causes
1. The timer job can take up to seven days to run
2. The Exchange location must contain at least 10 MB for the timer job to process
3. Items configured for disposition review are never permanently deleted until disposition is confirmed
4. Permanent deletion is suspended if the same item must be retained due to another retention policy, retention label, or eDiscovery hold

## Remediation Steps
1. Wait up to seven days for the timer job to run
2. Ensure the Exchange location has at least 10 MB of data
3. Check for conflicting retention policies or labels that retain the item
4. Verify if the item is under eDiscovery holds for legal or investigative reasons
5. For items with disposition review, confirm disposition to allow permanent deletion

## Validation
1. Run `Get-MailboxFolderStatistics -Identity <user> -FolderScope RecoverableItems | ft Name, ItemsInFolder, FolderSize` to confirm the Recoverable Items folder size is at least 10 MB. 2. Use `Get-Mailbox -Identity <user> | fl RetentionPolicy` to verify the assigned retention policy. 3. Run `Get-RetentionPolicy -Identity <policy> | fl RetentionEnabled, RetentionHoldEnabled` to ensure retention is enabled and not on hold. 4. Check for conflicting policies with `Get-RetentionPolicy | Where-Object {$_.RetentionEnabled -eq $true}` and verify no eDiscovery holds using `Get-MailboxSearch | Where-Object {$_.InPlaceHoldEnabled -eq $true}`. 5. For items under disposition review, run `Get-ComplianceTag -Identity <tag> | fl DispositionReviewEnabled` to confirm disposition is required and then use `Get-RecoverableItems -Identity <user> -ItemType DispositionReview` to list pending items.

## Rollback
1. If the timer job has not run, wait up to seven days as documented. 2. If the mailbox size is below 10 MB, add dummy data (e.g., send a test email) to increase folder size. 3. If a conflicting retention policy is found, remove or modify the conflicting policy using `Set-RetentionPolicy -Identity <policy> -RetentionEnabled $false` or adjust retention dates. 4. If an eDiscovery hold is active, remove the hold with `Remove-MailboxSearch -Identity <search>` after confirming legal requirements are met. 5. For disposition review items, confirm disposition via `Set-ComplianceTag -Identity <tag> -DispositionReviewEnabled $false` or manually approve disposition in the Purview portal.

## References
- <https://learn.microsoft.com/en-us/purview/retention-policies-exchange>
