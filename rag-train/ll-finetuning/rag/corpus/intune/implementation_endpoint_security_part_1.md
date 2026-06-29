# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to enable the integration between Microsoft Intune and Microsoft Defender for Endpoint when the connection status shows Unavailable?

## Environment Context
- **Tenant Type:** Microsoft Intune admin center
- **Configuration:** Endpoint security > Defender for Endpoint

## Symptoms
- Connection status shows Unavailable in the Intune admin center under Endpoint security > Defender for Endpoint

## Error Codes
N/A

## Root Causes
1. The service-to-service connection between Intune and Defender for Endpoint has not been enabled

## Remediation Steps
1. Sign in to the Microsoft Intune admin center and select Endpoint security > Defender for Endpoint.
2. If Connection status shows Unavailable, scroll to the bottom of the Defender for Endpoint page and select Open the Defender Security Center (or navigate directly to security.microsoft.com).
3. In the Microsoft Defender portal, go to System > Settings > Endpoints > General > Advanced features.
4. Locate Intune connection, toggle it to On, and then select Save preferences.
5. Return to the Intune admin center. The Connection status should now show Enabled (it can take up to 15 minutes to update).

## Validation
Return to the Intune admin center. The Connection status should now show Enabled (it can take up to 15 minutes to update). You can review and adjust monitoring settings under Endpoint security > Defender for Endpoint if needed.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
