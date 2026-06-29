# Troubleshooting: Incident Investigation

**Domain:** Sentinel
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I investigate a security incident in Microsoft Sentinel using the incident details page?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
- Need to review alerts, entities, timeline, and comments for an incident

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select View full details in the incident page and review the relevant tabs that summarize the incident information.
2. If currently using the new experience, toggle it off at the top right of the incident details page to use the legacy experience instead.
3. In the Timeline tab, review the timeline of alerts and bookmarks in the incident to reconstruct the timeline of attacker activity.
4. In the Similar incidents (Preview) tab, view a collection of up to 20 other incidents that most closely resemble the current incident to view the incident in a larger context.
5. In the Alerts tab, review the alerts included in the incident, including the analytics rules that produced them, the number of results returned per alert, and the ability to run playbooks on the alerts.
6. To drill down further into the incident, select the number of Events to open the query that generated the results and the events that triggered the alert in Log Analytics.
7. In the Bookmarks tab, view any bookmarks you or other investigators have linked to this incident.
8. In the Entities tab, view all the entities mapped as part of the alert rule definition, such as users, devices, addresses, files, or any other types.
9. In the Comments tab, add comments on the investigation and view any comments made by other analysts and investigators.

## Validation
1. Open the Microsoft Sentinel workspace in the Azure portal. 2. Navigate to 'Incidents' and select the incident you investigated. 3. Click 'View full details' and verify the following tabs are present and populated: Alerts, Bookmarks, Entities, Timeline, Comments, and Similar incidents (Preview). 4. In the Alerts tab, confirm that alerts are listed with their analytics rules and result counts. 5. Select the number of Events for an alert and verify that the Log Analytics query opens and returns results. 6. In the Timeline tab, confirm that alerts and bookmarks appear in chronological order. 7. In the Entities tab, verify that entities such as users, devices, or IP addresses are displayed. 8. In the Comments tab, confirm that any added comments are visible. 9. If the new experience was toggled off, toggle it back on and confirm the tabs remain accessible.

## Rollback
1. If the incident details page fails to load or tabs are missing, refresh the page and try again. 2. If the issue persists, toggle the new experience off/on at the top right of the incident details page to switch between experiences. 3. If the Log Analytics query fails to open, verify that the workspace has the necessary permissions and that the query is not blocked by a policy. 4. If entities are missing, check that the alert rule definitions include entity mapping and that the data connectors are sending the expected data. 5. If comments are lost, re-enter them using the Comments tab. 6. If the incident cannot be viewed, use the legacy experience by toggling off the new experience. 7. If all else fails, contact Azure support with the incident ID and workspace details.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
