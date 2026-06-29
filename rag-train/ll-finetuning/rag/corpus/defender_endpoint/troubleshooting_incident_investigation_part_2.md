# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I analyze incident details in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Incident management

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Click an incident to see the Incident pane.
2. Select Open incident page to see the incident details and related information (alerts, devices, investigations, evidence, graph).

## Validation
1. In Microsoft 365 Defender (https://security.microsoft.com), navigate to Incidents & alerts > Incidents. 2. Click on an incident to open the Incident pane. 3. Select 'Open incident page' and confirm that the incident details page displays the following sections: Alerts, Devices, Investigations, Evidence, and Graph. 4. Verify that each section contains the expected data (e.g., alerts list, affected devices, investigation status, evidence entities, and attack graph).

## Rollback
1. Close the incident details page by clicking the 'X' or navigating back to the Incidents list. 2. No configuration changes were made, so no rollback is required. If the incident page fails to load, clear the browser cache and retry, or use an InPrivate/Incognito session. If the issue persists, verify network connectivity and ensure the user has the required permissions (e.g., 'View incidents' role).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/investigate-incidents>
