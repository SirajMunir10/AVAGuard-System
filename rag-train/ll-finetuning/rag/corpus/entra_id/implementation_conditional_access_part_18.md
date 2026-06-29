# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to implement a Conditional Access policy that blocks access by location?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access licensing
- **Configuration:** Conditional Access policies, named locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a Conditional Access policy that targets specific users or groups
2. Configure the policy to block access based on location conditions (e.g., using named locations)

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the newly created policy. 3. Confirm the policy is set to 'On' and the 'Users' assignment includes the intended users or groups. 4. Under 'Cloud apps or actions', verify the targeted applications are selected. 5. Under 'Conditions > Locations', confirm the 'Include' tab lists the correct named locations (e.g., 'Blocked Countries') and the 'Exclude' tab lists any trusted locations if needed. 6. Under 'Access controls > Grant', verify 'Block access' is selected. 7. Use the 'What If' tool (https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) to simulate a sign-in from a blocked location and confirm the result shows 'Blocked'. 8. Optionally, sign in from a blocked location with a test user and verify access is denied with a message indicating the policy.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy that is causing issues. 4. To temporarily disable the policy, set its 'Enable policy' toggle to 'Off' and select 'Save'. 5. To permanently remove the policy, select the policy, then select 'Delete' and confirm. 6. If the policy was created but not yet enabled, simply delete it without enabling. 7. If the issue is due to incorrect location configuration, edit the policy: under 'Conditions > Locations', adjust the included or excluded named locations as needed, then select 'Save'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
