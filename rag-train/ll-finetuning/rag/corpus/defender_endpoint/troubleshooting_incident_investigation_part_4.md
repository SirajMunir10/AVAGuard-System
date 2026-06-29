# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How to use the attack story in Microsoft Defender XDR to review, investigate, and remediate attacks while maintaining context?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Incident investigation interface

## Symptoms
- Need to review the full story of an attack without losing context
- Need to take remediation actions such as deleting a file or isolating a device while viewing entity details

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the attack story within the incident page
2. Review the alert page sections: Alert story (including What happened, Actions taken, Related events) and Alert properties in the right pane (state, details, description, and others)
3. Use the incident graph to view the full scope of the attack, how it spread through the network over time, where it started, and how far the attacker went
4. From the graph, play the alerts and nodes as they occurred over time to understand the chronology of the attack
5. Open an entity pane to review entity details and act on remediation actions such as deleting a file or isolating a device
6. Highlight alerts based on the entity to which they are related
7. Hunt for entity information of a device, file, IP address, URL, user, email, mailbox, or cloud resource

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents and select the relevant incident.
3. Confirm the 'Attack story' tab is visible and displays the alert story sections: 'What happened', 'Actions taken', and 'Related events'.
4. Verify the incident graph shows the full scope of the attack, including nodes for devices, files, IPs, URLs, users, emails, mailboxes, or cloud resources.
5. Use the playback controls on the graph to step through the attack chronology and confirm alerts and nodes appear in correct sequence.
6. Click on an entity (e.g., a device or file) in the graph and verify the entity pane opens with details and remediation actions (e.g., 'Delete file' or 'Isolate device').
7. Confirm that selecting an alert in the graph highlights related entities and that the right pane shows alert properties (state, details, description).
8. Use the 'Hunt' option from an entity pane to launch advanced hunting and verify it returns relevant entity information.

## Rollback
1. If the attack story does not load, refresh the incident page or clear browser cache and retry.
2. If the incident graph fails to display, navigate back to the Incidents list and re-select the incident.
3. If entity details are missing, verify the entity is still active in the tenant and that permissions are not restricted.
4. If remediation actions (e.g., delete file, isolate device) fail, check the action status in the Action center (https://security.microsoft.com/action-center) and retry the action from the entity pane.
5. If playback controls are unresponsive, reload the incident page and ensure no browser extensions interfere.
6. If highlighting alerts by entity does not work, manually filter alerts using the 'Related entities' column in the Alerts tab.
7. If hunting from an entity pane fails, manually launch advanced hunting from the Hunting menu and construct a query using the entity's identifier.
8. For persistent issues, refer to the official documentation at https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
