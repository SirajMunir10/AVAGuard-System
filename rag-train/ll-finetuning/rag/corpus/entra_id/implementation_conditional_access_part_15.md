# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to modify excluded users and groups in a Conditional Access policy created from a template?

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
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Policies.
2. Select the policy to open the editor.
3. Modify the excluded users and groups to select accounts you want to exclude.

## Validation
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Policies.
2. Select the modified policy to open the editor.
3. Under 'Assignments' > 'Users and groups', confirm that the 'Exclude' tab lists the intended users and groups.
4. Optionally, use the 'What If' tool to simulate sign-in for an excluded user and verify that the policy does not apply.

## Rollback
1. Navigate to Microsoft Entra admin center > Entra ID > Conditional Access > Policies.
2. Select the policy to open the editor.
3. Under 'Assignments' > 'Users and groups', go to the 'Exclude' tab.
4. Remove the newly added users and groups, or re-add the previously excluded ones.
5. Save the policy.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
