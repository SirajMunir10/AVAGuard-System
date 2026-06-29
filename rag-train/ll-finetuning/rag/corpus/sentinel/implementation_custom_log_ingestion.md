# Implementation: Custom Log Ingestion

**Domain:** Sentinel
**Subdomain:** Custom Log Ingestion
**Incident Type:** Implementation

## Scenario / Query
How do I use the Custom Log API to normalize custom-format logs for ingestion into Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Custom Log API, Data Collection Rules (DCRs)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Custom Log API to normalize custom-format logs.
2. Ingest logs into standard tables or create customized output tables with user-defined schemas.
3. Configure the DCR in the Log Analytics portal, via API, or using an ARM template.

## Validation
1. Verify that the Data Collection Rule (DCR) is created and associated with the correct Log Analytics workspace: `Get-AzDataCollectionRule -ResourceGroupName <ResourceGroupName> -RuleName <DCRName> | Format-List`
2. Confirm the DCR includes the custom log ingestion stream and transformation: `Get-AzDataCollectionRuleAssociation -TargetResourceId <WorkspaceResourceId> | Format-List`
3. Send a sample log to the custom log endpoint and check for successful ingestion: `Invoke-RestMethod -Method Post -Uri 'https://<workspaceId>.ods.opinsights.azure.com/api/logs?api-version=2016-04-01' -Headers @{'Authorization'='Bearer <token>';'Content-Type'='application/json'} -Body '<sampleLog>'`
4. Query the target table in Log Analytics to confirm data appears: `union withsource=TableName * | where TimeGenerated > ago(5m) | take 10`

## Rollback
1. Remove the Data Collection Rule association: `Remove-AzDataCollectionRuleAssociation -TargetResourceId <WorkspaceResourceId> -AssociationName <AssociationName>`
2. Delete the Data Collection Rule: `Remove-AzDataCollectionRule -ResourceGroupName <ResourceGroupName> -RuleName <DCRName>`
3. If custom tables were created, drop them via Log Analytics: `.drop table <CustomTableName>`
4. Revert any ARM template deployments that added the DCR: `New-AzResourceGroupDeployment -ResourceGroupName <ResourceGroupName> -TemplateFile <originalTemplate.json>`

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation>
