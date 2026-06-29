# Optimization: Conditional Access (53003)

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Optimization

## Scenario / Query
How can I reduce sign-in failures caused by legacy authentication in my Entra ID tenant?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Conditional Access policies are enabled but legacy authentication protocols (POP, IMAP, SMTP, ActiveSync) are not blocked.

## Symptoms
- High volume of sign-in failures from legacy authentication protocols
- Sign-in logs show failures with error code 53003 or 50053 for legacy clients
- Security alerts for legacy authentication usage

## Error Codes
- `53003`
- `50053`

## Root Causes
1. Legacy authentication protocols do not support modern authentication and bypass Conditional Access policies
2. No Conditional Access policy blocking legacy authentication

## Remediation Steps
1. Create a Conditional Access policy that blocks access from legacy authentication clients. In the Azure portal, go to Entra ID > Security > Conditional Access > New policy. Under Assignments > Cloud apps or actions, select All cloud apps. Under Conditions > Client apps, check 'Exchange ActiveSync clients' and 'Other clients'. Under Access controls > Grant, select Block access. Enable the policy.
2. Alternatively, enable the 'Baseline policy: Block legacy authentication' if available in your tenant.
3. For Exchange Online, disable legacy protocols per user or organization-wide using Exchange Online PowerShell: Set-CASMailbox -Identity <user> -ActiveSyncEnabled $false -ImapEnabled $false -PopEnabled $false -SmtpEnabled $false

## Validation
Verify in Entra ID sign-in logs that legacy authentication attempts are now blocked with error code 53003. Confirm that modern authentication clients (e.g., Outlook for Windows with modern auth) can still sign in successfully.

## Rollback
Disable the Conditional Access policy that blocks legacy authentication, or re-enable legacy protocols per user using Set-CASMailbox cmdlet.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-block-legacy>
