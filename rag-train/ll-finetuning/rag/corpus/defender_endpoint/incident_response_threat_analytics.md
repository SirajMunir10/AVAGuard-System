# Incident Response: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Incident Response

## Scenario / Query
How to view and manage incidents related to a tracked threat in Microsoft Defender XDR Threat Analytics?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Threat Analytics module

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Related incidents tab in the threat analytics report.
2. View the list of all incidents related to the tracked threat.
3. Assign incidents or manage alerts linked to each incident.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Threat Analytics under the Endpoints section.
3. Select the specific threat report for the tracked threat.
4. Click on the 'Related incidents' tab.
5. Confirm that the list of incidents displayed corresponds to the tracked threat and includes expected incident IDs, titles, severity, and status.
6. Verify that you can click on an incident to view its details and manage alerts.

## Rollback
1. If the 'Related incidents' tab does not show expected incidents, refresh the page and ensure the correct threat report is selected.
2. If incidents are missing, check that the threat analytics report is up-to-date by navigating to the Threat Analytics dashboard and verifying the report's last updated time.
3. If incidents were incorrectly assigned or alerts mismanaged, reassign incidents to the original owner or reset alert statuses using the incident management options within the incident details page.
4. If the issue persists, contact Microsoft support with the tenant ID and threat analytics report details for further investigation.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
