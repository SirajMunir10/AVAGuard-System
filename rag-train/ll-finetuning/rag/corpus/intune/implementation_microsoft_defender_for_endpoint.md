# Implementation: Microsoft Defender for Endpoint

**Domain:** Intune
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to onboard Android devices to Microsoft Defender for Endpoint via Intune?

## Environment Context
- **Tenant Type:** Intune-managed Android devices
- **Configuration:** Microsoft Defender for Endpoint integration enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Follow the Deploy and configure Microsoft Defender for Endpoint on Android deployment guide.
2. Use Microsoft Defender for Endpoint web protection policies for additional security.
3. Confirm device registration in the Defender portal.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Microsoft Defender for Endpoint and confirm the integration status is 'Enabled'.
2. On an Android device, open the Company Portal app and verify that the Microsoft Defender for Endpoint app is listed as a required app and is installed.
3. On the Android device, open the Microsoft Defender for Endpoint app and confirm it shows 'Device is protected' and the device is registered.
4. In the Microsoft 365 Defender portal (security.microsoft.com), go to Assets > Devices and search for the Android device; verify its status shows 'Onboarded' and the sensor health is 'Active'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Microsoft Defender for Endpoint and set the integration to 'Disabled' to disconnect the tenant.
2. Remove the Microsoft Defender for Endpoint app assignment from Android device groups in Intune (Apps > All apps > Microsoft Defender for Endpoint > Properties > Assignments > Remove assignments).
3. Delete any Microsoft Defender for Endpoint web protection policies created for Android (Endpoint security > Attack surface reduction > Web protection > select policy > Delete).
4. On each Android device, uninstall the Microsoft Defender for Endpoint app via the Company Portal or device settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
