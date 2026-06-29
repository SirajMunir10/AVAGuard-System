# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure Conditional Access policy to block legacy authentication protocols for Exchange Online?

## Environment Context
- **Tenant Type:** Entra ID tenant with Exchange Online
- **Configuration:** Conditional Access policy targeting Exchange Online with client apps condition set to 'Other clients'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Conditional Access policy, under 'Client apps', select 'Exchange ActiveSync clients' to block EAS protocol.
2. In the Conditional Access policy, under 'Client apps', select 'Other clients' to block legacy protocols including SMTP, Autodiscover, Exchange Online PowerShell, EWS, IMAP4, MAPI/HTTP, OAB, Outlook Anywhere, Outlook Service, POP3, and Reporting Web Services.
3. For Exchange Online PowerShell, if Basic authentication is blocked, use the Exchange Online PowerShell Module with multifactor authentication. See instructions: Connect to Exchange Online PowerShell using multifactor authentication.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate and open the policy that was configured to block legacy authentication for Exchange Online. 4. Under 'Assignments' > 'Cloud apps or actions', confirm 'Exchange Online' is selected. 5. Under 'Access controls' > 'Grant', confirm 'Block access' is selected. 6. Under 'Conditions' > 'Client apps', confirm that 'Exchange ActiveSync clients' and 'Other clients' are both checked. 7. Use the 'What If' tool (Protection > Conditional Access > What If) with a test user, target cloud app 'Exchange Online', and client app 'Other clients' to verify the policy applies as expected. 8. Attempt to connect to Exchange Online using a legacy protocol (e.g., SMTP, IMAP4, POP3) with Basic authentication; the connection should be denied. 9. For Exchange Online PowerShell, run `Connect-ExchangeOnline -UserPrincipalName <testuser>@<domain>.onmicrosoft.com` without the `-UseRPSSession` switch; if Basic auth is blocked, the connection should fail unless multifactor authentication is used.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate and open the policy that blocks legacy authentication for Exchange Online. 4. Under 'Conditions' > 'Client apps', uncheck 'Exchange ActiveSync clients' and/or 'Other clients' to allow those protocols. Alternatively, set the policy to 'Off' or delete it. 5. If the policy was set to 'Block access', change the 'Grant' control to 'Grant access' or remove the policy assignment. 6. Wait up to 30 minutes for policy changes to propagate. 7. Verify that legacy protocol connections (e.g., SMTP, IMAP4, POP3) with Basic authentication are now allowed. 8. For Exchange Online PowerShell, confirm that `Connect-ExchangeOnline -UserPrincipalName <testuser>@<domain>.onmicrosoft.com` succeeds without multifactor authentication.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
