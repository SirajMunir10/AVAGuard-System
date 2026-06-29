# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How can I enforce multifactor authentication for all users in my tenant using Conditional Access policies, and what are the documented steps to create and validate such a policy?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** No Conditional Access policies currently assigned to all users

## Symptoms
- Users can sign in without being prompted for MFA even when MFA is enabled per-user
- No Conditional Access policy exists that targets all cloud apps and requires MFA

## Error Codes
N/A

## Root Causes
1. Conditional Access policy requiring MFA for all users is not configured
2. Per-user MFA is enabled but not enforced by a Conditional Access policy

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator, Security Administrator, or Global Administrator.
2. Browse to Protection > Conditional Access > Policies.
3. Select New policy and provide a name (e.g., 'Require MFA for all users').
4. Under Assignments > Users, select All users.
5. Under Cloud apps or actions, select All cloud apps.
6. Under Access controls > Grant, select Grant access, check Require multifactor authentication, and select Select.
7. Set Enable policy to Report-only initially, then after validation set to On.
8. For validation, use the What If tool under Conditional Access to test the policy against a test user.

## Validation
Use the Conditional Access What If tool to simulate a sign-in for a test user; verify that the policy 'Require MFA for all users' is listed under 'Policies that will apply' and that MFA is required.

## Rollback
Set the policy to Off or delete the policy. If per-user MFA was also enabled, disable it via the legacy MFA portal (Users > Per-user MFA).

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-all-users-mfa>
