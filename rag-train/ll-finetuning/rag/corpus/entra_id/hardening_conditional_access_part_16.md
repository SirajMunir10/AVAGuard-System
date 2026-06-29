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
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select each Conditional Access policy that is scoped to 'All users' or a specific set of users. 4. Under 'Assignments' > 'Users and groups', confirm that 'Exclude' includes the service accounts (e.g., Microsoft Entra Connect Sync Account) and service principals. 5. Use Microsoft Graph PowerShell: `Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.Conditions.Users.IncludeUsers -contains 'All'}` and verify that `ExcludeUsers` or `ExcludeGroups` contains the service account object IDs. 6. For service principals, confirm that no policy is scoped to 'All users' without excluding the service principal object IDs. 7. Optionally, test by signing in with the service account and verifying that the policy does not block access.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy where exclusions were added. 4. Under 'Assignments' > 'Users and groups', remove the excluded service accounts or service principals from the 'Exclude' list. 5. If the policy was previously scoped to 'All users' without exclusions, revert to that original configuration. 6. Use Microsoft Graph PowerShell: `Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId <policy-id> -Conditions @{Users = @{IncludeUsers = @('All'); ExcludeUsers = @()}}` to remove exclusions. 7. Verify that the policy is again applied to all users, including service accounts.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
