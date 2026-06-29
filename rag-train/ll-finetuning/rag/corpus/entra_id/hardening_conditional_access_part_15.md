# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to exclude emergency access or break-glass accounts from Conditional Access policies to prevent lockout due to policy misconfiguration?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Exclude emergency access or break-glass accounts from your Conditional Access policies to prevent lockout due to policy misconfiguration.
2. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with the Conditional Access Administrator or Global Administrator role.
2. Navigate to Protection > Conditional Access > Policies.
3. For each Conditional Access policy, select the policy and then select the Users or Users and groups tab.
4. Under Exclude, confirm that the emergency access or break-glass accounts (e.g., cloud-only accounts with *.onmicrosoft.com suffix and no MFA) are listed.
5. To test, sign in with one of the excluded emergency access accounts and verify that the Conditional Access policy does not apply (e.g., you can access the resource without meeting the policy conditions).
6. Optionally, use the What If tool in Conditional Access to simulate a sign-in from the excluded account and confirm the policy is not enforced.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with the Conditional Access Administrator or Global Administrator role.
2. Navigate to Protection > Conditional Access > Policies.
3. For each policy where emergency access accounts were excluded, select the policy and then select the Users or Users and groups tab.
4. Under Exclude, remove the emergency access accounts from the exclusion list.
5. Select Save to apply the change.
6. If the exclusion was added via a group, remove the group from the Exclude list or remove the accounts from that group.
7. Verify that the policy now applies to the emergency access accounts as expected.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
