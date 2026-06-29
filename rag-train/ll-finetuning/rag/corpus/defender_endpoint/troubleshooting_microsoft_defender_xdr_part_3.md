# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to view and analyze alerts related to a specific incident in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Alerts tab in incident investigation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Alerts tab within the incident to view the alert queue.
2. Review severity, entities involved, source (Defender for Identity, Defender for Endpoint, Defender for Office 365, Microsoft Defender for Cloud Apps, app governance add-on), and reason alerts link together.
3. Select an alert to see alert information specific to the incident context, including events, triggered alerts, and affected entities (devices, files, users, cloud apps, mailboxes).

## Validation
1. Navigate to https://security.microsoft.com/incidents and select the incident ID. 2. Click the 'Alerts' tab and confirm the alert queue displays alerts with severity, entities, and source (e.g., Defender for Endpoint, Defender for Identity). 3. Select an alert and verify the alert details pane shows events, triggered alerts, and affected entities (devices, files, users, cloud apps, mailboxes) specific to the incident context.

## Rollback
1. If alerts are missing or incorrect, refresh the incident page and verify the incident ID is correct. 2. If the alert queue is empty, check the time range filter and ensure alerts are not filtered out. 3. If alert details are incomplete, navigate to the 'Alerts' queue (https://security.microsoft.com/alerts) and search for the alert ID directly to view full details outside the incident context.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
