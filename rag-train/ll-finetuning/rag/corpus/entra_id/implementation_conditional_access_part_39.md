# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure Conditional Access policies for mobile apps and desktop clients, including the requirement to enable the Microsoft Enterprise SSO plug-in for Apple devices?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Conditional Access policy targeting Mobile apps and desktop clients; Apple devices using device-based authentication

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable the Microsoft Enterprise SSO plug-in for Apple devices for applications that do not use the Microsoft Authentication Library (MSAL), including Safari.
2. Ensure the Enterprise SSO plug-in is enabled so that applications can participate in device-based authentication required by Conditional Access policies, such as 'Require device to be marked as compliant' and 'Filter for devices condition'.

## Validation
1. Verify that the Microsoft Enterprise SSO plug-in is enabled on Apple devices by checking the device configuration profile in Microsoft Intune or your MDM console. 2. On an Apple device, navigate to Settings > General > VPN & Device Management and confirm the plug-in is listed as active. 3. Test a non-MSAL application (e.g., Safari) by accessing a resource protected by a Conditional Access policy that requires device compliance; confirm the user is prompted for device-based authentication and access is granted. 4. Run the following PowerShell command to check the Conditional Access policy configuration: Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.Conditions.Applications.IncludeApplications -contains 'All'} | Format-List DisplayName, Conditions, GrantControls. 5. Review the policy's grant controls to ensure 'Require device to be marked as compliant' is enabled.

## Rollback
1. Disable the Microsoft Enterprise SSO plug-in by removing or modifying the device configuration profile in Microsoft Intune or your MDM console. 2. On affected Apple devices, remove the plug-in profile manually via Settings > General > VPN & Device Management. 3. If the Conditional Access policy was modified, revert the policy to its previous state using the Microsoft Entra admin center or PowerShell: Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId <PolicyId> -GrantControls @{BuiltInControls = @('RequireDeviceToBeMarkedCompliant')}. 4. Verify that non-MSAL applications no longer participate in device-based authentication and that access is denied as expected for non-compliant devices.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
