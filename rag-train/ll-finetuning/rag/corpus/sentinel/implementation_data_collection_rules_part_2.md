# Implementation: Data Collection Rules

**Domain:** Sentinel
**Subdomain:** Data Collection Rules
**Incident Type:** Implementation

## Scenario / Query
How do I choose the correct Data Collection Rule (DCR) type for a specific data connector in Microsoft Sentinel?

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
1. Refer to the article to choose which kind of DCR is needed for your particular data connector.
2. Follow the instructions for the chosen scenario.

## Validation
1. Confirm that the correct Data Collection Rule (DCR) type is associated with the data connector by running: `Get-AzDataCollectionRule | Where-Object {$_.DataSources -match '<connector-name>'}` (replace <connector-name> with the actual connector name).
2. Verify that data ingestion is working as expected by checking the Sentinel Logs workspace: `Search-AzMonitorLog -WorkspaceId <workspace-id> -Query 'Usage | where DataType == "<connector-data-type>" | summarize count() by bin(TimeGenerated, 1h)'` (replace <workspace-id> and <connector-data-type> accordingly).
3. Review the DCR configuration in the Azure portal under 'Data Collection Rules' to ensure the data source and destination are correctly set per the chosen scenario.

## Rollback
1. If the DCR type is incorrect, delete the misconfigured DCR: `Remove-AzDataCollectionRule -Name <dcr-name> -ResourceGroupName <resource-group>` (replace <dcr-name> and <resource-group>).
2. Recreate the DCR with the correct type following the instructions in the source article: https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation.
3. If data ingestion fails after the change, revert to the previous DCR by restoring from backup or re-applying the original DCR configuration using: `New-AzDataCollectionRule -Name <original-dcr-name> -ResourceGroupName <resource-group> -Location <location> -DataSources <original-data-sources> -Destinations <original-destinations>`.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation>
