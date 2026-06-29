# Incident Response: Mail Flow and Transport Rules

**Domain:** Exchange Online
**Subdomain:** Mail Flow and Transport Rules
**Incident Type:** Incident Response

## Scenario / Query
A security analyst suspects that a compromised admin account created a malicious mail flow rule to exfiltrate sensitive data. How can the analyst identify and remove all transport rules created by that account in Exchange Online?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Exchange admin role assigned to the compromised account; mail flow rules (transport rules) enabled

## Symptoms
- Unexpected automatic forwarding of emails to external domains
- Mail flow rule reports showing rules created by an unknown or suspicious user
- Users reporting missing emails or emails sent to unintended recipients

## Error Codes
N/A

## Root Causes
1. Compromised Exchange administrator account used to create a mail flow rule that forwards messages to an external address

## Remediation Steps
1. 1. Connect to Exchange Online PowerShell using a secure admin account.
2. 2. Run 'Get-TransportRule | Format-List Name,Identity,Priority,State,CreatedBy,Description' to list all transport rules and their creators.
3. 3. Identify the malicious rule(s) created by the compromised account.
4. 4. Run 'Remove-TransportRule -Identity "<RuleIdentity>"' to delete each malicious rule.
5. 5. Revoke the compromised account's administrative roles and reset its credentials.
6. 6. Review and enable audit logging for Exchange admin actions if not already enabled.

## Validation
Run 'Get-TransportRule' again to confirm the malicious rules are no longer present. Verify that no unexpected forwarding is occurring by checking message trace for external forwarding.

## Rollback
If a rule was removed in error, re-create it using the original parameters from a backup or from the Exchange admin center's deleted rules recovery (if available within 30 days).

## References
- <https://learn.microsoft.com/en-us/powershell/module/exchange/remove-transportrule>
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules>
