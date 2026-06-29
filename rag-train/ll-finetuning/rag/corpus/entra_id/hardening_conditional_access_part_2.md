# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
A tenant has no Conditional Access policies enforcing multifactor authentication for all users. How should an administrator harden the tenant by creating a baseline policy requiring MFA for all users, and what are the documented steps and considerations?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** No Conditional Access policies exist; all users are in scope.

## Symptoms
- No Conditional Access policies are configured in the Microsoft Entra admin center under Protection > Conditional Access.
- Users can sign in without any additional authentication requirements.

## Error Codes
N/A

## Root Causes
1. Lack of Conditional Access policies to enforce security controls like MFA.

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator, Security Administrator, or Global Administrator.
2. Browse to Protection > Conditional Access > Policies.
3. Select New policy and provide a name, e.g., 'Require MFA for all users'.
4. Under Assignments > Users, select All users and ensure Exclude includes emergency break-glass accounts.
5. Under Cloud apps or actions, select All cloud apps.
6. Under Conditions, configure applicable conditions (e.g., locations, device platforms) as needed.
7. Under Access controls > Grant, select Grant access and check Require multifactor authentication.
8. Set Enable policy to Report-only initially to validate impact, then switch to On after testing.
9. Monitor sign-in logs and Conditional Access insights to confirm expected behavior.

## Validation
After enabling the policy, verify that users are prompted for MFA during sign-in. Use the What If tool under Conditional Access > Policy > What If to test a user sign-in scenario.

## Rollback
Set the policy to Off or delete it. If Off, the policy remains inactive but can be re-enabled. If deleted, recreate from scratch if needed.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-all-users-mfa>
