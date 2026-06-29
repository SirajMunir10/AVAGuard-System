# Migration: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Migration

## Scenario / Query
How to migrate Conditional Access policies from 'Require approved client app' to 'Require application protection policy' before the March 2026 retirement?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Conditional Access policies using 'Require approved client app' grant
- **Configuration:** Conditional Access policies using only the 'Require Approved Client App' grant

## Symptoms
- Conditional Access policies using 'Require approved client app' grant will stop working after March 2026
- New policies cannot use 'Require approved client app' grant

## Error Codes
N/A

## Root Causes
1. The 'Require approved client app' grant is retiring in early March 2026

## Remediation Steps
1. Transition all current Conditional Access policies that use only the 'Require Approved Client App' grant to 'Require Approved Client App or Application Protection Policy' by March 2026
2. For any new Conditional Access policy, only apply the 'Require application protection policy' grant

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. For each policy that previously used only 'Require approved client app', select the policy and verify under Access controls > Grant that the setting is now 'Require approved client app or app protection policy' (or 'Require app protection policy' for new policies). 4. Use Microsoft Graph PowerShell: `Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.GrantControls.BuiltInControls -contains 'approvedApplication'}` to confirm no policy uses only 'approvedApplication'. 5. Test the policy by signing in with a user in scope using a supported app (e.g., Outlook mobile) and confirm access is granted only when the app has an app protection policy applied.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. For each policy that was changed, select the policy and under Access controls > Grant, change the setting back to 'Require approved client app' (only). 4. If using Microsoft Graph PowerShell, run: `Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId <policy-id> -GrantControls @{BuiltInControls=@('approvedApplication')}`. 5. Verify the policy is restored by checking the grant controls in the portal or via `Get-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId <policy-id> | Select-Object -ExpandProperty GrantControls`.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#migrate-approved-client-app-to-application-protection-policy>
