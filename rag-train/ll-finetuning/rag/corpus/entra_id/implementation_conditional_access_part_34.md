# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure the Device platforms condition in Conditional Access for agents' user accounts?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policy with Device platforms and Agent execution environments conditions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For agents' user accounts, apply the Device platforms condition only when the agent session is initiated from an endpoint.
2. Use the Device platforms condition with the Agent execution environments condition to avoid targeting agents that run directly in cloud infrastructure.

## Validation
1. Sign in to the Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy configured for agents' user accounts. 4. Under Assignments > Conditions > Device platforms, confirm that the policy is configured to include specific platforms (e.g., Windows, iOS, Android) and not set to 'Any device'. 5. Under Assignments > Conditions > Agent execution environments, confirm that the condition is configured to include 'Endpoint' and exclude 'Cloud infrastructure' or similar. 6. Use the 'What If' tool in Conditional Access to simulate a sign-in from an agent user account from an endpoint device and verify the policy applies. 7. Use the 'What If' tool to simulate a sign-in from the same agent user account from a cloud infrastructure environment and verify the policy does not apply.

## Rollback
1. Sign in to the Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified. 4. Under Assignments > Conditions > Device platforms, revert the setting to the previous configuration (e.g., set to 'Any device' or remove specific platform inclusions). 5. Under Assignments > Conditions > Agent execution environments, revert the setting to the previous configuration (e.g., remove the condition or set to 'Any environment'). 6. Save the policy changes. 7. Use the 'What If' tool to verify that the policy behavior returns to the original state.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
