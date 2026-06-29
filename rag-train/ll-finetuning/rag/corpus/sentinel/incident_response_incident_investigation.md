# Incident Response: Incident Investigation

**Domain:** Sentinel
**Subdomain:** Incident Investigation
**Incident Type:** Incident Response

## Scenario / Query
How do I view the investigation map and add comments during an incident investigation in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Investigate to view the investigation map.
2. In the Comments tab, add your comments on the investigation and view any comments made by other analysts and investigators.

## Validation
1. Open the Microsoft Sentinel workspace in the Azure portal.
2. Navigate to Threat Management > Incidents.
3. Select an incident to open its details.
4. Click the 'Investigate' button and confirm the investigation map loads with entities and connections.
5. Switch to the 'Comments' tab, type a test comment, and click 'Add comment'.
6. Verify the comment appears in the comment list with timestamp and author.
7. Refresh the page and confirm the comment persists.

## Rollback
1. Open the same incident in Microsoft Sentinel.
2. Go to the 'Comments' tab.
3. Locate the test comment added during validation.
4. Click the delete icon (trash can) next to the comment to remove it.
5. Confirm the comment is removed from the list.
6. If the investigation map shows unexpected changes, close the incident without saving any modifications (the map is read-only and cannot be rolled back).

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
