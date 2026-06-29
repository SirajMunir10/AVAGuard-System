# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to use self-help diagnostics to troubleshoot device enrollment issues in Microsoft Intune?

## Environment Context
- **Tenant Type:** Commercial (not GCC High, DoD, or 21Vianet)
- **Configuration:** Intune enrollment configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run self-help diagnostics that cover top support topics and common tasks for which administrators request help with configuration.
2. Note: These diagnostics cannot make changes to your tenant, but they provide insight into known issues and instructions to fix them quickly.

## Validation
1. Navigate to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Go to 'Troubleshooting + support' > 'Help and support'.
3. Under 'Self-help diagnostics', select the diagnostic relevant to device enrollment (e.g., 'Device Enrollment').
4. Run the diagnostic and review the output for any identified issues or recommendations.
5. Confirm that the diagnostic completes without errors and provides actionable guidance.
6. Optionally, re-run the diagnostic after applying any recommended fixes to verify the issue is resolved.

## Rollback
1. Since self-help diagnostics are read-only and do not make changes to the tenant, no rollback is required.
2. If the diagnostic identifies misconfigurations, note the current settings before making any changes.
3. To revert any manual changes made based on diagnostic recommendations, restore the original configuration values documented in step 2.
4. If changes were made to enrollment restrictions, device type settings, or platform configurations, use the Intune admin center to revert those settings to their previous state.
5. For changes to Apple MDM push certificate or other certificates, re-upload the previous certificate or restore from backup if available.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
