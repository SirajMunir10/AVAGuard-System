# Incident Response: Incident Response

**Domain:** Sentinel
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst in a Microsoft Sentinel environment needs to investigate a suspicious sign-in from an unfamiliar location. How can the analyst use the built-in incident investigation graph to pivot from the initial alert to related entities and expand the scope of the investigation?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Sentinel enabled
- **Configuration:** Sentinel workspace is configured with the Microsoft 365 connector and Azure Active Directory connector enabled. The analyst has the 'Microsoft Sentinel Responder' role.

## Symptoms
- An incident is generated for a sign-in from an unfamiliar location
- The incident contains a single alert with a user account entity

## Error Codes
N/A

## Root Causes
1. The analyst is not familiar with the investigation graph feature in Microsoft Sentinel

## Remediation Steps
1. Open the incident in Microsoft Sentinel
2. Click the 'Investigate' button to launch the investigation graph
3. Select the user entity node and use the 'Explore' option to add related entities such as IP addresses, devices, and applications
4. Use the timeline slider to focus on events around the time of the suspicious sign-in
5. Add any new entities found to the incident as evidence

## Validation
Verify that the investigation graph displays a connected map of entities and that new entities can be added to the incident as evidence.

## Rollback
Remove any entities added to the incident that are not relevant to the investigation.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
