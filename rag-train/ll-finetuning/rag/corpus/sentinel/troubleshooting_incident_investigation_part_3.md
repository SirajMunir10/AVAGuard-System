# Troubleshooting: Incident Investigation

**Domain:** Sentinel
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I investigate an incident in Microsoft Sentinel?

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
1. Select Incidents.
2. Filter incidents as needed, for example by status or severity.
3. Select a specific incident to begin investigation.
4. View detailed information on the right including severity, summary of entities, raw events, incident ID, and MITRE ATT&CK tactics or techniques.
5. Select View full details in the incident page and review relevant tabs.
6. If using the new experience, toggle it off at the top right of the incident details page to use the legacy experience.
7. In the Timeline tab, review the timeline of alerts and bookmarks.
8. In the Similar incidents (Preview) tab, view up to 20 other incidents that most closely resemble the current incident.
9. In the Alerts tab, review alerts included in the incident, including analytics rules, results per alert, and ability to run playbooks.
10. To drill down further, select the number of Events to open the query in Log Analytics.
11. In the Bookmarks tab, review any bookmarks linked to the incident.
12. In the Entities tab, view all entities mapped as part of the alert rule definition.

## Validation
1. Navigate to the Microsoft Sentinel workspace in the Azure portal. 2. Select 'Incidents' from the left menu. 3. Verify that the incident list loads and filters (e.g., by status or severity) work correctly. 4. Click on a specific incident and confirm that the right pane displays severity, summary of entities, raw events, incident ID, and MITRE ATT&CK tactics/techniques. 5. Select 'View full details' and verify that the incident page opens with tabs: Timeline, Similar incidents (Preview), Alerts, Bookmarks, Entities. 6. In the Timeline tab, confirm that alerts and bookmarks are listed chronologically. 7. In the Similar incidents tab, verify that up to 20 similar incidents are shown. 8. In the Alerts tab, confirm that alerts include analytics rules, results per alert, and the option to run playbooks. 9. Click on the number of Events to confirm it opens the query in Log Analytics. 10. In the Bookmarks tab, verify that any linked bookmarks are displayed. 11. In the Entities tab, confirm that all mapped entities from the alert rule definition are visible.

## Rollback
1. If the new experience is enabled and causing issues, toggle it off at the top right of the incident details page to revert to the legacy experience. 2. If filters are not working correctly, reset filters by selecting 'Reset filters' or reloading the Incidents page. 3. If the incident details page fails to load, navigate back to the Incidents list and select the incident again. 4. If the Log Analytics query does not open, manually open Log Analytics from the Azure Sentinel menu and run the query: SecurityIncident | where IncidentId == '<incident-id>'. 5. If playbooks fail to run from the Alerts tab, run the playbook manually from the Automation blade in Microsoft Sentinel. 6. If bookmarks are not appearing, verify that bookmarks were created for the incident and refresh the page. 7. If entities are missing, check the alert rule definition and ensure entity mapping is configured correctly.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
