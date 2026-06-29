# Governance: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Governance

## Scenario / Query
A Microsoft Sentinel workspace is ingesting data from multiple regions and sources, but the security team cannot determine which data connectors are actively sending data, which are failing, or whether any connectors have been disabled without authorization. How can an administrator audit the health and status of all Microsoft Sentinel data connectors across the workspace?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with multiple data connectors (e.g., Azure Activity, Office 365, Microsoft Defender for Cloud, custom logs)

## Symptoms
- No single dashboard or report shows the operational status of all data connectors
- Data ingestion gaps are noticed only after an incident occurs
- Connector failures are not proactively alerted
- Audit logs show changes to connector configurations but no easy way to correlate with connector health

## Error Codes
N/A

## Root Causes
1. Lack of centralized monitoring for data connector health and status
2. No automated alerting rules configured for connector failures or configuration changes
3. Insufficient use of the Sentinel Health workbook or the â€˜SentinelHealthâ€™ table

## Remediation Steps
1. Enable the Sentinel Health data connector (Preview) to collect diagnostic data from Sentinel into the â€˜SentinelHealthâ€™ table.
2. Use the built-in â€˜Sentinel Healthâ€™ workbook to monitor connector status, ingestion latency, and data volume anomalies.
3. Create analytics rules that trigger alerts when a data connector status changes to â€˜Errorâ€™ or when ingestion stops for a defined period.
4. Configure Azure Policy to audit and enforce the deployment of required data connectors across the environment.
5. Review the â€˜SentinelAuditâ€™ table for any unauthorized changes to connector configurations.

## Validation
Open the Sentinel Health workbook and confirm that all expected data connectors show a status of â€˜Connectedâ€™ and that ingestion latency is within acceptable thresholds. Verify that alert rules for connector health trigger correctly by temporarily disabling a connector (in a non-production workspace).

## Rollback
Disable any alert rules created for connector health monitoring. Remove the Sentinel Health data connector if it was enabled. Revert any Azure Policy assignments that enforce connector deployment.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/monitor-data-connector-health>
- <https://learn.microsoft.com/en-us/azure/sentinel/sentinel-health-table-reference>
