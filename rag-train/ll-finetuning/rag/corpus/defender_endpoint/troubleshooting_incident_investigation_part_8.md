# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How to view and manage devices related to a Defender incident?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select a device from the Devices view list to open a management bar.
2. Use the management bar to export, manage tags, or initiate automated investigation.
3. Select the check mark for a device to see device details, directory data, active alerts, and logged on users.
4. Select the device name to see device details in the Defender for Endpoint device inventory.
5. From the device page, gather additional information such as all alerts, a timeline, and security recommendations.
6. From the Timeline tab, scroll through the device timeline to view all events and behaviors observed on the machine in chronological order, interspersed with the alerts raised.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents and select the incident under investigation.
3. In the incident details pane, click the Devices tab to confirm the list of associated devices is displayed.
4. Select a device from the list and verify that the management bar appears with options to export, manage tags, or initiate automated investigation.
5. Click the check mark for a device and confirm that the right pane shows device details, directory data, active alerts, and logged on users.
6. Click the device name to open the device inventory page in Defender for Endpoint and verify that all alerts, timeline, and security recommendations are visible.
7. On the device page, select the Timeline tab and confirm that events and behaviors are listed in chronological order, interspersed with alerts.

## Rollback
1. If the device list does not appear or is incomplete, refresh the incident page and verify that the incident is correctly selected.
2. If the management bar does not appear, ensure the device is selected by clicking on it once; if still missing, clear browser cache and reload the portal.
3. If device details, directory data, active alerts, or logged on users are not shown after selecting the check mark, try selecting a different device to rule out a transient issue.
4. If the device inventory page does not load after clicking the device name, navigate directly to Endpoints > Device inventory and search for the device manually.
5. If the Timeline tab does not display events or alerts, verify that the device has been active and that data collection is enabled; check the device's sensor health in the device inventory.
6. If any step fails persistently, contact Microsoft support with the incident ID and device name for further assistance.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
