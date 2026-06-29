# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure a Conditional Access policy that requires a password change when user risk is detected?

## Environment Context
- **Tenant Type:** Entra ID (Azure AD)
- **Configuration:** User risk policy with password change control

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure all users register for multifactor authentication before triggering the user risk policy.
2. Configure the policy to be assigned to 'All resources' to prevent an attacker from using a different app to change the user's password and resetting their account risk.
3. Use the password change control only with the user and group assignment condition, cloud app assignment condition (which must be set to 'all'), and user risk conditions.
4. Do not use 'Require password change' with other controls, such as requiring a compliant device.

## Validation
1. Confirm that all users have registered for multifactor authentication by running: Get-MsolUser -All | Where-Object {$_.StrongAuthenticationMethods -eq $null}. If any users are returned, they must register MFA before the policy can be safely applied. 2. Verify the Conditional Access policy configuration using: Get-AzureADMSConditionalAccessPolicy | Where-Object {$_.GrantControls.BuiltInControls -contains 'passwordChange'}. Ensure the policy is assigned to 'All resources' (i.e., the cloud apps condition includes 'All cloud apps'). 3. Check that the policy includes only the 'Require password change' grant control and no other controls (e.g., require compliant device) by reviewing the GrantControls property. 4. Validate that the policy conditions include user risk (e.g., 'User risk level' set to 'High' or 'Medium') and that the assignment includes the intended users/groups.

## Rollback
1. Disable the user risk Conditional Access policy by running: Set-AzureADMSConditionalAccessPolicy -PolicyId <PolicyId> -State 'disabled'. 2. If the policy was already enforced and caused issues, remove the policy entirely with: Remove-AzureADMSConditionalAccessPolicy -PolicyId <PolicyId>. 3. If users are locked out due to password change requirements, temporarily exclude affected users from the policy by adding them to the 'Exclude users' list in the policy assignments. 4. Reset any user accounts that were incorrectly flagged as risky using: Set-AzureADUserRiskLevel -UserPrincipalName <UPN> -RiskLevel 'none'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
