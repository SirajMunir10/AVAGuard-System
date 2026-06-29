# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
A Conditional Access policy targeting all cloud apps is not being enforced for users assigned to the policy. What configuration step might be missing?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policy with 'All cloud apps' target, assigned to a test user group

## Symptoms
- Users in the assigned group are not prompted for MFA or blocked as expected
- Sign-in logs show the policy is not evaluated for those users

## Error Codes
N/A

## Root Causes
1. The Conditional Access policy was created in 'Report-only' mode instead of 'On'
2. The policy does not include any conditions (e.g., user risk, device platform) that are required to trigger enforcement

## Remediation Steps
1. Navigate to Entra admin center > Protection > Conditional Access > Policies
2. Select the policy and set 'Enable policy' to 'On'
3. Ensure at least one condition (e.g., user risk, device platform) is configured if the policy targets 'All cloud apps'
4. Save the policy and test with a user in the assigned group

## Validation
Sign in as a test user and confirm the policy is enforced (e.g., MFA prompt appears). Check sign-in logs under 'Conditional Access' tab for policy evaluation details.

## Rollback
Set the policy back to 'Report-only' mode or disable it by setting 'Enable policy' to 'Off'.

## References
- Microsoft Learn: 'Conditional Access policy components' - https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policies
