# Optimization: Mailbox Archiving

**Domain:** Exchange Online
**Subdomain:** Mailbox Archiving
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Exchange Online by enabling the archive mailbox for all users who have a specific license and are not already archived, and verify the change?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E3/E5 or Exchange Online Plan 2)
- **Configuration:** Archive mailbox feature is available but not enabled for all eligible users.

## Symptoms
- Users report they cannot archive emails manually or via retention policies.
- Compliance or legal team requests that archiving be enabled for all licensed users.
- Mailbox storage quotas are being reached, but archive is not in use.

## Error Codes
N/A

## Root Causes
1. Archive mailbox is not enabled by default; it must be explicitly enabled per user or via PowerShell.
2. Only users with an Exchange Online Plan 2 or higher (or equivalent) license are eligible for archiving.

## Remediation Steps
1. Connect to Exchange Online PowerShell using the Exchange Online V2 module.
2. Run the following command to enable the archive for all eligible users who do not already have one: Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited | Where-Object {$_.ArchiveStatus -eq 'None' -and $_.RecipientTypeDetails -eq 'UserMailbox'} | Enable-Mailbox -Archive
3. Verify the change by running: Get-Mailbox -Archive | Format-Table Name, ArchiveStatus, ArchiveDatabase

## Validation
Run the verification command and confirm that the ArchiveStatus column shows 'Active' for the targeted mailboxes.

## Rollback
To disable an archive mailbox, run: Disable-Mailbox -Identity <UserPrincipalName> -Archive. Note: This removes the archive and its contents permanently.

## References
- <https://learn.microsoft.com/en-us/purview/enable-archive-mailboxes>
