# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to onboard macOS devices to Microsoft Defender for Endpoint using Intune?

## Environment Context
- **Tenant Type:** Intune-managed macOS devices
- **Configuration:** Microsoft Defender for Endpoint for macOS

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Deploy the app: Follow the Microsoft Defender for Endpoint for macOS deployment guide.
2. Configure settings: Use Intune app configuration policies.
3. Verify onboarding: Check device appears in the Defender portal.

## Validation
1. In the Microsoft 365 Defender portal (https://security.microsoft.com), navigate to 'Inventory' > 'Devices' and filter by OS = macOS. Confirm the target device appears in the list with a status of 'Active' or 'Onboarded'.
2. On the macOS device, open Terminal and run: 'mdatp health --field real_time_protection_enabled'. Verify the output is 'true'.
3. In Intune, go to 'Apps' > 'All apps' and confirm the Microsoft Defender for Endpoint app shows a status of 'Installed' for the target device.
4. In Intune, go to 'Devices' > 'macOS' > select the device > 'Managed apps' and verify the Defender app is listed with a status of 'Installed'.

## Rollback
1. In Intune, go to 'Apps' > 'All apps', select the Microsoft Defender for Endpoint app, and click 'Uninstall' for the affected device group.
2. In Intune, go to 'Devices' > 'macOS' > 'Configuration profiles' and delete any app configuration policy that was applied for Defender.
3. On the macOS device, open Terminal and run: 'sudo mdatp uninstall' to remove the Defender agent.
4. In the Microsoft 365 Defender portal, confirm the device no longer appears under 'Inventory' > 'Devices'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
