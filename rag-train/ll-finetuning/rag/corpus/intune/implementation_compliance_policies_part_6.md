# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to configure password requirements in a Windows compliance policy in Intune?

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
1. Set 'Require a password to unlock mobile devices' to 'Require' to enforce password entry for device access.
2. Set 'Simple passwords' to 'Block' to prevent simple passwords like 1234 or 1111.
3. Choose 'Password type' as 'Device default', 'Numeric', or 'Alphanumeric'.
4. If 'Alphanumeric' is selected, configure 'Password complexity' with options: 'Require digits and lowercase letters', 'Require digits, lowercase letters, and uppercase letters', or 'Require digits, lowercase letters, uppercase letters, and special characters'.
5. Set 'Minimum password length' to the desired number of digits or characters.

## Validation
1. In the Microsoft Intune admin center, navigate to 'Devices' > 'Compliance policies' and select the Windows compliance policy you configured. 2. Under 'Properties', review the 'Compliance settings' tab to confirm that 'Require a password to unlock mobile devices' is set to 'Require'. 3. Verify that 'Simple passwords' is set to 'Block'. 4. Confirm the 'Password type' matches your selection (e.g., 'Device default', 'Numeric', or 'Alphanumeric'). 5. If 'Alphanumeric' was selected, check that 'Password complexity' is set to one of the required options (e.g., 'Require digits and lowercase letters'). 6. Ensure 'Minimum password length' reflects the desired number of characters. 7. On a Windows device enrolled in Intune, trigger a compliance check by going to 'Settings' > 'Accounts' > 'Access work or school' > selecting the work account > 'Info' > 'Sync'. 8. After sync, verify the device shows as 'Compliant' in the Intune admin center under 'Devices' > 'All devices'.

## Rollback
1. In the Microsoft Intune admin center, navigate to 'Devices' > 'Compliance policies' and select the Windows compliance policy you modified. 2. Under 'Properties', select 'Edit' next to 'Compliance settings'. 3. Set 'Require a password to unlock mobile devices' back to 'Not configured' or the previous setting. 4. Set 'Simple passwords' back to 'Not configured' or the previous setting. 5. Revert 'Password type' to the previous selection (e.g., 'Not configured' or a different type). 6. If 'Alphanumeric' was selected, revert 'Password complexity' to the previous option or 'Not configured'. 7. Adjust 'Minimum password length' to the previous value or remove the setting. 8. Select 'Review + save' and then 'Save' to apply the changes. 9. On a Windows device enrolled in Intune, trigger a compliance check by going to 'Settings' > 'Accounts' > 'Access work or school' > selecting the work account > 'Info' > 'Sync' to ensure the device re-evaluates compliance based on the reverted policy.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
