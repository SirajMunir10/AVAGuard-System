# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
Users get invalid username/password error when using Pass-through Authentication

## Environment Context
- **Tenant Type:** hybrid
- **Configuration:** Pass-through Authentication agent installed

## Symptoms
- Users get invalid username/password error

## Error Codes
N/A

## Root Causes
1. User's on-premises UserPrincipalName (UPN) is different than the user's cloud UPN
2. On-premises UPN is non-routable
3. Microsoft Entra Connect server is not domain joined

## Remediation Steps
1. Create a test account
2. Import the PowerShell module on the agent machine: Import-Module "C:\Program Files\Microsoft Azure AD Connect Authentication Agent\Modules\PassthroughAuthPSModule\PassthroughAuthPSModule.psd1"
3. Run the Invoke PowerShell command: Invoke-PassthroughAuthOnPremLogonTroubleshooter
4. When prompted to enter credentials, enter the same username and password that are used to sign in to https://login.microsoftonline.com
5. If the same username/password error occurs, the Pass-through Authentication agent is working correctly and the issue may be that the on-premises UPN is non-routable. See Configuring Alternate Login ID for more information.
6. If the Microsoft Entra Connect server is not domain joined, ensure it meets the prerequisite of being domain joined as mentioned in Microsoft Entra Connect: Prerequisites

## Validation
If you get the same username/password error, this means that the Pass-through Authentication agent is working correctly

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
