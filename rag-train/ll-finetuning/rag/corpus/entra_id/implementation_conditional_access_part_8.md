# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
A Conditional Access policy targeting all cloud apps with a block control is not being enforced for users who are not assigned the policy. What is the most likely misconfiguration?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policy with 'Block access' control, assigned to 'All users', targeting 'All cloud apps'

## Symptoms
- Users not assigned to the policy can still access cloud apps
- Policy appears enabled in the Conditional Access blade
- No sign-in logs show the policy being evaluated for unassigned users

## Error Codes
N/A

## Root Causes
1. The policy was configured with 'Include' for users but the 'Exclude' list inadvertently contains 'All users' or a dynamic group that includes all users
2. The policy was saved in 'Report-only' mode instead of 'On'
3. The policy assignment scope was set to 'All users' but the policy was not enabled

## Remediation Steps
1. Navigate to Azure AD > Security > Conditional Access > select the policy
2. Under 'Assignments > Users and groups', verify that 'Include' is set to 'All users' and 'Exclude' does not contain any unintended groups or users
3. Under 'Enable policy', confirm it is set to 'On' (not 'Report-only')
4. Save the policy and test with a user who was previously not blocked

## Validation
Sign in as a test user who should be blocked; verify that access is denied and that the sign-in log shows the Conditional Access policy was applied with result 'Block'.

## Rollback
Set the policy to 'Report-only' or disable it by setting 'Enable policy' to 'Off'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-block-access>
