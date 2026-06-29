# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to create a Conditional Access policy from a template to block high-risk agent identities?

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
3. Choose the 'Block high-risk agent identities' template.
4. Review the policy settings summary.
5. Edit the policy to customize based on organizational needs, including modifying excluded users and groups if necessary.
6. By default, the policy is created in report-only mode. Test and monitor usage to ensure the intended result before turning on the policy.

## Validation
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Policies. 2. Locate the policy named 'Block high-risk agent identities' (or your custom name). 3. Confirm the policy is listed with status 'Report-only' (or 'On' if enabled). 4. Review the policy settings: under Assignments > Users and groups, verify the included/excluded users and groups match your organization's requirements. 5. Under Assignments > Cloud apps or actions, confirm 'All cloud apps' is selected. 6. Under Conditions > Client apps, verify 'Exchange ActiveSync clients' and 'Other clients' are selected. 7. Under Access controls > Grant, confirm 'Block access' is selected. 8. Use the 'What If' tool with a test user account that simulates a high-risk agent identity to verify the policy would block access. 9. Check the Sign-in logs for the test user to confirm the policy was evaluated and the result is 'Blocked'.

## Rollback
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Policies. 2. Select the policy named 'Block high-risk agent identities' (or your custom name). 3. Click 'Delete' and confirm deletion to remove the policy entirely. 4. Alternatively, if you want to keep the policy but disable it, set the policy status to 'Off' and save. 5. If the policy was enabled (status 'On'), change the status to 'Report-only' first to monitor impact before disabling or deleting. 6. Verify that the policy no longer appears in the list of active policies (status 'Off' or deleted). 7. Use the 'What If' tool with the same test user to confirm the policy is no longer enforced.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
