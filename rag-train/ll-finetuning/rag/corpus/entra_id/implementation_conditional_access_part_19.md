# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to implement a Conditional Access policy that blocks access except for specific apps?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access licensing
- **Configuration:** Conditional Access policies, cloud apps assignment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a Conditional Access policy that targets all cloud apps
2. Configure an exclusion for the specific apps that should be allowed
3. Set the grant control to block access

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the newly created policy and confirm its state is 'On'. 4. Select the policy and verify: - Under 'Assignments > Cloud apps or actions', 'Include' is set to 'All cloud apps'. - Under 'Exclude', the specific allowed apps are listed. - Under 'Access controls > Grant', 'Block access' is selected. 5. Use the 'What If' tool to simulate a sign-in from a user assigned to the policy, targeting an excluded app; confirm the result is 'Blocked' for non-excluded apps and 'Grant' for excluded apps. 6. Optionally, perform a test sign-in with a test user to validate the policy behavior.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy and set its state to 'Off' to immediately disable it. 4. If the policy must be removed entirely, select it and choose 'Delete', confirming the deletion. 5. Alternatively, edit the policy to remove the 'Block access' grant control and set it to 'Grant access' or remove the exclusions to restore previous access behavior.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
