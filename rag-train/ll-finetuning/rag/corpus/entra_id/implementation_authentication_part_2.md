# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to plan user registration for Microsoft Entra multifactor authentication deployment?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Multifactor authentication deployment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Determine how users will register their methods.
2. Consider that authentication methods such as Voice and SMS allow preregistration.
3. Consider that authentication methods such as the Authenticator App require user interaction.

## Validation
1. Confirm that the authentication methods policy is configured as intended: Run `Get-MgPolicyAuthenticationMethodPolicy` in Microsoft Graph PowerShell to list all authentication method policies. Verify that 'voice' and 'sms' methods are enabled with 'includeTargets' set to the appropriate user groups. 2. Check that users can see available registration methods: Sign in as a test user to https://aka.ms/mfasetup and confirm that 'Phone' (voice/sms) and 'Microsoft Authenticator' options appear. 3. Validate that preregistered methods (voice/sms) are applied without user interaction: For a test user who has a phone number already in their profile, trigger a conditional access policy requiring MFA and verify that the user receives a voice call or SMS without needing to register first. 4. Ensure the Authenticator App registration flow works: For a test user without preregistered methods, navigate to https://aka.ms/mfasetup and complete the Authenticator App setup; confirm the app shows the account and generates codes.

## Rollback
1. If the authentication methods policy was changed, revert to the previous configuration: Use `Update-MgPolicyAuthenticationMethodPolicy` to restore the previous set of enabled methods and target groups. 2. If user registration states were modified, reset them: For each affected user, run `Reset-MgUserAuthenticationMethod -UserId <user-id>` to clear their registered methods. 3. If conditional access policies were updated to require MFA, disable or remove those policies: Use `Update-MgIdentityConditionalAccessPolicy` to set the policy state to 'disabled' or remove it with `Remove-MgIdentityConditionalAccessPolicy`. 4. If any test users were added to groups for piloting, remove them: Use `Remove-MgGroupMember -GroupId <group-id> -DirectoryObjectId <user-id>` to revert group membership.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
