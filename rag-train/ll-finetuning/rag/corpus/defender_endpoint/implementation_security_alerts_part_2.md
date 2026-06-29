# Implementation: Security Alerts

**Domain:** Defender for Endpoint
**Subdomain:** Security Alerts
**Incident Type:** Implementation

## Scenario / Query
How to export security alerts from Microsoft Defender for Cloud to external systems?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Defender for Cloud alerts dashboard, Environment settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Download CSV report on the alerts dashboard provides a one-time export to CSV.
2. Continuous export from Environment settings allows you to configure streams of security alerts and recommendations to Log Analytics workspaces and Event Hubs.
3. Microsoft Sentinel connector streams security alerts from Microsoft Defender for Cloud into Microsoft Sentinel.

## Validation
1. Navigate to Microsoft Defender for Cloud > Security alerts. Click 'Download CSV report' and verify the CSV file contains the expected alert data.
2. Go to Environment settings > Continuous export. Confirm that the export configuration for security alerts to Log Analytics workspace or Event Hubs is enabled and set to 'Enabled'.
3. If using Microsoft Sentinel, open Microsoft Sentinel > Data connectors. Verify the 'Microsoft Defender for Cloud' connector shows a status of 'Connected' and that security alerts are streaming into Sentinel.

## Rollback
1. If CSV export fails, ensure browser allows pop-ups and retry the download.
2. For continuous export issues, navigate to Environment settings > Continuous export, disable the export configuration, then re-enable it after verifying the target Log Analytics workspace or Event Hub is accessible.
3. If the Microsoft Sentinel connector is not streaming, disconnect the connector in Microsoft Sentinel > Data connectors, then reconnect it following the connector configuration steps.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-overview>
