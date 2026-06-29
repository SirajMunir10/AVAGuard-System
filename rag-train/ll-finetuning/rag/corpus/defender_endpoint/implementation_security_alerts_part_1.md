# Implementation: Security Alerts

**Domain:** Defender for Endpoint
**Subdomain:** Security Alerts
**Incident Type:** Implementation

## Scenario / Query
How to configure streaming of Defender for Cloud security alerts to a SIEM or SOAR solution?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Defender for Cloud workload protection plans enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Stream alerts directly to a Security Information and Event Management (SIEM) such as Microsoft Sentinel
2. Stream alerts to Security Orchestration Automated Response (SOAR) solution
3. Stream alerts to IT Service Management (ITSM) solution

## Validation
1. In the Azure portal, navigate to Microsoft Defender for Cloud > Security alerts. Verify that alerts are being generated for your protected workloads. 2. If streaming to Microsoft Sentinel, go to Microsoft Sentinel > Data connectors and confirm the 'Security Alerts' data type shows a connected status and that alerts are appearing in the Log Analytics workspace (e.g., run `SecurityAlert | take 10`). 3. If streaming to a third-party SIEM/SOAR/ITSM via continuous export, go to Defender for Cloud > Environment settings > select your subscription > Continuous export. Verify that the export is enabled and that the target Event Hub or Log Analytics workspace is correctly configured. 4. Check the target SIEM/SOAR/ITSM console to confirm that test alerts are received within the expected time frame.

## Rollback
1. To stop streaming to Microsoft Sentinel, in Sentinel > Data connectors, disconnect the 'Security Alerts' connector. 2. To disable continuous export, in Defender for Cloud > Environment settings > select your subscription > Continuous export, set the export toggle to 'Off' for the relevant export type (e.g., 'Stream to Event Hub' or 'Export to Log Analytics workspace'). 3. If alerts were being forwarded via an Event Hub, delete or disable the Event Hub namespace or the specific event hub used for alert streaming. 4. Remove any alert forwarding rules or action groups that were created to send alerts to the SIEM/SOAR/ITSM solution.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-overview>
