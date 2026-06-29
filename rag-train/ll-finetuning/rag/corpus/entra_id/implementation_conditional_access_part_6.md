# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
A Conditional Access policy is not being applied to guest users even though the policy targets 'All users'. What configuration step is missing?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policy targeting 'All users' with a grant control requiring MFA; guest users from external organizations are not prompted for MFA.

## Symptoms
- Guest users are not prompted for MFA when accessing resources protected by a Conditional Access policy that targets 'All users'.
- Sign-in logs show guest users bypassing the Conditional Access policy.

## Error Codes
N/A

## Root Causes
1. The Conditional Access policy does not include 'External users' in the 'Users and groups' assignment. By default, 'All users' includes only users in the directory, not guest users.
2. Guest user access is not explicitly scoped in the policy.

## Remediation Steps
1. Edit the Conditional Access policy and under 'Assignments' > 'Users and groups', select 'All users' and also check the box for 'External users' (or 'Guest or external users' depending on the portal version).
2. Alternatively, create a separate Conditional Access policy specifically targeting 'Guest or external users' with the required controls.
3. Ensure that the policy is in 'Report-only' mode first to validate the impact before enabling it.

## Validation
Sign in as a guest user and verify that the Conditional Access policy is triggered (e.g., MFA prompt appears). Check the Conditional Access insights and reporting workbook for policy evaluation details.

## Rollback
Remove the 'External users' assignment from the policy or disable the policy. If a separate policy was created, delete or disable it.

## References
- Microsoft Learn: 'Conditional Access: Users and groups' - https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-users-groups
