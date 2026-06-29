# Implementation: Multifactor Authentication

**Domain:** Entra ID
**Subdomain:** Multifactor Authentication
**Incident Type:** Implementation

## Scenario / Query
How to integrate Microsoft Entra multifactor authentication with AD FS resources for on-premises and cloud applications?

## Environment Context
- **Tenant Type:** federated with Microsoft Entra ID
- **Configuration:** AD FS 2016 or newer, Azure multifactor authentication adapter

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Azure multifactor authentication adapter with AD FS 2016 or newer.
2. Configure Microsoft Entra multifactor authentication as an authentication provider with AD FS resources both on-premises and in the cloud.

## Validation
1. On the AD FS server, open the AD FS Management console and navigate to 'Authentication Policies' > 'Primary Authentication' > 'Global Settings'. Verify that 'Azure multifactor authentication' is listed as an additional authentication method. 2. Run the PowerShell command 'Get-AdfsGlobalAuthenticationPolicy' and confirm that 'AdditionalAuthenticationProvider' includes 'AzureMfaAuthentication'. 3. Test user sign-in to a federated application and verify that the user is prompted for MFA via Microsoft Entra ID. 4. Check the AD FS admin event log (Event ID 1200) for successful MFA authentication events.

## Rollback
1. On the AD FS server, open the AD FS Management console, navigate to 'Authentication Policies' > 'Primary Authentication' > 'Global Settings', and remove 'Azure multifactor authentication' from the list of additional authentication methods. 2. Run the PowerShell command 'Set-AdfsGlobalAuthenticationPolicy -AdditionalAuthenticationProvider @()' to clear the MFA provider. 3. Restart the AD FS service using 'Restart-Service adfssrv'. 4. Verify that users can sign in without MFA prompts and that the previous authentication methods are restored.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
