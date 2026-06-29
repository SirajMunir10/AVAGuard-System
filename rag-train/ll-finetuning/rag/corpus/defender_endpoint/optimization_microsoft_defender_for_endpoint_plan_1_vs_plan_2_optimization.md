# Optimization: Microsoft Defender for Endpoint Plan 1 vs Plan 2 optimization

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint Plan 1 vs Plan 2 optimization
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Microsoft Defender for Endpoint by ensuring that devices are correctly assigned to the appropriate service plan (Plan 1 or Plan 2) based on their licensing, and what PowerShell command can I use to verify the current plan assignment?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 or E5 Security licensed tenant
- **Configuration:** Devices may be licensed for Defender for Endpoint Plan 1 or Plan 2; incorrect plan assignment can lead to missing capabilities or unnecessary cost.

## Symptoms
- Some devices show 'Plan 1' in the Microsoft 365 Defender portal even though they are licensed for Plan 2.
- Advanced hunting or threat analytics features are unavailable on certain devices.
- Device inventory reports show inconsistent plan assignments.

## Error Codes
N/A

## Root Causes
1. Devices may not have the correct license assigned in the Microsoft 365 admin center.
2. The Defender for Endpoint onboarding script or group policy may not have been updated to reflect the correct service plan.
3. Licensing synchronization delay between Azure AD and the Defender portal.

## Remediation Steps
1. Verify each device's assigned license in the Microsoft 365 admin center (Billing > Licenses).
2. Use the PowerShell cmdlet `Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled, AntivirusEnabled` to check the Defender for Endpoint service status on a device. Note: This cmdlet does not directly show the plan; instead, check the 'Onboarding state' in the Microsoft 365 Defender portal under Devices.
3. If a device is licensed for Plan 2 but shows Plan 1, re-run the onboarding script for the correct plan. The onboarding script is available from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding).
4. Ensure the device is properly connected to the internet and can reach the Defender for Endpoint cloud service endpoints.
5. Allow up to 24 hours for licensing changes to propagate.

## Validation
In the Microsoft 365 Defender portal, navigate to Devices, select the device, and verify that the 'Service plan' field shows the expected plan (Plan 1 or Plan 2).

## Rollback
If a device was incorrectly assigned to Plan 2 but is only licensed for Plan 1, remove the Plan 2 license from the user or device in the Microsoft 365 admin center and assign the correct Plan 1 license. Then re-run the onboarding script for Plan 1.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/defender-endpoint-plan-1-2>
- <https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint>
