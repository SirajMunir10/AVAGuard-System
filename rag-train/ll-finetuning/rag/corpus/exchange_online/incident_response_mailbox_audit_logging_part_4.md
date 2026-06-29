# Incident Response: Mailbox Audit Logging

**Domain:** Exchange Online
**Subdomain:** Mailbox Audit Logging
**Incident Type:** Incident Response

## Scenario / Query
An administrator suspects that a user's mailbox was accessed by an unauthorized party. How can the admin enable and search the mailbox audit log to identify the suspicious access events, and what specific actions should be taken to preserve the audit data and remediate the breach?

## Environment Context
- **Tenant Type:** Enterprise (E5 licensed)
- **Configuration:** Mailbox audit logging is enabled by default for all mailboxes in Microsoft 365, but the admin wants to verify the configuration and run a specific audit log search for non-owner mailbox access events.

## Symptoms
- User reports unexpected email read or deletion
- Mailbox rules created without user knowledge
- Suspicious sign-in activity for the user's account

## Error Codes
N/A

## Root Causes
1. Compromised user credentials
2. Misconfigured mailbox forwarding or delegation
3. Insider threat or unauthorized access by another user

## Remediation Steps
1. 1. Verify mailbox audit logging is enabled: Run `Get-Mailbox -Identity <UserPrincipalName> | fl AuditEnabled` in Exchange Online PowerShell. If disabled, enable with `Set-Mailbox -Identity <UserPrincipalName> -AuditEnabled $true`.
2. 2. Search the mailbox audit log for non-owner access: Use `Search-MailboxAuditLog -Identity <UserPrincipalName> -LogonTypes Owner,Delegate,Admin -StartDate <date> -EndDate <date> -ShowDetails` to identify unauthorized access.
3. 3. If suspicious activity is confirmed, reset the user's password and revoke all active sessions via the Microsoft 365 admin center.
4. 4. Remove any unauthorized mailbox rules: Run `Get-Mailbox -Identity <UserPrincipalName> | Get-InboxRule` and remove suspicious rules with `Remove-InboxRule`.
5. 5. Enable multi-factor authentication (MFA) for the affected user and review conditional access policies.
6. 6. Preserve audit logs by exporting them to a CSV file using `Search-MailboxAuditLog -Identity <UserPrincipalName> -StartDate <date> -EndDate <date> -ShowDetails | Export-Csv -Path 'audit.csv'`.

## Validation
Run `Get-Mailbox -Identity <UserPrincipalName> | fl AuditEnabled` to confirm audit logging is enabled. Then run a new audit log search to verify that no further unauthorized access has occurred.

## Rollback
If audit logging was disabled and then enabled, no rollback is needed. If mailbox rules were removed incorrectly, restore from a recent backup or re-create the rules manually.

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mailbox-auditing/manage-mailbox-auditing>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/search-mailboxauditlog>
