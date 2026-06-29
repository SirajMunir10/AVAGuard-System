# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve N/A compliance state for Hybrid Microsoft Entra devices deployed with Windows Autopilot that causes device-based Conditional Access policy issues?

## Environment Context
- **Tenant Type:** Hybrid Microsoft Entra ID with Intune
- **Configuration:** Windows Autopilot deployment of Hybrid Microsoft Entra devices

## Symptoms
- Hybrid compliance state displays as N/A when viewed from the devices list in the Azure portal until a user signs in
- Device-based Conditional Access policies that block access based on compliance may be affected

## Error Codes
N/A

## Root Causes
1. Two device IDs are initially associated with the same device - one Microsoft Entra ID and one hybrid
2. Intune only syncs with the Hybrid device ID after a successful user sign-in

## Remediation Steps
1. A user must sign in to the device to resolve the conflict
2. Alternatively, modify the device-based Conditional Access policy to not require compliance

## Validation
1. Confirm that a user has signed in to the affected device. 2. In the Azure portal, navigate to Microsoft Entra ID > Devices > All devices and locate the device. Verify that the compliance state now displays a value (e.g., 'Compliant' or 'Non-compliant') instead of 'N/A'. 3. Check that the device appears only once in the device list (no duplicate IDs). 4. Test a device-based Conditional Access policy that requires compliance to ensure it now evaluates correctly.

## Rollback
1. If the compliance state remains 'N/A' after user sign-in, verify that the device is properly enrolled in Intune and that the Intune connector for Active Directory is healthy. 2. As a temporary workaround, modify the device-based Conditional Access policy to not require device compliance (e.g., set 'Grant' > 'Require device to be marked as compliant' to 'No'). 3. If the issue persists, consider re-registering the device with Windows Autopilot by removing and re-adding its hardware hash, then redeploying.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
