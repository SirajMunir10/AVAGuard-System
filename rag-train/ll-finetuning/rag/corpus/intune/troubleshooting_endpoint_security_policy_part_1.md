# Troubleshooting: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve configuration conflicts when implementing endpoint security policies alongside other Intune policy types?

## Environment Context
- **Tenant Type:** Intune-managed tenant
- **Configuration:** Endpoint security policies, security baselines, device configuration policies

## Symptoms
- Affected settings might fail to apply properly

## Error Codes
N/A

## Root Causes
1. Conflicts occur when a device receives different configurations for the same setting from multiple policies
2. Security baselines can set non-default values for settings to comply with recommended configurations, while endpoint security and device configuration policies typically default to Not configured
3. Device configuration policies managing the same settings as endpoint security policies
4. Multiple endpoint security policies setting different values for the same setting

## Remediation Steps
1. Plan your policy architecture
2. Use the linked guidance to identify and resolve conflicts

## Validation
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'All policies' and verify that no two policies assign different values for the same setting to the same device or user group. 2. Use the 'Troubleshooting + support' blade to select a test device and review the 'Policy' tab to confirm the effective configuration for each setting matches the intended value. 3. Run the following PowerShell cmdlet as a global administrator to retrieve policy assignments and check for conflicts: Get-MgDeviceManagementConfigurationPolicyAssignment -DeviceManagementConfigurationPolicyId <policyId> | Select-Object -ExpandProperty Target. 4. For a device, run the command: Get-MgDeviceManagementManagedDevice -ManagedDeviceId <deviceId> | Select-Object -ExpandProperty ConfigurationManagerClientEnabledFeatures to ensure no conflicting policies are applied.

## Rollback
1. Identify the conflicting policy by reviewing the 'Policy conflicts' report in the Intune admin center under 'Troubleshooting + support' > 'Policy conflicts'. 2. Remove the conflicting policy assignment by navigating to the policy, selecting 'Assignments', and deleting the assignment for the affected group. 3. Alternatively, modify the conflicting policy to set the conflicting setting to 'Not configured' or to align with the desired value. 4. If a security baseline is causing the conflict, navigate to 'Endpoint security' > 'Security baselines', select the baseline, and under 'Settings', change the conflicting setting to 'Not configured' or to a value that matches the endpoint security policy. 5. Force a sync on the affected device by going to 'Devices' > 'All devices', selecting the device, and clicking 'Sync'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
