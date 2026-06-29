# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate alerts affecting the network in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select an alert from the alerts queue to go to the alert page.
2. From the alert page, begin your investigation by selecting the affected assets or any of the entities under the alert story tree view.
3. The details pane automatically populates with further information about what you selected.

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. In the left navigation, under 'Endpoints', select 'Alerts' to open the alerts queue.
3. Confirm that the alerts queue loads without errors and displays the list of alerts.
4. Select an alert from the queue and verify that the alert page opens, showing the alert title, severity, status, and other details.
5. On the alert page, locate the 'Alert story' tree view and verify that it displays affected assets and entities (e.g., devices, users, IP addresses).
6. Click on an affected asset or entity in the alert story tree view and confirm that the details pane automatically populates with relevant information (e.g., device details, user details, or IP address details).
7. Repeat the selection for different entity types to ensure the details pane updates correctly.

## Rollback
1. If the alert page fails to open or displays incorrect data, clear the browser cache and cookies, then reload the Microsoft 365 Defender portal.
2. If the alert story tree view does not show expected entities, verify that the alert is not a false positive and that the affected assets are still active in the tenant.
3. If the details pane does not populate automatically, manually refresh the alert page by pressing F5 or clicking the browser's refresh button.
4. If the issue persists, check the service health dashboard in the Microsoft 365 Defender portal (Health > Service health) for any ongoing incidents or advisories related to Microsoft Defender for Endpoint.
5. If the problem continues, contact Microsoft Support and provide the alert ID, tenant ID, and a description of the behavior observed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/investigate-alerts>
