# Incident Response: Authentication methods

**Domain:** Entra ID
**Subdomain:** Authentication methods
**Incident Type:** Incident Response

## Scenario / Query
How to handle a user who is locked out of MFA and has no backup authentication method?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** MFA registration with multiple methods recommended

## Symptoms
- User is unable to authenticate because their primary MFA method is unavailable
- User has no backup MFA method registered

## Error Codes
N/A

## Root Causes
1. User registered only one MFA method
2. Primary MFA method is unavailable (e.g., lost phone, broken token)

## Remediation Steps
1. Provide the user with a Temporary Access Pass so they can manage their own authentication methods
2. Alternatively, provide a Temporary Access Pass to enable temporary access to resources
3. As an administrator, update the user's methods: select the user in the Microsoft Entra admin center, then select Entra ID > Authentication methods and update their methods

## Validation
1. Confirm the user can sign in using the Temporary Access Pass: `Test-MgUserAuthenticationMethod -UserId <user-id> -AuthenticationMethodId <TAP-id>` (Microsoft Graph PowerShell). 2. Verify the user has registered a new MFA method: `Get-MgUserAuthenticationMethod -UserId <user-id>` should show at least two methods. 3. Check that the user can complete MFA with the new method by performing a test sign-in.

## Rollback
1. Revoke the Temporary Access Pass: `Remove-MgUserAuthenticationMethod -UserId <user-id> -AuthenticationMethodId <TAP-id>`. 2. If admin updated methods, revert to previous state using `Update-MgUserAuthenticationMethod` with the original method details. 3. Notify the user that changes have been reversed and provide alternative support options.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
