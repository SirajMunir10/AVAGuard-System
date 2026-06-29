# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How to create a custom data connector for Microsoft Sentinel when no existing solution is available?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Consider creating your own data source connector.
2. Configure the data source APIs with the Codeless Connector Framework.
3. Use the Log Ingestion API for Azure Monitor as part of an Azure Function or Logic App.
4. Use Azure Monitor Agent directly or Logstash to create your custom connector.

## Validation
1. Verify that the custom data connector appears in the Microsoft Sentinel workspace under Data connectors with a connected status.
2. Run the following KQL query in the Sentinel Logs workspace to confirm data ingestion: `YourCustomTable_CL | take 10` (replace YourCustomTable_CL with the actual table name).
3. Check the Azure Function or Logic App execution logs for successful data submission to the Log Analytics workspace.
4. Validate that the data source API is returning expected data by testing the API endpoint independently.

## Rollback
1. Delete the custom data connector from the Microsoft Sentinel Data connectors blade.
2. Remove any associated Azure Function or Logic App that was created for data ingestion.
3. Delete the custom table created in the Log Analytics workspace using: `Remove-AzOperationalInsightsTable -ResourceGroupName <RG> -WorkspaceName <WS> -TableName YourCustomTable_CL`.
4. If Azure Monitor Agent was used, remove the data collection rule (DCR) associated with the custom connector via Azure portal or PowerShell: `Remove-AzDataCollectionRule -ResourceGroupName <RG> -Name <DCRName>`.
5. Restore any previous data connector configuration from backup if applicable.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources>
