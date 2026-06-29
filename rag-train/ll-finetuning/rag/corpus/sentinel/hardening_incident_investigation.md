# Hardening: Incident Investigation

**Domain:** Sentinel
**Subdomain:** Incident Investigation
**Incident Type:** Hardening

## Scenario / Query
How do I monitor detected threats by investigating incidents in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel in the Azure portal, legacy incident investigation experience

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Let Microsoft Sentinel know what kinds of threats you're looking for and how to find them
2. Monitor detected threats by investigating incidents

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel and select the relevant workspace. 2. Under 'Threat management', click 'Incidents'. 3. Verify that the incident list displays and that you can open an incident to view its details, timeline, and entities. 4. Confirm that the legacy investigation graph (if enabled) loads correctly for an incident. 5. Check that alerts and entities are linked and that you can perform actions like assigning or closing an incident.

## Rollback
1. If the legacy investigation experience is not working, ensure the feature is enabled in the workspace settings under 'Settings' > 'Incident investigation'. 2. If incidents are not appearing, verify that the data connector for the relevant source (e.g., Microsoft 365 Defender) is connected and ingesting data. 3. If the investigation graph fails, try refreshing the page or clearing the browser cache. 4. As a last resort, disable and re-enable the legacy investigation experience in the workspace settings.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
