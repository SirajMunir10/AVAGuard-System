# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
How to set up risk-based policies to allow users to self-remediate sign-in and user risks?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection
- **Configuration:** Risk-based policies configured for sign-in risk and user risk

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set up risk-based policies to allow users to self-remediate their sign-in and user risks
2. Configure policies so that if users pass the required access control (e.g., multifactor authentication or secure password change), their risks are automatically remediated

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risk policies. 3. Verify that a sign-in risk policy exists with the following settings: - Assignment: All users or targeted users. - Conditions: Sign-in risk level set to Medium and above (or your chosen threshold). - Access controls: Allow access and Require multifactor authentication. 4. Verify that a user risk policy exists with the following settings: - Assignment: All users or targeted users. - Conditions: User risk level set to Medium and above (or your chosen threshold). - Access controls: Allow access and Require password change. 5. Confirm that both policies are set to 'Enabled' or 'Report-only' as intended. 6. Use the 'What If' tool in Identity Protection to simulate a risky sign-in for a test user and confirm the policy triggers the expected access control (MFA or password change). 7. After the user completes the access control, check the user's risk state in Identity Protection > Risky users to verify the risk is remediated (state changes to 'Remediated').

## Rollback
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risk policies. 3. For the sign-in risk policy, set the policy to 'Disabled' or change the access control to 'Block access' (if previously 'Allow access'). 4. For the user risk policy, set the policy to 'Disabled' or change the access control to 'Block access' (if previously 'Allow access'). 5. If the policies were previously in 'Report-only' mode, revert them to 'Report-only'. 6. If any test users were affected, manually remediate their risks by navigating to Identity Protection > Risky users, selecting the user, and choosing 'Dismiss user risk' or 'Confirm user compromised' as appropriate. 7. Verify that no unintended access blocks or self-remediation prompts are active by testing sign-in with a non-privileged test account.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
