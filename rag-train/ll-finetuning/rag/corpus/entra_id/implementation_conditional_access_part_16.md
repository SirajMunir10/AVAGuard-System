# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to export and import a Conditional Access policy JSON definition for programmatic workflows?

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
2. Select a policy template and choose 'Export the JSON definition'.
3. Edit the JSON definition as needed.
4. Navigate to the main Conditional Access policies page.
5. Use the 'Upload policy file' option to import the edited JSON definition.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator or Global Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the newly imported policy in the list. 4. Select the policy to open its details. 5. Verify that the policy name, assignments (users/groups, cloud apps, conditions), and access controls (grant/block/session) match the JSON definition you uploaded. 6. Optionally, use the 'What If' tool to simulate a user sign-in and confirm the policy applies as expected.

## Rollback
1. In the Microsoft Entra admin center, go to Protection > Conditional Access > Policies. 2. Find the problematic imported policy. 3. Select the policy and choose 'Delete' to remove it entirely. 4. If you have a backup of the original JSON definition, re-import it using the 'Upload policy file' option. 5. Alternatively, manually recreate the policy from scratch using the original settings. 6. Verify that the restored policy is in the expected state and does not cause unintended access issues.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
