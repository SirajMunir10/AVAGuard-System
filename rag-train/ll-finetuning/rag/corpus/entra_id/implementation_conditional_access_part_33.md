# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How do I configure the Agent execution environments condition in a Conditional Access policy to exclude cloud-only agents from endpoint-dependent controls?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Agent execution environments condition (Preview)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Agent execution environments condition to scope a Conditional Access policy to agents' user account sessions initiated from endpoints.
2. This condition helps avoid applying endpoint-dependent controls to agents that run directly in the cloud and don't have a device to evaluate.
3. When a policy uses this condition, agents that aren't running on a device are excluded from evaluation.
4. Use this condition with other endpoint-based conditions, such as Device platforms, Filter for devices, and Network, when you want to enforce controls only for agents running on managed endpoints.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was configured with the Agent execution environments condition. 4. Under Assignments > Conditions > Agent execution environments, confirm that the configuration is set to 'Exclude' and that 'Cloud-only agents' is selected. 5. Use the 'What If' tool to simulate a sign-in from a cloud-only agent (e.g., a service principal used for automation) and verify that the policy is not applied. 6. Simulate a sign-in from an agent running on a managed endpoint (e.g., a user with a hybrid Azure AD joined device) and confirm that the policy is applied as expected.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified. 4. Under Assignments > Conditions > Agent execution environments, change the setting to 'Not configured' or remove the exclusion of 'Cloud-only agents'. 5. Alternatively, if the policy was newly created, delete the policy entirely. 6. Use the 'What If' tool to verify that the previous behavior is restored (e.g., all agents are evaluated against the policy).

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
