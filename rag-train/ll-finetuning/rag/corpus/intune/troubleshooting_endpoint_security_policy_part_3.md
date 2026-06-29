# Troubleshooting: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and resolve policy conflicts in Intune endpoint security policies?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security policies, device configuration policies, security baselines

## Symptoms
- Policy deployment reports show error or conflict status flags
- Settings fail to apply on devices

## Error Codes
N/A

## Root Causes
1. Multiple policies configure the same setting with different values
2. Setting overlap between endpoint security policies, device configuration policies, and security baselines
3. All policy types have equal precedence when Intune evaluates device configuration

## Remediation Steps
1. Monitor policy deployment reports for error or conflict status flags
2. Check which policy types target the same setting across multiple policies
3. Use device-level reporting to identify which policies are applying
4. Determine if security baselines are setting non-default values that conflict with other policies
5. Use policy-specific guidance to resolve conflicts systematically

## Validation
1. Open Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to 'Endpoint security' > 'All policies' and review the 'Deployment status' column for any policy showing 'Error' or 'Conflict'.
3. Select a policy with a conflict status, then click 'Device status' to view per-device details. Identify devices with 'Conflict' status.
4. On a conflicting device, go to 'Devices' > 'All devices', select the device, then click 'Device configuration' > 'Policies' to list all policies assigned to that device.
5. Compare the settings in each policy (Endpoint security, Device configuration, Security baseline) that target the same configuration. Use the 'Settings catalog' view to see overlapping settings.
6. Verify that after remediation, the device status changes from 'Conflict' to 'Succeeded' and that the intended setting value is applied (e.g., via 'Device status' > 'Settings' view).

## Rollback
1. If a policy was removed to resolve conflict, re-create the original policy with its previous settings and assignments. Use the 'Policies' > 'Create policy' wizard, selecting the same platform and profile type.
2. If a policy was modified (e.g., a setting was changed to a non-conflicting value), revert that setting to its original value by editing the policy in 'Endpoint security' > 'All policies' > select policy > 'Properties' > 'Configuration settings' > 'Edit'.
3. If a security baseline was adjusted, restore the baseline to its previous configuration by editing the baseline in 'Endpoint security' > 'Security baselines' > select baseline > 'Properties' > 'Configuration settings' > 'Edit' and resetting the changed setting.
4. After rollback, monitor the 'Deployment status' for the affected policies and devices to confirm that the conflict status returns (if intended) or that no new issues arise.
5. Use device-level reporting to verify that the original conflicting state is restored.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-policies-in-microsoft-intune>
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines-monitor>
