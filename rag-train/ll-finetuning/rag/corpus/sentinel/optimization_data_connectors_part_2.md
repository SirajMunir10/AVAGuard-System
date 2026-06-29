# Optimization: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Optimization

## Scenario / Query
A Microsoft Sentinel workspace is ingesting security events from Windows machines using the legacy Security Events connector instead of the Windows Security Events via AMA connector. How can I migrate to the AMA-based connector to reduce ingestion costs and improve performance?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Sentinel workspace with legacy Security Events connector (Event Logs) enabled on multiple Windows VMs

## Symptoms
- High data ingestion volume from Windows Event Logs
- Legacy Security Events connector shows 'Connected' status but uses older agent
- Unable to filter specific event IDs without custom Log Analytics queries

## Error Codes
N/A

## Root Causes
1. Legacy Microsoft Monitoring Agent (MMA) is still deployed instead of Azure Monitor Agent (AMA)
2. Security Events connector (legacy) does not support advanced filtering or cost optimization features available in the AMA-based connector

## Remediation Steps
1. 1. Deploy the Azure Monitor Agent (AMA) on Windows machines using Azure Policy or manual installation.
2. 2. In Microsoft Sentinel, enable the 'Windows Security Events via AMA' data connector.
3. 3. Create a Data Collection Rule (DCR) that specifies which security event IDs to collect (e.g., minimal set per Microsoft best practices).
4. 4. Verify that events are flowing into the Sentinel workspace under the 'WindowsEvent' table.
5. 5. Disable the legacy Security Events connector after confirming AMA-based ingestion is working.

## Validation
Run the following KQL query in Sentinel to confirm events are being ingested via AMA: WindowsEvent | where TimeGenerated > ago(1h) | summarize count() by Computer. Then check that the legacy connector shows 'Disconnected' after removal.

## Rollback
Re-enable the legacy Security Events connector and remove the AMA-based DCR. Reinstall the Microsoft Monitoring Agent if needed.

## References
- Microsoft Learn, 'Windows Security Events via AMA connector' - https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/windows-security-events-via-ama
