# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How do I configure multiple conditions in a Conditional Access policy to improve access decisions for sensitive applications?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policy conditions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Admins use one or more signals to improve policy decisions.
2. Admins combine multiple conditions to create specific, fine-grained Conditional Access policies.
3. When users access a sensitive application, admins might consider multiple conditions in their access decisions, such as: Risk information from Microsoft Entra ID Protection, Agent execution environment, Network location, Device information.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy you configured with multiple conditions. 4. Under Assignments > Conditions, verify that each condition (e.g., User risk, Device platforms, Locations, Client apps) is set to 'Yes' and configured with the desired values. 5. Under Access controls > Grant, confirm that the required controls (e.g., Require multifactor authentication, Require device to be marked as compliant) are selected. 6. Set the policy to 'Report-only' mode and use the Conditional Access insights and reporting workbook to simulate a sign-in from a user matching the conditions. 7. Confirm that the policy evaluation shows the intended grant controls are applied. 8. Finally, set the policy to 'On' and perform a test sign-in with a user who meets all conditions to verify the access decision.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that is causing issues. 4. Under Assignments > Conditions, set each condition back to 'No' or remove the specific configurations that were added. 5. Alternatively, set the policy to 'Off' to disable it entirely. 6. If the policy was created new, delete the policy by selecting it and choosing 'Delete'. 7. Monitor sign-in logs for any affected users and ensure access is restored. 8. If needed, re-enable any previous policy that was replaced.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
