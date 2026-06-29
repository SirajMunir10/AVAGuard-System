# Implementation: Data Transformation

**Domain:** Sentinel
**Subdomain:** Data Transformation
**Incident Type:** Implementation

## Scenario / Query
How do I configure data collection rules (DCRs) for data transformation in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Data collection rules (DCRs) in Azure Monitor and Microsoft Sentinel

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Learn more about data transformation and DCRs in Azure Monitor and Microsoft Sentinel. For more information, see: Data collection rules in Azure Monitor, Logs ingestion API in Azure Monitor Logs (Preview), Transformations in Azure Monitor Logs (preview), Data transformation in Microsoft Sentinel (preview).
2. Verify data connector support. Make sure that your data connectors are supported for data transformation. In our data connector reference article, check the section for your data connector to understand which types of DCRs are supported. Continue in this article to understand how the DCR type you select affects the rest of the ingestion and transformation process.

## Validation
1. Verify that the data collection rule (DCR) is created and associated with the correct data source: Use Azure CLI command 'az monitor data-collection rule show --name <DCR-name> --resource-group <resource-group> --query "properties.dataSources"' to confirm the data sources are configured as expected. 2. Validate that the transformation is applied: Run 'az monitor data-collection rule show --name <DCR-name> --resource-group <resource-group> --query "properties.dataFlows[].transformKql"' to ensure the KQL transformation is set. 3. Check that logs are being ingested with the transformation: In the Log Analytics workspace, run a query like 'Usage | where TimeGenerated > ago(1h) | where DataType == "<YourDataType>" | summarize count() by _ResourceId' to confirm data is flowing. 4. Confirm the data connector supports the DCR type: Refer to the data connector reference article at https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources and check the specific connector's DCR support.

## Rollback
1. Remove the transformation from the DCR: Use Azure CLI command 'az monitor data-collection rule update --name <DCR-name> --resource-group <resource-group> --set properties.dataFlows[0].transformKql=""' to clear the transformation. 2. If the DCR was newly created, delete it: Run 'az monitor data-collection rule delete --name <DCR-name> --resource-group <resource-group>'. 3. Revert to the previous DCR configuration: If a backup exists, apply it using 'az monitor data-collection rule create --name <DCR-name> --resource-group <resource-group> --location <location> --rule-file <backup-file>'. 4. Verify that data ingestion returns to normal: In the Log Analytics workspace, run a query to confirm data is being ingested without transformation, e.g., 'Usage | where TimeGenerated > ago(1h) | where DataType == "<YourDataType>" | summarize count() by _ResourceId'.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation>
