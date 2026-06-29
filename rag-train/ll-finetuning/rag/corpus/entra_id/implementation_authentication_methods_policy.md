# Implementation: Authentication methods policy

**Domain:** Entra ID
**Subdomain:** Authentication methods policy
**Incident Type:** Implementation

## Scenario / Query
How to choose and enable authentication methods for MFA in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** MFA settings or Authentication methods policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose from the list of available authentication methods, evaluating each in terms of security, usability, and availability.
2. Enable more than one MFA method so that users have a backup method available in case their primary method is unavailable.
3. For the best flexibility and usability, use the Microsoft Authenticator app.
4. Control the authentication methods available in your tenant. For example, you may want to block some of the least secure methods, such as SMS.
5. Microsoft Authenticator (Push notification and passwordless phone sign-in) can be configured via MFA settings or Authentication methods policy.
6. Authenticator passwordless phone sign-in can be scoped to users and groups.
7. FIDO2 security key can be configured via Authentication methods policy and can be scoped to users and groups.
8. Software or Hardware OATH tokens can be configured via MFA settings.
9. SMS verification can be configured via MFA settings.
10. Manage SMS sign-in for primary authentication in authentication policy; SMS sign-in can be scoped to users and groups.
11. Voice calls can be configured via Authentication methods policy.

## Validation
1. Sign in to the Microsoft Entra admin center as an Authentication Policy Administrator. 2. Navigate to Protection > Authentication methods > Policies. 3. Verify that the desired authentication methods (e.g., Microsoft Authenticator, FIDO2 security key, OATH tokens, SMS, Voice calls) are enabled and configured according to the remediation steps. 4. For each method, confirm that the correct user and group scoping is applied (e.g., Authenticator passwordless phone sign-in scoped to specific users/groups). 5. Use the 'Test' feature in the Authentication methods policy to simulate a user sign-in and confirm that the enabled methods appear as options. 6. Run the following Microsoft Graph PowerShell command to programmatically verify the policy: Get-MgPolicyAuthenticationMethodPolicy | Select-Object -ExpandProperty AuthenticationMethodConfigurations.

## Rollback
1. Sign in to the Microsoft Entra admin center as an Authentication Policy Administrator. 2. Navigate to Protection > Authentication methods > Policies. 3. For each authentication method that was enabled or modified, revert to the previous state: disable the method or remove scoping as needed. 4. If a method was blocked (e.g., SMS), re-enable it by setting the state to 'Enabled' and restoring any previous user/group targeting. 5. Use the following Microsoft Graph PowerShell command to reset a specific method configuration to default: Update-MgPolicyAuthenticationMethodPolicy -AuthenticationMethodConfigurations @(@{Id='<methodId>'; State='disabled'}). 6. Verify that the rollback is complete by repeating the validation steps to ensure the policy matches the pre-change state.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
