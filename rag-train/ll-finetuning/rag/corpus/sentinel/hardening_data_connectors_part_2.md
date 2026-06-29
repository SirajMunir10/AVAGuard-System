# Hardening: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Hardening

## Scenario / Query
A customer has deployed Microsoft Sentinel but notices that the SecurityEvent data connector is ingesting events from all Windows Event Log channels, including verbose and analytic logs, causing high ingestion costs and noise. How can they harden the connector to only collect security-relevant events (e.g., Audit Success/Failure for specific event IDs) and reduce the data volume?

## Environment Context
- **Tenant Type:** Enterprise (Azure tenant with Microsoft Sentinel enabled)
- **Configuration:** SecurityEvent data connector configured with default 'AllEvents' setting

## Symptoms
- High daily data ingestion volume from Windows Event Logs
- Large number of low-severity or informational security events in Sentinel
- Increased Azure Monitor Log Analytics costs

## Error Codes
N/A

## Root Causes
1. The SecurityEvent data connector is configured to collect all Windows Event Log events (default 'AllEvents' setting) instead of using a filtered set of event IDs
2. No explicit filtering of event channels (e.g., Security, System, Application) or event IDs (e.g., 4624, 4625, 4688)

## Remediation Steps
1. 1. In the Microsoft Sentinel portal, navigate to Data connectors > Security Events via Windows Event Forwarding (or Windows Security Events via AMA).
2. 2. Select the connector and click 'Open connector page'.
3. 3. Under 'Configuration', click 'Edit' on the data collection rule (DCR) associated with the connector.
4. 4. In the DCR, change the 'Data source' from 'AllEvents' to 'Minimal' or 'Common' (or create a custom XPath query to filter specific event IDs such as 4624, 4625, 4688, 4776, etc.).
5. 5. Save the DCR and verify that only the desired events are being ingested.
6. 6. Optionally, use Azure Policy to enforce the use of filtered DCRs across all workspaces.

## Validation
Run the following KQL query in Sentinel to confirm reduced ingestion: SecurityEvent | where TimeGenerated > ago(1h) | summarize count() by EventID. Compare the count and variety of EventIDs before and after the change.

## Rollback
Revert the DCR data source setting back to 'AllEvents' or restore the previous DCR configuration via the Azure portal or PowerShell.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-windows-security-events?tabs=AMA>
- <https://learn.microsoft.com/en-us/azure/sentinel/best-practices-cost>
