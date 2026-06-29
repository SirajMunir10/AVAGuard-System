# Implementation: Jamf Pro integration

**Domain:** Intune
**Subdomain:** Jamf Pro integration
**Incident Type:** Implementation

## Scenario / Query
How to migrate Jamf macOS devices from Conditional Access to Device Compliance?

## Environment Context
- **Tenant Type:** Intune tenant with Jamf Pro Conditional Access integration for macOS
- **Configuration:** Jamf Pro Conditional Access feature for macOS devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Follow Jamf's documented guidelines to migrate your devices from macOS Conditional Access to macOS Device Compliance.
2. If you have questions or need help, contact Jamf Customer Success.

## Validation
1. In the Microsoft Intune admin center, navigate to 'Endpoint Security' > 'Device Compliance' and confirm that the macOS compliance policies are assigned to the appropriate groups.
2. In Jamf Pro, verify that the macOS devices are now listed under the 'Device Compliance' integration (not the 'Conditional Access' integration) by checking the Jamf Pro console under 'Settings' > 'Global Management' > 'Microsoft Intune Integration'.
3. On a test macOS device, run 'sudo jamf recon' to force a check-in, then in Intune verify the device shows as 'Compliant' under 'Devices' > 'macOS' > select the device > 'Device compliance'.
4. Confirm that Conditional Access policies referencing 'Require device to be marked as compliant' are now evaluating these devices correctly by signing into a Microsoft 365 resource (e.g., portal.office.com) and verifying access is granted.

## Rollback
1. In Jamf Pro, under 'Settings' > 'Global Management' > 'Microsoft Intune Integration', switch the integration back to 'Conditional Access' mode.
2. In the Microsoft Intune admin center, remove the macOS Device Compliance policies that were assigned during migration.
3. Re-enable any Conditional Access policies that were previously disabled or modified to support the migration.
4. On affected macOS devices, run 'sudo jamf recon' to re-register with the Conditional Access integration.
5. Verify that devices appear as 'Compliant' under the Conditional Access integration in Intune and that Conditional Access policies enforce access correctly.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf#transitioning-jamf-macos-devices-from-conditional-access-to-device-compliance>
