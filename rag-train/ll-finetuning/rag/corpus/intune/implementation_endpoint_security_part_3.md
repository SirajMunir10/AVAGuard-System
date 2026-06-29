# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to configure compliance and app protection settings for Microsoft Defender for Endpoint integration in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Endpoint security > Defender for Endpoint integration settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Intune admin center, go to Endpoint security > Defender for Endpoint. The Connection status should now show Enabled.
2. Enable these options under Compliance policy evaluation for your supported platforms: Connect Android devices to Defender for Endpoint: On; Connect iOS/iPadOS devices to Defender for Endpoint: On; Connect Windows devices to Defender for Endpoint: On.
3. For iOS devices, enable App Sync for iOS Devices to allow metadata sharing for threat analysis (requires MDM enrollment), and configure Send full application inventory data on personally owned iOS/iPadOS Devices to control what app data is shared with Defender for Endpoint.
4. Enable these options under App protection policy evaluation for mobile platforms: Connect Android devices to Defender for Endpoint: On; Connect iOS/iPadOS devices to Defender for Endpoint: On.

## Validation
1. Navigate to Endpoint security > Defender for Endpoint in the Intune admin center and confirm the Connection status shows 'Enabled'.
2. Under Compliance policy evaluation, verify that 'Connect Android devices to Defender for Endpoint', 'Connect iOS/iPadOS devices to Defender for Endpoint', and 'Connect Windows devices to Defender for Endpoint' are all set to 'On'.
3. For iOS, check that 'App Sync for iOS Devices' is enabled and 'Send full application inventory data on personally owned iOS/iPadOS Devices' is configured as desired.
4. Under App protection policy evaluation, confirm that 'Connect Android devices to Defender for Endpoint' and 'Connect iOS/iPadOS devices to Defender for Endpoint' are both set to 'On'.

## Rollback
1. In Endpoint security > Defender for Endpoint, set the connection to 'Disabled' if the integration causes issues.
2. Under Compliance policy evaluation, set all platform toggles ('Connect Android devices to Defender for Endpoint', 'Connect iOS/iPadOS devices to Defender for Endpoint', 'Connect Windows devices to Defender for Endpoint') to 'Off'.
3. For iOS, disable 'App Sync for iOS Devices' and reset 'Send full application inventory data on personally owned iOS/iPadOS Devices' to the default (Off).
4. Under App protection policy evaluation, set both 'Connect Android devices to Defender for Endpoint' and 'Connect iOS/iPadOS devices to Defender for Endpoint' to 'Off'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
