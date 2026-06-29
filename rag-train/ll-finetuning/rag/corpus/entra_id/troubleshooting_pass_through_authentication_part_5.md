# Troubleshooting: Pass-through Authentication

**Domain:** Entra ID
**Subdomain:** Pass-through Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Authentication Agent registration failure due to token or account authorization errors in Microsoft Entra Connect Pass-through Authentication?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Pass-through Authentication with Authentication Agent

## Symptoms
- Registration of the Authentication Agent failed due to token or account authorization errors

## Error Codes
N/A

## Root Causes
1. Use of a non-cloud-only Hybrid Identity Administrator account
2. MFA-enabled Hybrid Identity Administrator account causing known issue

## Remediation Steps
1. Ensure that you use a cloud-only Hybrid Identity Administrator account for all Microsoft Entra Connect or standalone Authentication Agent installation and registration operations
2. Turn off MFA temporarily (only to complete the operations) as a workaround for the known issue with MFA-enabled Hybrid Identity Administrator accounts

## Validation
1. Confirm the account used for registration is cloud-only: Run `Get-MsolUser -UserPrincipalName <adminUPN> | Select-Object -Property UserPrincipalName, IsLicensed, StrongAuthenticationRequirements, StrongAuthenticationMethods` and verify that StrongAuthenticationRequirements and StrongAuthenticationMethods are empty or null. 2. If MFA was disabled, verify MFA is turned off for the account: In the Microsoft Entra admin center, go to Identity > Users > All users > select the admin account > Authentication methods, and confirm no MFA methods are registered. 3. Re-run the Authentication Agent registration: On the server, launch the Microsoft Entra Connect Authentication Agent wizard and complete registration. 4. Check the agent status: In the Microsoft Entra admin center, go to Identity > Hybrid management > Pass-through authentication, and verify the agent shows as 'Active'.

## Rollback
1. If a cloud-only account was used and registration still fails, re-enable MFA for the original Hybrid Identity Administrator account: In the Microsoft Entra admin center, go to Identity > Users > All users > select the admin account > Authentication methods, and add the required MFA methods. 2. If MFA was temporarily disabled, re-enable MFA for the Hybrid Identity Administrator account: In the Microsoft Entra admin center, go to Identity > Users > All users > select the admin account > Authentication methods, and configure MFA enforcement. 3. If the agent registration fails after changes, uninstall the Authentication Agent: Run 'C:\Program Files\Microsoft Azure AD Connect Authentication Agent\Modules\Remove-AuthenticationAgent.ps1' as an administrator. 4. Restore the original registration state by re-running the Microsoft Entra Connect wizard and selecting the previous configuration.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
