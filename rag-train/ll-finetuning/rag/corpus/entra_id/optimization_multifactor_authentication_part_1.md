# Optimization: Multifactor Authentication

**Domain:** Entra ID
**Subdomain:** Multifactor Authentication
**Incident Type:** Optimization

## Scenario / Query
How to plan user session lifetime for Microsoft Entra multifactor authentication deployment?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Session lifetime settings, sign-in frequency policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Understand the needs of your business and users and configure settings that provide the best balance for your environment.
2. Use devices with Primary Refresh Tokens (PRT) for improved end user experience.
3. Reduce the session lifetime with sign-in frequency policy only on specific business use cases.

## Validation
1. Confirm that the sign-in frequency policy is applied to the intended users or groups by running: Get-MgIdentityConditionalAccessPolicy -Filter "displayName eq 'Sign-in Frequency Policy'". 2. Verify the session token lifetime for a test user by signing in and checking the token expiration using a tool like jwt.ms or by inspecting the 'exp' claim in the token. 3. Ensure that devices with Primary Refresh Tokens (PRT) are registered by running: Get-MgDevice -Filter "operatingSystem eq 'Windows'" | Select-Object -Property DisplayName, TrustType. 4. Validate that the sign-in frequency prompt appears only for the specified business use cases by simulating a login from a non-trusted location or application.

## Rollback
1. Remove or disable the sign-in frequency policy by running: Remove-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId <policy-id>. 2. Reset the session lifetime settings to the default by clearing any custom sign-in frequency configuration in the Conditional Access policy. 3. If PRT-based devices were modified, revert to the previous device registration state by re-enrolling devices or restoring from backup. 4. Monitor user sign-in logs for any unexpected authentication prompts and adjust the policy scope as needed.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
