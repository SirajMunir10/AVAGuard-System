# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to harden Exchange Online by blocking legacy authentication protocols via Conditional Access?

## Environment Context
- **Tenant Type:** Entra ID tenant with Exchange Online
- **Configuration:** Conditional Access policy targeting 'Other clients' to block basic/legacy authentication

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Block SMTP used by POP and IMAP clients to send email messages.
2. Block Autodiscover used by Outlook and EAS clients to find and connect to mailboxes.
3. Block Exchange Online PowerShell; if blocked, use the Exchange Online PowerShell Module with multifactor authentication.
4. Block Exchange Web Services (EWS) used by Outlook, Outlook for Mac, and non-Microsoft apps.
5. Block IMAP4 used by IMAP email clients.
6. Block MAPI over HTTP (MAPI/HTTP) used by Outlook 2010 and later.
7. Block Offline Address Book (OAB) used by Outlook.
8. Block Outlook Anywhere (RPC over HTTP) used by Outlook 2016 and earlier.
9. Block Outlook Service used by Mail and Calendar app for Windows 10.
10. Block POP3 used by POP email clients.
11. Block Reporting Web Services used to retrieve report data in Exchange Online.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy that targets 'Other clients' and blocks legacy authentication. 4. Open the policy and confirm that under 'Assignments' > 'Users and groups', the intended users or groups are included. 5. Under 'Assignments' > 'Cloud apps or actions', confirm 'Office 365 Exchange Online' is selected. 6. Under 'Conditions' > 'Client apps', confirm 'Exchange ActiveSync clients' and 'Other clients' are selected. 7. Under 'Access controls' > 'Grant', confirm 'Block access' is selected. 8. Enable the policy and save. 9. Use a test account that is subject to the policy to attempt to connect to Exchange Online using a legacy protocol (e.g., IMAP, POP3, SMTP). Verify that the connection is blocked and an error message is displayed. 10. Run the following Exchange Online PowerShell command to confirm that legacy protocols are blocked: Get-CASMailbox -Identity testuser@contoso.com | Format-List *Enabled. Verify that IMAPEnabled, POPEnabled, SmtpClientAuthenticationDisabled, and other legacy protocol settings are set to $false or blocked as intended.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy that blocks legacy authentication for Exchange Online. 4. Disable the policy by toggling 'Enable policy' to 'Off' and save. 5. Alternatively, delete the policy by selecting it and clicking 'Delete'. 6. If the policy was applied to a specific group, remove that group from the policy assignment. 7. To re-enable legacy protocols for specific users, run the following Exchange Online PowerShell commands: Set-CASMailbox -Identity user@contoso.com -IMAPEnabled $true -POPEnabled $true -SmtpClientAuthenticationDisabled $false. 8. To re-enable Autodiscover, EWS, or other protocols, use the appropriate Exchange Online cmdlets (e.g., Set-CASMailbox -Identity user@contoso.com -EwsEnabled $true). 9. Verify that the changes take effect by testing connectivity with the legacy protocol.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
