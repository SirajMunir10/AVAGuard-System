# Implementation: Mobile Threat Defense

**Domain:** Intune
**Subdomain:** Mobile Threat Defense
**Incident Type:** Implementation

## Scenario / Query
How to configure Mobile Threat Defense role for Android Enterprise devices?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Mobile Threat Defense role settings for Android Enterprise corporate-owned fully managed and corporate-owned work profile devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Under Mobile Threat Defense role , you can optionally grant Defender for Endpoint enhanced security permissions on enrolled Android Enterprise corporate-owned fully managed and corporate-owned work profile devices.
2. You can also enable automatic launch of Defender for Endpoint during device setup on these devices.
3. Select Save to apply all settings.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Mobile Threat Defense. 2. Under the Mobile Threat Defense role section, confirm that Defender for Endpoint is granted enhanced security permissions for Android Enterprise corporate-owned fully managed and corporate-owned work profile devices. 3. Verify that the toggle for automatic launch of Defender for Endpoint during device setup is enabled. 4. Select Save to apply settings. 5. On a test Android Enterprise device, enroll and confirm that Defender for Endpoint launches automatically during setup and that enhanced security permissions are active.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Mobile Threat Defense. 2. Under the Mobile Threat Defense role section, disable the enhanced security permissions for Defender for Endpoint on Android Enterprise corporate-owned fully managed and corporate-owned work profile devices. 3. Disable the automatic launch of Defender for Endpoint during device setup. 4. Select Save to apply the rollback settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
