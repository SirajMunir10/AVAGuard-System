# Implementation: Data Transformation

**Domain:** Sentinel
**Subdomain:** Data Transformation
**Incident Type:** Implementation

## Scenario / Query
How to migrate from custom Microsoft Sentinel data connectors or built-in API-based data connectors to ingestion-time data transformation?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with custom data connectors

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure a DCR to define, from scratch, the custom ingestion from your data source to a new table. You might use this option if you want to use a new schema that doesn't have the current column suffixes, and doesn't require query-time KQL functions to standardize your data. After you've verified that your data is properly ingested to the new table, you can delete the legacy table, as well as your legacy, custom data connector.
2. Continue using the custom table created by your custom data connector. You might use this option if you have a lot of custom security content created for your existing table. In such cases, see Migrate from Data Collector API and custom fields-enabled tables to DCR-based custom logs in the Azure Monitor documentation.

## Validation
1. Verify that the new DCR-based table is receiving data by running a sample query in the Log Analytics workspace: `YourNewTable_CL | take 10`. 2. Confirm that the data schema matches the expected transformation by checking the table schema in Log Analytics: `| getschema`. 3. Ensure that the legacy custom data connector is no longer sending data by checking the connector's health in Sentinel under Data connectors. 4. Validate that any security content (analytics rules, workbooks) referencing the new table works correctly.

## Rollback
1. If the new DCR-based table is not receiving data, revert to the legacy custom data connector by re-enabling it in Sentinel under Data connectors. 2. Delete the new DCR-based table using the Azure portal or PowerShell: `Remove-AzOperationalInsightsTable -ResourceGroupName <RG> -WorkspaceName <WS> -TableName YourNewTable_CL`. 3. Restore any deleted legacy tables from the Recycle Bin in Log Analytics if necessary. 4. Reapply any query-time KQL functions that were previously used to standardize data from the legacy table.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation>
