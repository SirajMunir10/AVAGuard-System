# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to exclude service accounts and service principals from Conditional Access policies scoped to users?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policies, service accounts, service principals

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Exclude service accounts and service principals, such as the Microsoft Entra Connect Sync Account, from Conditional Access policies scoped to users.
2. Calls made by service principals aren't blocked by Conditional Access policies scoped to users.
3. Use Conditional Access for workload identities to define policies that target service principals.
4. If your organization uses these accounts in scripts or code, replace them with managed identities.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. For each policy scoped to 'All users' or a specific user group, select the policy and go to the 'Assignments' > 'Users and groups' section. 4. Under 'Exclude', confirm that the service account (e.g., Microsoft Entra Connect Sync Account) and any service principals are listed. 5. Use Microsoft Graph PowerShell: `Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.Conditions.Users.ExcludeUsers -contains 'object-id-of-service-account'}` to verify exclusions. 6. Test by simulating a sign-in from the service account using the 'What If' tool in Conditional Access – ensure the policy is not applied.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy where exclusions were added. 4. In 'Assignments' > 'Users and groups' > 'Exclude', remove the service account and service principals from the exclusion list. 5. Click 'Save'. 6. If using Microsoft Graph PowerShell, run: `Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId 'policy-id' -Conditions @{Users = @{ExcludeUsers = @()}}` to clear exclusions. 7. Verify the policy is now applied to the service account using the 'What If' tool.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
