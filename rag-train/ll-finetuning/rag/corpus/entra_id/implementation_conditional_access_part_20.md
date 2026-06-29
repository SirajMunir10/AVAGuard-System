# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to plan and implement Conditional Access policies to enforce Microsoft Entra multifactor authentication?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policies under Entra ID > Conditional Access

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure Conditional Access policies under Entra ID > Conditional Access in the Microsoft Entra admin center.
2. Create a Conditional Access policy to prompt for Microsoft Entra multifactor authentication when a user signs in.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator or Global Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Locate the newly created policy (e.g., 'Require MFA for all users').
4. Confirm the policy is set to 'On' (Report-only or On).
5. Select the policy and verify the following assignments:
   - Users and groups: target users or 'All users'.
   - Cloud apps or actions: 'All cloud apps' or specific apps.
6. Under Access controls > Grant, confirm 'Grant access' is selected and 'Require multifactor authentication' is checked.
7. Under Session, confirm no conflicting controls (e.g., 'Sign-in frequency' or 'Persistent browser session') are set that could bypass MFA.
8. Perform a test sign-in as a targeted user from a non-trusted device/location and verify that MFA is prompted.
9. Check the Sign-in logs (Monitoring > Sign-in logs) for the test user; confirm the 'Requirement' column shows 'MFA' and the 'Result' column shows 'Success'.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator or Global Administrator.
2. Navigate to Protection > Conditional Access > Policies.
3. Locate the policy that was created or modified.
4. To disable the policy without deleting it: set the policy state to 'Off' and select 'Save'.
5. To permanently remove the policy: select the policy, click 'Delete', and confirm.
6. If the policy was part of a broader rollout, consider setting it to 'Report-only' mode first to assess impact before full disablement.
7. Verify that users can sign in without MFA prompts by performing a test sign-in from a non-trusted device/location.
8. Monitor the Sign-in logs for any authentication failures caused by the policy removal.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted#plan-conditional-access-policies>
