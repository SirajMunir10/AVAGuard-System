# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to avoid blocking all users when configuring Conditional Access policies with 'all users' and 'all resources' assignments?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policy assignments

## Symptoms
- Entire organization is blocked from accessing resources
- Admins cannot access Intune or Azure portals
- Users without enrolled devices are blocked
- Users without Microsoft Entra hybrid joined devices are blocked
- Users without Intune app protection policy are blocked

## Error Codes
N/A

## Root Causes
1. Using 'all users' and 'all resources' assignments with 'Block access' control
2. Using 'Require device to be marked as compliant' for all users and all resources without device enrollment
3. Using 'Require Hybrid Microsoft Entra domain joined device' for all users and all resources without hybrid joined devices
4. Using 'Require app protection policy' for all users and all resources without Intune policy
5. Using 'all users', 'all resources', and 'all device platforms' with 'Block access' control

## Remediation Steps
1. Avoid using 'all users' and 'all resources' assignments with 'Block access' control
2. Avoid using 'Require device to be marked as compliant' for all users and all resources
3. Avoid using 'Require Hybrid Microsoft Entra domain joined device' for all users and all resources
4. Avoid using 'Require app protection policy' for all users and all resources
5. Avoid using 'all users', 'all resources', and 'all device platforms' with 'Block access' control
6. Carefully review each configuration policy before releasing it to avoid unwanted results

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Identify any policy with assignments set to 'All users' and 'All resources' and a control of 'Block access'. 4. Verify that no such policy is in 'Report-only' mode or enabled. 5. Check that policies requiring device compliance, hybrid join, or app protection are not applied to 'All users' and 'All resources' without appropriate exclusions. 6. Use the 'What If' tool for a test user to confirm that no unintended block or device requirement is triggered. 7. Confirm that at least one break-glass account is excluded from all Conditional Access policies.

## Rollback
1. Sign in to the Microsoft Entra admin center using a break-glass account that is excluded from all Conditional Access policies. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the problematic policy (e.g., one with 'All users', 'All resources', and 'Block access'). 4. Disable the policy by setting 'Enable policy' to 'Off'. 5. If the policy is in 'Report-only' mode, switch it to 'Off' to prevent enforcement. 6. If the policy cannot be accessed due to being locked out, use Microsoft Graph API or PowerShell with a break-glass account to disable the policy: Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId <policy-id> -State 'disabled'. 7. After disabling, verify access is restored for all users.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
