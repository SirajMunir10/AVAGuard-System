# Implementation: Conditional Access (Policy cannot be created because it would block all access)

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator attempts to create a Conditional Access policy that requires multi-factor authentication for all users, but the policy fails to save with a 'Policy cannot be created because it would block all access' error. What is the cause and how should the policy be correctly configured?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Default Conditional Access policies are enabled; no custom policies exist yet.

## Symptoms
- Conditional Access policy creation fails in the Azure portal
- Error message: 'Policy cannot be created because it would block all access'

## Error Codes
- `Policy cannot be created because it would block all access`

## Root Causes
1. The policy is configured to require MFA for all users and all cloud apps, but does not exclude at least one user (e.g., a break-glass account) or does not include a fallback grant control, which would lock out all administrators including the policy creator.

## Remediation Steps
1. Add at least one emergency access or break-glass account to the 'Exclude' list of the policy.
2. Ensure the policy includes a 'Require multi-factor authentication' grant control, but also configure a session control such as 'Sign-in frequency' to avoid permanent lockout.
3. Save the policy after adding the exclusion.

## Validation
After adding the exclusion, the policy saves successfully. Verify by signing in as the excluded user and confirming MFA is not required, then sign in as a non-excluded user and confirm MFA is enforced.

## Rollback
Delete the newly created Conditional Access policy in the Azure portal under 'Azure Active Directory > Security > Conditional Access > Policies'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-all-users-mfa>
