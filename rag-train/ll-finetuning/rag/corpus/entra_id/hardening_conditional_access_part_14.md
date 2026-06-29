# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to block legacy authentication protocols in Exchange Online using Conditional Access conditions?

## Environment Context
- **Tenant Type:** Entra ID tenant with Exchange Online
- **Configuration:** Conditional Access policy conditions for client apps

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Block Basic authentication for Exchange Online PowerShell, then use the Exchange Online PowerShell Module to connect. For instructions, see Connect to Exchange Online PowerShell using multifactor authentication.
2. Block legacy authentication protocols: Exchange Web Services (EWS), IMAP4, MAPI over HTTP (MAPI/HTTP), Offline Address Book (OAB), Outlook Anywhere (RPC over HTTP), Outlook Service, POP3, Reporting Web Services, SMTP, Autodiscover.

## Validation
1. Connect to Exchange Online PowerShell using modern authentication (MFA).
2. Run: Get-OrganizationConfig | Select-Object *BasicAuth*,*Legacy* to confirm Basic auth is disabled.
3. Run: Get-CASMailbox | Select-Object *Enabled - to verify legacy protocols (EWS, IMAP, POP, SMTP) are disabled.
4. In Entra admin center, navigate to Conditional Access > Policies, select the policy that blocks legacy auth, and confirm 'Client apps' condition includes 'Exchange ActiveSync clients' and 'Other clients'.
5. Use 'What If' tool in Conditional Access with a test user and legacy client app to verify the policy would block access.

## Rollback
1. Connect to Exchange Online PowerShell using modern authentication.
2. Run: Set-OrganizationConfig -BasicAuthEnabled $true to re-enable Basic auth if needed.
3. Run: Set-CASMailbox -Identity <user> -EWSEnabled $true -ImapEnabled $true -PopEnabled $true -SmtpEnabled $true to re-enable legacy protocols per user.
4. In Entra admin center, navigate to Conditional Access > Policies, select the policy that blocks legacy auth, and set 'Enable policy' to 'Off' or delete the policy.
5. Verify legacy protocol access is restored by testing with a legacy client.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
