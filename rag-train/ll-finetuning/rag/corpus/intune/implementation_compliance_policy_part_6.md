# Implementation: Compliance Policy

**Domain:** Intune
**Subdomain:** Compliance Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure compliance policies for Surface Hub devices running Windows Team OS in Intune?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Surface Hub devices must be Microsoft Entra joined for compliance and Conditional Access to work. Windows automatic enrollment in Intune is recommended.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Windows automatic enrollment in Intune (requires Microsoft Entra ID).
2. Target the Surface Hub devices as device groups.
3. For Surface Hubs running Windows Team OS, set the following two settings to their default of Not configured: In the category Password, set Require a password to unlock mobile devices to the default of Not configured. In the category Microsoft Defender for Endpoint, set Require the device to be at or under the machine risk score to the default of Not configured.

## Validation
1. Verify that Windows automatic enrollment is enabled in Microsoft Entra ID: Navigate to Microsoft Entra admin center > Identity > Devices > Device settings. Confirm 'Users may join devices to Azure AD' is set to 'All' or 'Selected' and that 'Windows 10 or later devices' enrollment is configured. 2. Confirm Surface Hub devices are Microsoft Entra joined: In Microsoft Entra admin center > Identity > Devices > All devices, filter by OS 'Windows Team OS' and verify each device shows 'Azure AD joined' as the join type. 3. Validate the compliance policy targeting: In Intune admin center > Devices > Compliance policies, select the policy for Surface Hub. Under 'Assignments', confirm the device group containing Surface Hubs is listed. 4. Check policy settings: In the same policy, under 'Settings', expand 'Password' and confirm 'Require a password to unlock mobile devices' is set to 'Not configured'. Expand 'Microsoft Defender for Endpoint' and confirm 'Require the device to be at or under the machine risk score' is set to 'Not configured'. 5. Verify compliance status: In Intune admin center > Devices > All devices, filter by OS 'Windows Team OS'. Select a Surface Hub device and check its 'Compliance' status. It should show 'Compliant' if the policy is applied correctly.

## Rollback
1. If automatic enrollment causes issues, disable it: In Microsoft Entra admin center > Identity > Devices > Device settings, set 'Users may join devices to Azure AD' to 'None' and disable Windows automatic enrollment. 2. If the compliance policy is misapplied, remove the assignment: In Intune admin center > Devices > Compliance policies, select the policy. Under 'Assignments', remove the device group containing Surface Hubs. 3. If the policy settings need to be reverted, change them back to their original values: In the same policy, set 'Require a password to unlock mobile devices' to 'Require' (or the previous setting) and set 'Require the device to be at or under the machine risk score' to a specific risk level (e.g., 'Medium'). 4. If the device group is incorrect, delete or modify the group: In Microsoft Entra admin center > Groups, locate the device group used for targeting. Remove Surface Hub devices from the group or delete the group entirely.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
