# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How does automatic attack disruption isolate a compromised device in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Automatic attack disruption enabled; device onboarded and managed by Defender for Endpoint

## Symptoms
- Device suspected to be compromised
- Automatic isolation triggered as part of attack disruption

## Error Codes
N/A

## Root Causes
1. Device suspected to be compromised, triggering automatic attack disruption

## Remediation Steps
1. The compromised device is disconnected from the network automatically
2. The device retains connectivity to the Microsoft Defender for Endpoint service for continued monitoring

## Validation
1. In Microsoft Defender for Endpoint portal (https://security.microsoft.com), navigate to 'Incidents & alerts' > 'Incidents'. Select the incident that triggered automatic attack disruption. Verify the 'Device isolation' status shows 'Isolated' for the affected device. 2. From the device timeline, confirm the 'Device isolation' action was initiated automatically under 'Attack disruption'. 3. Check that the device still reports to Defender for Endpoint by verifying its 'Last seen' timestamp is recent (within the last hour) and its 'Health state' is 'Active' or 'Passive'. 4. Optionally, run a test connectivity check from the device to the Defender for Endpoint cloud service (e.g., using 'Test-NetConnection' to the appropriate endpoint URLs) to ensure only management traffic is allowed.

## Rollback
1. In Microsoft Defender for Endpoint portal, go to 'Device inventory' and select the isolated device. 2. Click 'Release from isolation' to restore network connectivity. 3. Confirm the action by reviewing the device timeline for a 'Release from isolation' event. 4. Verify the device can access network resources and communicate with Defender for Endpoint by checking its 'Last seen' timestamp updates and health state returns to 'Active'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
