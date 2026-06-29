# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to implement Conditional Access policy templates for secure foundation, remote work, and administrator protection?

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
1. Deploy these policies as a group: Require multifactor authentication for admins, Securing security info registration, Block legacy authentication, Require multifactor authentication for admins accessing Microsoft admin portals, Require multifactor authentication for all users, Require multifactor authentication for Azure management, Require compliant or Microsoft Entra hybrid joined device or multifactor authentication for all users, Require compliant device.
2. For remote workers: Securing security info registration, Block legacy authentication, Require multifactor authentication for all users, Require multifactor authentication for guest access, Require multifactor authentication for risky sign-ins (Requires Microsoft Entra ID P2), Require password change for high-risk users (Requires Microsoft Entra ID P2), Require compliant or Microsoft Entra hybrid joined device or multifactor authentication for all users, Require multifactor authentication for admins accessing Microsoft admin portals, Block access for users with insider risk (Requires Microsoft Purview).
3. For administrators: Require multifactor authentication for admins, Block legacy authentication, Require multifactor authentication for Azure management, Require compliant or Microsoft Entra hybrid joined device for administrators, Require compliant device, Require phishing-resistant multifactor authentication for administrators.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Verify that each policy listed in the remediation steps is present with status 'On' or 'Report-only' as intended. 4. For each policy, confirm the assignments (users, groups, locations, apps) and access controls match the template descriptions in the source documentation. 5. Use the 'What If' tool for a test user to simulate sign-in and confirm the expected policy is applied. 6. Run the following Microsoft Graph PowerShell command to list all policies: Get-MgIdentityConditionalAccessPolicy | Select-Object Id, DisplayName, State.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. For each policy that needs to be rolled back, select the policy and change its status to 'Off' or delete it. 4. If the policy was created as part of this implementation, delete it by selecting 'Delete' from the policy's context menu. 5. Use the following Microsoft Graph PowerShell command to disable a policy: Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId '<PolicyId>' -State 'disabled'. 6. To delete a policy: Remove-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId '<PolicyId>'. 7. Verify rollback by checking that the policies are no longer enforced using the 'What If' tool.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
