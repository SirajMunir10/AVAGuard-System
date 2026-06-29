# Implementation: Mobile Threat Defense

**Domain:** Intune
**Subdomain:** Mobile Threat Defense
**Incident Type:** Implementation

## Scenario / Query
How to configure app protection policy evaluation for Defender for Endpoint on Android and iOS/iPadOS devices?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** App protection policy evaluation settings for mobile platforms

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable these options under App protection policy evaluation for mobile platforms: Connect Android devices to Defender for Endpoint : On
2. Enable these options under App protection policy evaluation for mobile platforms: Connect iOS/iPadOS devices to Defender for Endpoint : On
3. Under Mobile Threat Defense role , you can optionally grant Defender for Endpoint enhanced security permissions on enrolled Android Enterprise corporate-owned fully managed and corporate-owned work profile devices.
4. You can also enable automatic launch of Defender for Endpoint during device setup on these devices.
5. Select Save to apply all settings.

## Validation
1. Navigate to Microsoft Intune admin center > Endpoint security > Mobile Threat Defense. 2. Verify that 'Connect Android devices to Defender for Endpoint' is set to 'On'. 3. Verify that 'Connect iOS/iPadOS devices to Defender for Endpoint' is set to 'On'. 4. If applicable, confirm that the 'Mobile Threat Defense role' for enhanced security permissions on enrolled Android Enterprise devices is configured as desired. 5. If applicable, confirm that 'Automatic launch of Defender for Endpoint during device setup' is enabled. 6. Click 'Save' and confirm no error messages appear. 7. On a test Android and iOS/iPadOS device, verify that the Defender for Endpoint app appears in the Company Portal and that app protection policies are evaluated correctly.

## Rollback
1. Navigate to Microsoft Intune admin center > Endpoint security > Mobile Threat Defense. 2. Set 'Connect Android devices to Defender for Endpoint' to 'Off'. 3. Set 'Connect iOS/iPadOS devices to Defender for Endpoint' to 'Off'. 4. If enhanced permissions were granted, remove the 'Mobile Threat Defense role' assignment for Android Enterprise devices. 5. If automatic launch was enabled, disable 'Automatic launch of Defender for Endpoint during device setup'. 6. Click 'Save' to apply the changes. 7. Verify that the settings are reverted and that no devices are affected by the previous configuration.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
