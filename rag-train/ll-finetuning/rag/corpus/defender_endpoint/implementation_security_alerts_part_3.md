# Implementation: Security Alerts

**Domain:** Defender for Endpoint
**Subdomain:** Security Alerts
**Incident Type:** Implementation

## Scenario / Query
How to connect Microsoft Defender for Cloud to SIEM solutions like Microsoft Sentinel for alert streaming?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Defender for Cloud enabled, SIEM/SOAR/ITSM solution available

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Connect Microsoft Defender for Cloud to SIEM solutions including Microsoft Sentinel
2. Consume the alerts from your tool of choice
3. Stream alerts to a SIEM, SOAR, or IT Service Management solution

## Validation
1. In the Azure portal, navigate to Microsoft Defender for Cloud > Security alerts. Verify that alerts are visible. 2. Go to Microsoft Sentinel (or your SIEM) and confirm that the same alerts appear in the ingested logs. 3. Check the data connector status in Sentinel: Azure Active Directory > Data connectors > 'Azure Security Center' (or 'Microsoft Defender for Cloud') and ensure the connector shows 'Connected' and has recent data. 4. Run a sample query in Sentinel, e.g., `SecurityAlert | where ProviderName == 'ASC' | take 10`, to confirm alert streaming.

## Rollback
1. In Microsoft Sentinel, navigate to Data connectors, select the 'Azure Security Center' (or 'Microsoft Defender for Cloud') connector, and click 'Disconnect'. 2. In Defender for Cloud, go to Environment settings, select your subscription, and under 'Integrations', disable the SIEM integration (e.g., uncheck 'Stream alerts to SIEM'). 3. If using a different SIEM, remove the API connection or webhook configured for alert ingestion. 4. Verify that alerts no longer appear in the SIEM by checking the last ingestion timestamp and running a query for recent alerts.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/managing-and-responding-alerts>
