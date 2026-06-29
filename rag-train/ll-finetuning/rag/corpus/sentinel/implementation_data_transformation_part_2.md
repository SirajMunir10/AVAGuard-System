# Implementation: Data Transformation

**Domain:** Sentinel
**Subdomain:** Data Transformation
**Incident Type:** Implementation

## Scenario / Query
How do I determine my requirements for data transformation in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Data Collection Rules (DCR), Log Ingestion API

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Determine your requirements
2. Custom data through the Log Ingestion API: Required, included in the DCR that defines the data model
3. Built-in data types (Syslog, CommonSecurityLog, WindowsEvent, SecurityEvent) using the Azure Monitor Agent: Optional, if desired added to the DCR that configures how this data is being ingested
4. Built-in data types from most other sources: Optional, if desired added to the DCR attached to the Workspace where this data is being ingested (Workspace transformation DCR)

## Validation
1. Confirm that the Data Collection Rule (DCR) exists and is correctly associated: `az monitor data-collection rule show --name <DCR-name> --resource-group <RG-name> --query "{id:id, location:location, properties:properties}"`
2. Verify the DCR includes the expected data transformations: `az monitor data-collection rule show --name <DCR-name> --resource-group <RG-name> --query "properties.dataFlows[].transformKql"`
3. For custom data via Log Ingestion API, ensure the DCR's `streamDeclarations` match the custom table schema: `az monitor data-collection rule show --name <DCR-name> --resource-group <RG-name> --query "properties.streamDeclarations"`
4. For built-in data types (Syslog, CommonSecurityLog, WindowsEvent, SecurityEvent) using Azure Monitor Agent, confirm the DCR is assigned to the agent: `az monitor data-collection rule association list --resource <VM-ID> --query "[].properties.dataCollectionRuleId"`
5. For workspace-level transformations, verify the workspace transformation DCR is attached: `az monitor log-analytics workspace show --name <Workspace-name> --resource-group <RG-name> --query "properties.defaultDataCollectionRuleResourceId"`

## Rollback
1. Remove custom data stream from the DCR: `az monitor data-collection rule update --name <DCR-name> --resource-group <RG-name> --remove properties.streamDeclarations.<custom-stream-name>`
2. Remove transformation KQL from data flows: `az monitor data-collection rule update --name <DCR-name> --resource-group <RG-name> --set properties.dataFlows[0].transformKql=null`
3. Disassociate the DCR from Azure Monitor Agent: `az monitor data-collection rule association delete --name <Association-name> --resource-group <RG-name>`
4. Remove workspace transformation DCR: `az monitor log-analytics workspace update --name <Workspace-name> --resource-group <RG-name> --set properties.defaultDataCollectionRuleResourceId=null`
5. If needed, delete the entire DCR: `az monitor data-collection rule delete --name <DCR-name> --resource-group <RG-name>`

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation>
