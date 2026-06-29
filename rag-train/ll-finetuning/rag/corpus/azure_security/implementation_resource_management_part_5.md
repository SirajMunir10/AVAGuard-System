# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
How to apply tags to Azure resources for tracking deployment environments?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Tags are key-value pairs applied to Azure resources

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add a key named Environment
2. Give resources deployed to production a value of Production
3. The full key-value pair is Environment = Production

## Validation
Run the following Azure CLI command to verify that the tag 'Environment' with value 'Production' is applied to the target resources: az resource list --tag Environment=Production --query "[].{Name:name, ResourceGroup:resourceGroup, Tags:tags}" -o table. Alternatively, use Azure PowerShell: Get-AzResource -Tag @{Environment='Production'} | Select-Object Name, ResourceGroupName, Tags. Confirm the output lists the intended resources.

## Rollback
To remove the 'Environment' tag from resources, run the Azure CLI command: az tag delete --resource-id <resource-id> --tag Environment --value Production. For multiple resources, use a loop: az resource list --tag Environment=Production --query "[].id" -o tsv | xargs -I {} az tag delete --resource-id {} --tag Environment --value Production. In Azure PowerShell: Get-AzResource -Tag @{Environment='Production'} | ForEach-Object { Remove-AzTag -ResourceId $_.Id -Tag @{Environment='Production'} }.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
