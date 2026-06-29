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
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with at least the Conditional Access Administrator role.
2. Navigate to Protection > Conditional Access > Policies.
3. For each Conditional Access policy, select the policy, then under Assignments > Users and groups, confirm that the emergency access or break-glass accounts are listed under Exclude.
4. Optionally, run the following Microsoft Graph PowerShell command to verify exclusions: Get-MgIdentityConditionalAccessPolicy | Where-Object { $_.Conditions.Users.ExcludeUsers -contains 'break-glass-user-id' }.
5. Test sign-in with an excluded break-glass account to ensure it is not blocked by any Conditional Access policy.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with at least the Conditional Access Administrator role.
2. Navigate to Protection > Conditional Access > Policies.
3. For each policy where break-glass accounts were excluded, select the policy, then under Assignments > Users and groups, remove the break-glass accounts from the Exclude list.
4. Alternatively, run the following Microsoft Graph PowerShell command to remove the exclusion: Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId 'policy-id' -Conditions @{ Users = @{ ExcludeUsers = @() } }.
5. Verify the change by reviewing the policy assignments and testing sign-in with a break-glass account to confirm it is now subject to the policy.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
