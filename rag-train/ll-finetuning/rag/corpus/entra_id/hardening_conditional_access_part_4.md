# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
A tenant has no Conditional Access policies enforcing multifactor authentication for all users. What hardening steps should be taken to align with Microsoft's security baseline?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** No Conditional Access policies exist; legacy per-user MFA is enabled for some administrators.

## Symptoms
- No Conditional Access policies are configured in the Microsoft Entra admin center under Protection > Conditional Access.
- Legacy per-user MFA is enabled but does not enforce MFA for all users or block legacy authentication.

## Error Codes
N/A

## Root Causes
1. Conditional Access policies have not been created or deployed.
2. Reliance on per-user MFA instead of policy-based enforcement.

## Remediation Steps
1. Create a Conditional Access policy named 'Baseline policy: Require MFA for all users' with the following settings: Assignments > Users and groups > Include > All users; Cloud apps or actions > Include > All cloud apps; Conditions > Client apps > Configure > Yes > Select 'Browser' and 'Mobile apps and desktop clients'; Access controls > Grant > Require multifactor authentication > Select 'Require all the selected controls'; Enable policy > Report-only initially, then switch to On after validation.
2. Disable legacy per-user MFA after the Conditional Access policy is enforced to avoid conflicting configurations.

## Validation
Sign in as a test user without MFA registered; verify that the user is prompted to register and complete MFA. Confirm in the Conditional Access 'What If' tool that the policy applies to the test user.

## Rollback
Set the Conditional Access policy to 'Off' or delete the policy. Re-enable per-user MFA if needed via the Microsoft Entra admin center > Users > Per-user MFA.

## References
- Microsoft Learn: Conditional Access policy for requiring MFA for all users
