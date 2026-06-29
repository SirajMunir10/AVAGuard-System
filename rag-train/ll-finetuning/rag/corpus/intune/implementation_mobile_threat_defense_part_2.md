# Implementation: Mobile Threat Defense

**Domain:** Intune
**Subdomain:** Mobile Threat Defense
**Incident Type:** Implementation

## Scenario / Query
How do I configure integration settings between Microsoft Intune and Microsoft Defender for Endpoint for compliance and app protection policy evaluation?

## Environment Context
- **Tenant Type:** Microsoft Intune tenant with Microsoft Defender for Endpoint
- **Configuration:** Endpoint Security Manager role or equivalent permissions for Mobile Threat Defense settings; custom roles require Read and Modify rights for the Mobile Threat Defense permission

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create the service connection between Intune and Defender for Endpoint.
2. Configure which platforms connect to Defender for Endpoint for compliance and app protection policy evaluation.

## Validation
1. Sign in to the Microsoft Intune admin center (https://endpoint.microsoft.com).
2. Navigate to Tenant administration > Connectors and tokens > Microsoft Defender for Endpoint (Cross-tenant).
3. Verify that the status shows 'Enabled' and the connection state is 'Active'.
4. Under 'Microsoft Defender for Endpoint connector', confirm that 'Allow Microsoft Defender for Endpoint to enforce app protection policies' is set to 'On'.
5. Go to Endpoint security > Mobile threat defense > Microsoft Defender for Endpoint.
6. Confirm that the platforms (Android, iOS/iPadOS, Windows) you intend to use are toggled 'On' for both 'Connect Android devices to Microsoft Defender for Endpoint' and 'Connect iOS/iPadOS devices to Microsoft Defender for Endpoint' as applicable.
7. Verify that the 'Connection status' for each platform shows 'Active' and 'Last synchronized' time is recent.
8. Create a test compliance policy that uses 'Require the device to be at or under the Device Threat Level' set to 'Low' and assign it to a test user.
9. On a test device, verify that the device is marked as compliant in the Intune admin center and that the Defender for Endpoint threat level is evaluated.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://endpoint.microsoft.com).
2. Navigate to Tenant administration > Connectors and tokens > Microsoft Defender for Endpoint (Cross-tenant).
3. Set 'Allow Microsoft Defender for Endpoint to enforce app protection policies' to 'Off'.
4. Go to Endpoint security > Mobile threat defense > Microsoft Defender for Endpoint.
5. For each platform (Android, iOS/iPadOS, Windows) that was enabled, set the toggle to 'Off' for 'Connect Android devices to Microsoft Defender for Endpoint' and 'Connect iOS/iPadOS devices to Microsoft Defender for Endpoint'.
6. Navigate to Tenant administration > Connectors and tokens > Microsoft Defender for Endpoint (Cross-tenant) and click 'Disconnect' to remove the service connection entirely.
7. Confirm the disconnection by clicking 'Yes' in the confirmation dialog.
8. Verify that the connection status shows 'Not connected' and that no platforms are listed under the connector.
9. Remove any test compliance policies that were created for validation.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
