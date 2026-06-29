# Troubleshooting: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Troubleshooting

## Scenario / Query
How to check if the Intune and Defender for Endpoint integration is already enabled?

## Environment Context
- **Tenant Type:** Microsoft Intune admin center
- **Configuration:** Endpoint security > Defender for Endpoint

## Symptoms
- Need to verify if the services are already connected before proceeding with onboarding

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Intune admin center and select Endpoint security > Defender for Endpoint.
2. If Connection status shows Enabled, the services are already connected. Skip to Onboard devices.
3. If Connection status shows Unavailable, continue with the next step to enable the connection.

## Validation
Sign in to the Microsoft Intune admin center (https://endpoint.microsoft.com). Navigate to Endpoint security > Defender for Endpoint. Confirm that the Connection status displays 'Enabled'. If so, the integration is active.

## Rollback
If the connection status shows 'Unavailable' and you proceed to enable it, but later need to disable the integration, sign in to the Microsoft Intune admin center, go to Endpoint security > Defender for Endpoint, and set the connection to 'Off' or remove the Defender for Endpoint connector. Alternatively, use the Microsoft Graph API to delete the connector: DELETE https://graph.microsoft.com/beta/deviceManagement/intuneBrandingProfiles/{profileId} (if applicable). Refer to https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure for detailed steps.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
