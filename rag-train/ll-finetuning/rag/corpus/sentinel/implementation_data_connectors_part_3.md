# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
A security administrator is deploying Microsoft Sentinel and needs to collect Windows security events from on-premises servers using the Windows Security Events via AMA connector. After installing the Azure Monitor Agent (AMA) and configuring the Data Collection Rule (DCR), no events appear in Sentinel. What configuration step is missing?

## Environment Context
- **Tenant Type:** Enterprise (Azure + on-premises hybrid)
- **Configuration:** Sentinel workspace in a single region; Windows servers in on-premises Active Directory; Azure Arc enabled for on-premises servers; AMA installed via Azure Arc; DCR created but not linked to the correct data stream for Windows Security Events.

## Symptoms
- Windows Security Events connector shows 'Connected' but no events ingested
- No security events in the SecurityEvent table in Log Analytics
- Azure Monitor Agent heartbeat is present in the Heartbeat table

## Error Codes
N/A

## Root Causes
1. The Data Collection Rule (DCR) was created but the 'WindowsSecurityEvents' data stream was not selected or the DCR is not associated with the correct resource group containing the Arc-enabled servers
2. The DCR is not linked to the Log Analytics workspace used by Sentinel

## Remediation Steps
1. 1. In the Azure portal, navigate to the Data Collection Rule associated with the Windows Security Events connector.
2. 2. Under 'Resources', verify that the Arc-enabled Windows servers are listed. If not, add them.
3. 3. Under 'Data Sources', ensure a data source of type 'Windows Security Events' is present and that the 'Data stream' is set to 'WindowsSecurityEvents'.
4. 4. Under 'Destinations', confirm that the destination is the Log Analytics workspace linked to your Sentinel instance.
5. 5. Save the DCR and wait up to 10 minutes for data to appear. If still missing, use the 'Logs' blade in Sentinel to run: `SecurityEvent | take 10`.

## Validation
Run `SecurityEvent | where TimeGenerated > ago(1h) | count` in the Sentinel Logs workspace. A count greater than zero confirms successful ingestion.

## Rollback
If the connector is misconfigured, remove the Windows Security Events data source from the DCR, or delete the DCR entirely and recreate it following the documented steps.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-windows-security-events?tabs=AMA>
