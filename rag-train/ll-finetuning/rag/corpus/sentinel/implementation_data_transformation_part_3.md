# Implementation: Data Transformation

**Domain:** Sentinel
**Subdomain:** Data Transformation
**Incident Type:** Implementation

## Scenario / Query
How do I configure data transformation for Microsoft Sentinel using Log Analytics and Azure Monitor documentation?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Data Collection Rules (DCRs)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Direct ingestion through the Log Ingestion API: Walk through a tutorial for ingesting logs using the Azure portal.
2. Direct ingestion through the Log Ingestion API: Walk through a tutorial for ingesting logs using Azure Resource Manager (ARM) templates and REST API.
3. Workspace transformations: Walk through a tutorial for configuring workspace transformation using the Azure portal.
4. Workspace transformations: Walk through a tutorial for configuring workspace transformation using Azure Resource Manager (ARM) templates and REST API.

## Validation
1. Verify that the Data Collection Rule (DCR) is created and associated with the correct Log Analytics workspace: `Get-AzDataCollectionRule -ResourceGroupName <ResourceGroupName> -RuleName <DCRName> | Format-List`
2. Confirm that the transformation KQL query is applied correctly: `Get-AzDataCollectionRuleAssociation -TargetResourceId <WorkspaceResourceId> | Select-Object -ExpandProperty DataCollectionRuleId`
3. Ingest a test log entry using the Log Ingestion API and verify it appears in the custom table with the expected transformed schema: `search * | where TimeGenerated > ago(1h) | take 10`
4. For workspace transformations, check that the transformation is enabled on the workspace: `Get-AzOperationalInsightsWorkspace -ResourceGroupName <ResourceGroupName> -Name <WorkspaceName> | Select-Object -ExpandProperty Features`
5. Validate that the transformation is applied to incoming logs by querying the transformed table and confirming no raw data remains: `TableName_CL | where TimeGenerated > ago(1h) | summarize count() by _ResourceId`

## Rollback
1. Remove the Data Collection Rule association: `Remove-AzDataCollectionRuleAssociation -TargetResourceId <WorkspaceResourceId> -AssociationName <AssociationName>`
2. Delete the Data Collection Rule: `Remove-AzDataCollectionRule -ResourceGroupName <ResourceGroupName> -RuleName <DCRName>`
3. For workspace transformations, disable the transformation by removing the transformation KQL from the workspace configuration: `Update-AzOperationalInsightsWorkspace -ResourceGroupName <ResourceGroupName> -Name <WorkspaceName> -Features @{enableLogAccessUsingOnlyResourcePermissions=$false}`
4. If a custom table was created, drop it: `Drop-Table -TableName <TableName> -WorkspaceId <WorkspaceId>`
5. Revert to direct ingestion without transformation by reconfiguring the data source to send raw logs to the default table.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation>
