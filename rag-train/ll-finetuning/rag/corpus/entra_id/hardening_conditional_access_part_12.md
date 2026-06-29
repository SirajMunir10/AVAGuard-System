# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How do I configure Conditional Access policies to block legacy authentication clients that don't support MFA or device state information?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policy client apps condition

## Symptoms
- Sign-ins from legacy authentication clients are blocked by Conditional Access grant controls like requiring MFA or compliant devices
- Legacy authentication clients cannot pass multifactor authentication (MFA) or device state information

## Error Codes
N/A

## Root Causes
1. Legacy authentication clients do not support MFA and do not pass device state information
2. Conditional Access policies apply to all client app types by default even if the client apps condition is not configured

## Remediation Steps
1. Exclude accounts that must use legacy authentication from the policy
2. Configure the policy to only apply to modern authentication clients

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified. 4. Under Assignments > Users and groups, confirm the excluded users/groups are listed. 5. Under Assignments > Cloud apps or actions, confirm the policy applies to the intended apps. 6. Under Conditions > Client apps, confirm 'Modern authentication clients' is selected and 'Legacy authentication clients' is not selected. 7. Use the 'What If' tool to test a sign-in from a legacy authentication client for an excluded user and verify the policy does not apply. 8. Use the 'What If' tool to test a sign-in from a modern authentication client for a non-excluded user and verify the policy applies.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified. 4. Under Assignments > Users and groups, remove any excluded users/groups. 5. Under Conditions > Client apps, select 'All client apps' or re-select 'Legacy authentication clients' if previously removed. 6. Save the policy. 7. Monitor sign-in logs to confirm legacy authentication clients are again subject to the policy.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
