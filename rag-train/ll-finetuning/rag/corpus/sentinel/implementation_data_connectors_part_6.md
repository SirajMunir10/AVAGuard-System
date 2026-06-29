# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Sentinel, the Windows Security Events via AMA connector shows a status of 'Connected' but no security events are ingested. What configuration step is missing?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Data Collection Rule (DCR) for Windows Security Events using Azure Monitor Agent (AMA) is deployed and linked to the Sentinel workspace, but the DCR does not include the 'SecurityEvents' data source.

## Symptoms
- Windows Security Events via AMA connector shows 'Connected' in Sentinel
- No security events appear in the SecurityEvent table
- Azure Monitor Agent is installed and heartbeat is present

## Error Codes
N/A

## Root Causes
1. The Data Collection Rule (DCR) associated with the connector does not have the 'SecurityEvents' data source configured
2. The DCR was created using a template that only collects performance counters or custom logs, not security events

## Remediation Steps
1. Navigate to Azure Monitor > Data Collection Rules and select the DCR linked to the Sentinel connector
2. Under 'Resources', add the 'SecurityEvents' data source with the desired event log levels (e.g., All Events, Minimal, Common)
3. Save the DCR and allow up to 5 minutes for ingestion to begin
4. Verify data ingestion by running a KQL query: SecurityEvent | take 10

## Validation
Run the KQL query 'SecurityEvent | where TimeGenerated > ago(10m) | count' in the Sentinel Logs blade. A count greater than 0 confirms successful ingestion.

## Rollback
Remove the 'SecurityEvents' data source from the DCR and save. The connector will remain connected but stop ingesting security events.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference-windows-security-events-via-ama>
