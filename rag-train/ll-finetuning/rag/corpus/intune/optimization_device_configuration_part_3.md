# Optimization: Device Configuration

**Domain:** Intune
**Subdomain:** Device Configuration
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Intune device compliance by reducing the number of devices that repeatedly fall out of compliance due to stale or missing configuration profiles?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft Intune standalone)
- **Configuration:** Devices enrolled via MDM with compliance policies and configuration profiles assigned to Azure AD groups

## Symptoms
- Devices show 'Not compliant' status in Microsoft Intune admin center for no apparent reason
- Compliance policy evaluation logs show frequent re-evaluation cycles for the same device
- Help desk receives recurring tickets about devices losing compliance after a configuration profile update

## Error Codes
N/A

## Root Causes
1. Configuration profiles are not assigned to the same Azure AD groups as compliance policies, causing evaluation mismatches
2. Devices are not checking in regularly; the default check-in interval (every 8 hours) may be too long for some scenarios
3. Stale device records or orphaned enrollment states are not being cleaned up

## Remediation Steps
1. Ensure that compliance policies and the configuration profiles they depend on are assigned to the same Azure AD groups to avoid evaluation conflicts (Microsoft Learn: 'Create a compliance policy in Microsoft Intune')
2. Use the 'Check compliance' action in the Intune admin center to manually trigger a compliance evaluation on a device and verify the result
3. Review the 'Device compliance' report in Intune to identify devices that are frequently non-compliant and investigate their configuration profile assignments
4. Enable 'Device compliance: Mark devices with no compliance policy assigned as' setting to 'Compliant' or 'Not compliant' based on your organizational needs (Microsoft Learn: 'Compliance policy settings in Microsoft Intune')
5. Remove stale device records using the 'Delete' action in Intune admin center or via the Graph API (Microsoft Learn: 'Remove devices from Microsoft Intune')

## Validation
After applying the remediation steps, verify that devices that were repeatedly non-compliant now show a consistent 'Compliant' status and that the compliance evaluation logs no longer show repeated re-evaluation cycles for the same device.

## Rollback
If the changes cause unintended compliance failures, revert the assignment of compliance policies and configuration profiles to the original Azure AD groups. If the 'Mark devices with no compliance policy assigned as' setting was changed, set it back to the previous value.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/create-compliance-policy>
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-settings>
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/device-management#remove-devices>
