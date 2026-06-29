# Hardening: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Hardening

## Scenario / Query
How to configure risk-based policies for Microsoft Entra multifactor authentication using Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with ID Protection enabled
- **Configuration:** Risk-based policies instead of named locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Consider using risk-based policies instead of named locations if your organization uses Microsoft Entra ID Protection to detect risk signals.
2. Create policies to force password changes when there's a threat of compromised identity.
3. Require MFA when a sign-in is deemed at risk such as leaked credentials, sign-ins from anonymous IP addresses, and more.
4. Risk policies include: Require all users to register for Microsoft Entra multifactor authentication.
5. Require a password change for users that are high-risk.
6. Require MFA for users with medium or high sign in risk.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Verify that a policy named 'Require MFA for medium or high sign-in risk' exists and is enabled.
4. Confirm the policy assignments: Users and groups = 'All users', Cloud apps or actions = 'All cloud apps', Conditions > Sign-in risk = 'Medium and High', Grant > Grant access = selected, Require multifactor authentication = selected.
5. Navigate to Protection > Identity Protection > Risk policies.
6. Verify that the 'User risk policy' is set to 'On' with Target = 'All users', User risk level = 'High', Access = 'Allow access, Require password change'.
7. Confirm that the 'Sign-in risk policy' is set to 'On' with Target = 'All users', Sign-in risk level = 'Medium and High', Access = 'Allow access, Require multifactor authentication'.
8. Use the 'What If' tool in Conditional Access to simulate a sign-in from a risky IP address and confirm the policy requires MFA.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Locate the policy 'Require MFA for medium or high sign-in risk' and set its state to 'Off' or delete it.
4. Navigate to Protection > Identity Protection > Risk policies.
5. For the 'User risk policy', set the toggle to 'Off'.
6. For the 'Sign-in risk policy', set the toggle to 'Off'.
7. If named locations were previously used, navigate to Protection > Conditional Access > Named locations and re-add the required IP ranges or country/region locations.
8. Re-create any Conditional Access policies that were replaced by the risk-based policies, ensuring they reference the named locations as conditions.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
