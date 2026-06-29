# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
How do I configure risk-based Conditional Access policies to enable end-user self-remediation for user risk and sign-in risk?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection and Conditional Access
- **Configuration:** Risk-based Conditional Access policies must be configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure and enable risk policies
2. Require multifactor authentication for all users
3. Implement password hash sync

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Verify that a policy named 'User risk policy' exists with: Assignments > Users > Include > All users; Cloud apps or actions > Include > All cloud apps; Conditions > User risk > Configure > Yes > High; Access controls > Grant > Grant access > Require multifactor authentication > Require password change > Require reauthentication (if applicable).
4. Verify that a policy named 'Sign-in risk policy' exists with: Assignments > Users > Include > All users; Cloud apps or actions > Include > All cloud apps; Conditions > Sign-in risk > Configure > Yes > Medium and above (or High); Access controls > Grant > Grant access > Require multifactor authentication.
5. Confirm both policies are set to 'On' (Report-only or On).
6. Use the 'What If' tool for a test user to confirm the policies apply as expected.
7. In Identity Protection > Risky users, confirm that a user with high risk can self-remediate by performing a secure password change or reauthentication.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Security Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Locate the 'User risk policy' and set it to 'Off' or delete it.
4. Locate the 'Sign-in risk policy' and set it to 'Off' or delete it.
5. If password hash sync was enabled, navigate to Protection > Identity Protection > MFA registration policy and disable it if it was enabled as part of the remediation.
6. Verify that no risk-based policies are active by reviewing the list of Conditional Access policies.
7. If users were blocked due to risk, unblock them in Identity Protection > Risky users by selecting the user and choosing 'Dismiss user risk' or 'Confirm safe'.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
