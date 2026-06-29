# Troubleshooting: Azure Resource Manager

**Domain:** Azure
**Subdomain:** Azure Resource Manager
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot an Azure Resource Manager (ARM) deployment using Visual Studio Code and Azure PowerShell or Azure CLI?

## Environment Context
- **Tenant Type:** Azure subscription
- **Configuration:** Visual Studio Code with Azure Resource Manager Tools extension; Azure PowerShell or Azure CLI installed

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you don't have an Azure subscription, create a free account before you begin.
2. Install Visual Studio Code with the latest Azure Resource Manager Tools extension.
3. Install the latest version of Azure PowerShell or Azure CLI.

## Validation
1. Open Visual Studio Code and verify the Azure Resource Manager Tools extension is installed (look for 'Azure Resource Manager Tools' in the Extensions view).
2. Open a terminal in VS Code and run 'az account show' (Azure CLI) or 'Get-AzContext' (Azure PowerShell) to confirm you are logged into the correct Azure subscription.
3. Create a simple test ARM template (e.g., a storage account) and attempt a deployment using 'az deployment group create --resource-group <test-rg> --template-file <template.json>' or 'New-AzResourceGroupDeployment -ResourceGroupName <test-rg> -TemplateFile <template.json>'. Verify the deployment succeeds without errors.
4. Check the deployment output and Azure portal to confirm the resource was created as expected.

## Rollback
1. If the test deployment fails, review the error output and correct any template syntax or parameter issues.
2. If the extension or tools are not working, uninstall and reinstall the Azure Resource Manager Tools extension from the VS Code marketplace.
3. Reinstall Azure PowerShell using 'Install-Module -Name Az -Force -AllowClobber' or reinstall Azure CLI from the official installer.
4. If the subscription context is incorrect, use 'az account set --subscription <subscription-id>' or 'Set-AzContext -SubscriptionId <subscription-id>' to switch to the correct subscription.
5. Delete any test resources created during validation using 'az group delete --name <test-rg>' or 'Remove-AzResourceGroup -Name <test-rg>'.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/quickstart-troubleshoot-arm-deployment>
