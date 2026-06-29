# Troubleshooting: Azure Resource Manager

**Domain:** Azure
**Subdomain:** Azure Resource Manager
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix an ARM template deployment error caused by a reference to a non-existent virtual network?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Deployment fails because outputs references a virtual network that doesn't exist in the resource group
- Deployment history shows a failed deployment
- Storage account resource deployed successfully but overall deployment failed

## Error Codes
N/A

## Root Causes
1. The template's outputs section contains a reference function pointing to a virtual network resource that does not exist in the resource group

## Remediation Steps
1. Change the reference function to use a valid resource
2. Delete the comma that precedes vnetResult and all of vnetResult
3. Save the file and rerun the deployment

## Validation
1. Run 'Get-AzResourceGroupDeployment -ResourceGroupName <ResourceGroupName> -Name <DeploymentName>' to confirm the deployment succeeded. 2. Verify the outputs section by running 'Get-AzResourceGroupDeployment -ResourceGroupName <ResourceGroupName> -Name <DeploymentName> | Select-Object -ExpandProperty Outputs' and ensure no reference to a non-existent virtual network. 3. Check that the storage account resource is deployed and its properties are correct using 'Get-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName>'.

## Rollback
1. If the deployment fails again, redeploy the previous working version of the template using 'New-AzResourceGroupDeployment -ResourceGroupName <ResourceGroupName> -TemplateFile <PathToPreviousTemplate>'. 2. If the storage account was incorrectly modified, restore it from a backup or redeploy with the correct template. 3. Review the deployment history with 'Get-AzResourceGroupDeployment -ResourceGroupName <ResourceGroupName> | Where-Object {$_.ProvisioningState -eq "Failed"}' to identify and correct any remaining issues.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/quickstart-troubleshoot-arm-deployment>
