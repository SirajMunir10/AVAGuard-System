# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to implement risk-based Conditional Access with Microsoft Entra ID P2 for multifactor authentication?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra ID P2 license provides risk-based Conditional Access that adapts to user patterns and minimizes multifactor authentication prompts.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use risk-based Conditional Access to adapt to user's patterns and minimize multifactor authentication prompts.
2. This provides the strongest security position and improved user experience.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Verify that a policy exists with assignments that include 'All users' or specific users/groups, and conditions that include 'Sign-in risk' or 'User risk' set to a level such as 'High' or 'Medium and above'.
4. Confirm that the policy grants access requiring 'Require multifactor authentication'.
5. Use the 'What If' tool to simulate a user sign-in with a risk level matching the policy conditions and confirm that MFA is required.
6. Optionally, review the Microsoft Entra ID P2 license assignment for the users to ensure they are licensed for Identity Protection and risk-based policies.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Locate the risk-based Conditional Access policy created during remediation.
4. Set the policy state to 'Off' or delete the policy entirely.
5. If the policy was created with a specific exclusion group, ensure that group is removed from exclusions to restore previous access behavior.
6. Verify that no other policies enforce risk-based MFA that could conflict with the rollback.
7. Monitor sign-in logs for any unexpected access changes after disabling the policy.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing>
