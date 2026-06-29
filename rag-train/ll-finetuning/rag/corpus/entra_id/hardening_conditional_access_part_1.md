# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How do I detect and remediate a tenant where legacy authentication protocols (POP3, IMAP, SMTP, ActiveSync) are still enabled, increasing the risk of password spray and replay attacks?

## Environment Context
- **Tenant Type:** production
- **Configuration:** Legacy authentication enabled for some users; no Conditional Access policy blocking legacy auth

## Symptoms
- Sign-in logs show successful authentications from legacy protocols (POP3, IMAP, SMTP, ActiveSync)
- Users report they can still connect using Outlook 2010 or older clients without modern authentication
- Sign-in logs show 'Client app' field as 'POP3' or 'IMAP' for some users

## Error Codes
N/A

## Root Causes
1. No Conditional Access policy exists to block legacy authentication
2. Tenant-level settings allow legacy protocols (e.g., Exchange Online allow list for POP/IMAP/SMTP)
3. Users have not been migrated to modern authentication clients

## Remediation Steps
1. Create a Conditional Access policy that blocks all legacy authentication protocols. In the Azure portal, go to Conditional Access > New policy, name it 'Block Legacy Authentication', assign all users, under 'Cloud apps or actions' select 'All cloud apps', under 'Conditions' > 'Client apps' check 'Exchange ActiveSync clients' and 'Other clients', set 'Grant' to 'Block access', and enable the policy.
2. Disable legacy protocols at the tenant level for Exchange Online: Connect to Exchange Online PowerShell and run `Set-CASMailbox -Identity <user> -PopEnabled $false -ImapEnabled $false -SmtpClientAuthenticationDisabled $true` for each user, or use a bulk script.
3. Communicate to users that they must upgrade to modern authentication-capable email clients (e.g., Outlook 2016 or later, Outlook for iOS/Android, or the Mail app on Windows 10/11).

## Validation
After policy creation, verify in Azure AD sign-in logs that no successful sign-ins show 'Client app' as POP3, IMAP, SMTP, or ActiveSync. Also run `Get-CASMailbox -ResultSize unlimited | Where-Object {$_.PopEnabled -eq $true -or $_.ImapEnabled -eq $true}` to confirm no user has legacy protocols enabled.

## Rollback
Delete or disable the Conditional Access policy 'Block Legacy Authentication'. Re-enable legacy protocols for specific users via Exchange Online PowerShell: `Set-CASMailbox -Identity <user> -PopEnabled $true -ImapEnabled $true -SmtpClientAuthenticationDisabled $false`.

## References
- <https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/block-legacy-authentication>
- CIS Microsoft 365 Foundations Benchmark v2.0.0, Control 3.1 â€“ 'Ensure legacy authentication is blocked'
