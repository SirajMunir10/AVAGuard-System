# Incident Response: Mailbox Audit Logging

**Domain:** Exchange Online
**Subdomain:** Mailbox Audit Logging
**Incident Type:** Incident Response

## Scenario / Query
A user reports that mailbox folder permissions were changed without their knowledge. How can an administrator determine who modified the permissions and when, using Exchange Online mailbox audit logging?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Mailbox audit logging is enabled by default for all users in Exchange Online; however, the administrator must search the audit log to retrieve specific events.

## Symptoms
- User notices unexpected changes to folder-level permissions in their mailbox.
- User reports that other users can access folders they should not be able to see.

## Error Codes
N/A

## Root Causes
1. A user with delegated permissions or an administrator modified folder permissions without authorization.
2. Mailbox audit logging was not being reviewed regularly, so the change went undetected.

## Remediation Steps
1. Connect to Exchange Online PowerShell using the EXO V2 module.
2. Run the Search-MailboxAuditLog cmdlet with the appropriate parameters to identify the specific change. For example: Search-MailboxAuditLog -Identity <user> -LogonTypes Admin,Delegate -Operations UpdateFolderPermissions -StartDate <date> -EndDate <date>
3. Review the output to identify the user who made the change, the time of the change, and the specific folder permissions modified.
4. If unauthorized, revert the folder permissions to the correct state using Set-MailboxFolderPermission or Remove-MailboxFolderPermission.
5. Consider implementing alerts for mailbox audit log events using Microsoft  Defender for Cloud Apps or a custom alert policy in the Microsoft 365 compliance portal.

## Validation
Run Search-MailboxAuditLog again with the same parameters to confirm that the unauthorized change is no longer present and that the corrected permissions are reflected.

## Rollback
If the remediation steps inadvertently remove legitimate permissions, reapply the original permissions using the same Set-MailboxFolderPermission cmdlet with the correct parameters as documented in the audit log output.

## References
- Search-MailboxAuditLog (ExchangePowerShell) | Microsoft Learn
