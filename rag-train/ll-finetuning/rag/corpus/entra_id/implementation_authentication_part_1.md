# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to convert users from per-user MFA to Conditional Access based MFA?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Per-user MFA enabled and enforced

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Conditional Access for all users
2. Manually disable per-user multifactor authentication

## Validation
1. Confirm that Conditional Access policies are enabled and applied to all users by running: Connect-MgGraph -Scopes 'Policy.Read.All'; Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.State -eq 'enabled'} | Format-List DisplayName, State, Conditions, GrantControls. 2. Verify that per-user MFA is disabled for each user by running: Get-MgUser -All | Where-Object {$_.StrongAuthenticationRequirements -ne $null} | Select-Object UserPrincipalName, StrongAuthenticationRequirements. 3. Test authentication for a sample user by signing in at https://login.microsoftonline.com and confirming that MFA is prompted only when required by the Conditional Access policy.

## Rollback
1. Re-enable per-user MFA for all users by running: $users = Get-MgUser -All; foreach ($user in $users) { Update-MgUser -UserId $user.Id -StrongAuthenticationRequirements @(@{State='Enabled'}) }. 2. Disable the Conditional Access policies that were enabled by running: Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.State -eq 'enabled'} | ForEach-Object { Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId $_.Id -State 'disabled' }. 3. Confirm that per-user MFA is enforced by checking that users are prompted for MFA during sign-in.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
