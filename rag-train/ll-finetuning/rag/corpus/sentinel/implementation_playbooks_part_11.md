# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I apply tags to a Logic App for a Microsoft Sentinel playbook during creation?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Logic App Standard workflow creation in Azure portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. To apply tags to this logic app for resource categorization and billing purposes, select Next: Tags >.
2. Otherwise, select Review + create.

## Validation
1. In the Azure portal, navigate to the Logic App resource you created. 2. Under 'Settings', select 'Tags'. 3. Verify that the tags you specified during creation are listed with the correct names and values. 4. Optionally, run the Azure CLI command: az resource show --resource-group <ResourceGroupName> --name <LogicAppName> --resource-type 'Microsoft.Logic/workflows' --query 'tags'

## Rollback
1. In the Azure portal, go to the Logic App resource. 2. Under 'Settings', select 'Tags'. 3. Remove or modify the tags that were applied during creation. 4. Alternatively, use the Azure CLI: az resource tag --resource-group <ResourceGroupName> --name <LogicAppName> --resource-type 'Microsoft.Logic/workflows' --tags {}

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
