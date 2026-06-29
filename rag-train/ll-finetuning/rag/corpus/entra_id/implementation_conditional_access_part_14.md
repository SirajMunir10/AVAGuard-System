# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure a Conditional Access policy for autonomous agent access?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policy templates

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Create new policy from templates.
2. Select Show more to view all policy templates in each category.
3. Choose the 'Configure policy for autonomous agent access' template.
4. Review the policy settings summary.
5. Edit the policy to customize based on organizational needs, including modifying excluded users and groups if necessary.
6. By default, the policy is created in report-only mode. Test and monitor usage to ensure the intended result before turning on the policy.

## Validation
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Policies. 2. Locate the policy created from the 'Configure policy for autonomous agent access' template. 3. Confirm the policy is listed with the expected name and status (Report-only). 4. Review the policy settings: under Assignments, verify that the target resources and conditions match the template defaults. 5. Under Access controls, confirm the grant or session controls are as defined. 6. Use the 'What If' tool to simulate a sign-in from an autonomous agent and verify the policy applies as expected. 7. Check the Sign-in logs for any test sign-ins to ensure the policy is evaluated and reported correctly.

## Rollback
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Policies. 2. Select the policy created from the 'Configure policy for autonomous agent access' template. 3. Click 'Delete' and confirm to remove the policy entirely. 4. Alternatively, set the policy to 'Off' to disable it without deletion. 5. If the policy was enabled, switch it back to 'Report-only' mode to stop enforcement while retaining configuration. 6. Verify that no unintended access blocks or grants remain by checking the Sign-in logs for affected users or agents.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
