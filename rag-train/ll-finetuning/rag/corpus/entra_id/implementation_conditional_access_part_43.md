# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to apply filter for devices condition for agent user accounts in Conditional Access?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access and agent sessions
- **Configuration:** Conditional Access policy for agent user accounts

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Apply filter for devices condition for agent user accounts only when the agent session is initiated from an endpoint
2. Use the Agent execution environments condition when targeting specific approved devices for agents running on endpoints

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified for agent user accounts. 4. Under Assignments > Conditions > Filter for devices, confirm that the filter rule includes the required device attributes (e.g., device.trustType -eq 'ServerAD' or device.isCompliant -eq True) and that the policy is set to 'On' or 'Report-only' as intended. 5. Use the 'What If' tool to simulate an agent user sign-in from an endpoint and verify that the policy applies as expected. 6. Review the Conditional Access insights and reporting workbook to confirm that the policy is being evaluated for agent sessions.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified. 4. Under Assignments > Conditions > Filter for devices, either clear the filter rule or set it to the previous value. 5. If the filter was added as a new condition, remove the filter for devices condition entirely. 6. Under Enable policy, set the policy to 'Off' if the change caused issues. 7. Use the 'What If' tool to verify that the policy no longer applies to agent user accounts. 8. Monitor sign-in logs for any remaining policy enforcement issues.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions#filter-for-devices>
