# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites and least privileged roles required to remediate and unblock users in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID P2 or Microsoft Entra Suite license required
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The User Administrator role is the least privileged role required to reset passwords.
2. The Security Operator role is the least privileged role required to dismiss user risk.
3. The Security Administrator role is the least privileged role required to create or edit risk-based policies.
4. The Conditional Access Administrator role is the least privileged role required to create or edit Conditional Access policies.

## Validation
1. Confirm that the user performing remediation has the required role: For password reset, verify the user is assigned the 'User Administrator' role by running: Get-MgDirectoryRole | Where-Object {$_.DisplayName -eq 'User Administrator'} | Get-MgDirectoryRoleMember. For dismissing user risk, verify the 'Security Operator' role: Get-MgDirectoryRole | Where-Object {$_.DisplayName -eq 'Security Operator'} | Get-MgDirectoryRoleMember. For creating/editing risk-based policies, verify the 'Security Administrator' role: Get-MgDirectoryRole | Where-Object {$_.DisplayName -eq 'Security Administrator'} | Get-MgDirectoryRoleMember. For creating/editing Conditional Access policies, verify the 'Conditional Access Administrator' role: Get-MgDirectoryRole | Where-Object {$_.DisplayName -eq 'Conditional Access Administrator'} | Get-MgDirectoryRoleMember. 2. Test password reset for a test user: Use the Microsoft Entra admin center to navigate to Users > select a test user > Reset password. Confirm the temporary password is generated. 3. Test dismissing user risk: In Identity Protection > Risky users, select a test user and choose 'Dismiss user risk'. Confirm the user's risk state changes to 'Dismissed'. 4. Verify risk-based policy creation: In Identity Protection > Risk policies, create a test policy (e.g., sign-in risk policy) and confirm it saves without errors. 5. Verify Conditional Access policy creation: In Conditional Access > Policies, create a test policy and confirm it saves without errors.

## Rollback
1. If password reset fails or causes issues, revert by resetting the user's password again to a known value using the same User Administrator role. 2. If dismissing user risk was unintended, re-investigate the user's risk level in Identity Protection > Risky users and, if needed, confirm the risk detection is still valid (no direct rollback action exists; risk state can only be dismissed or confirmed compromised). 3. If a risk-based policy causes unintended blocks, disable or delete the policy: In Identity Protection > Risk policies, select the policy and choose 'Disable' or 'Delete'. 4. If a Conditional Access policy causes access issues, disable or delete the policy: In Conditional Access > Policies, select the policy and choose 'Disable' or 'Delete'. 5. If role assignments were changed, revert to previous assignments using the Microsoft Entra admin center or PowerShell: Remove-MgDirectoryRoleMember -DirectoryRoleId <roleId> -DirectoryObjectId <userId>.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
