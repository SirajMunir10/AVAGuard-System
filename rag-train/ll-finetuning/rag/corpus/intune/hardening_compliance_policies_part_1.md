# Hardening: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Hardening

## Scenario / Query
How to harden password policies for Windows devices using Intune compliance policies?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** Compliance policy for Windows devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set 'Require a password to unlock mobile devices' to 'Require'.
2. Set 'Simple passwords' to 'Block'.
3. Set 'Password type' to 'Alphanumeric'.
4. Configure 'Password complexity' to 'Require digits, lowercase letters, uppercase letters, and special characters'.
5. Set 'Minimum password length' to a value that meets organizational security requirements.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy that was modified. Under 'Properties', review the 'Compliance settings' to confirm: 'Require a password to unlock mobile devices' is set to 'Require', 'Simple passwords' is set to 'Block', 'Password type' is set to 'Alphanumeric', 'Password complexity' is set to 'Require digits, lowercase letters, uppercase letters, and special characters', and 'Minimum password length' is set to the desired value. 2. On a test Windows device that is targeted by the policy, run 'dsregcmd /status' to verify the device is Azure AD joined and enrolled in Intune. 3. On the same device, trigger a compliance check by running 'SyncML' or using the 'Sync' button in Settings > Accounts > Access work or school > Info. 4. In the Intune admin center, go to Devices > All devices, select the test device, and under 'Device compliance' confirm the status shows 'Compliant' and the policy settings are applied. 5. Attempt to change the local password on the device to a simple or short password to verify the policy blocks it.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy that was modified. 2. Under 'Properties', select 'Edit' for 'Compliance settings'. 3. Change 'Require a password to unlock mobile devices' to 'Not configured'. 4. Change 'Simple passwords' to 'Allow'. 5. Change 'Password type' to 'Not configured' or a less restrictive option. 6. Change 'Password complexity' to 'Not configured' or a less restrictive option. 7. Change 'Minimum password length' to 'Not configured' or a lower value. 8. Select 'Review + save' and confirm the changes. 9. On a test device, trigger a compliance check to ensure the previous settings are no longer enforced.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
