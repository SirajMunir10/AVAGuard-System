# Troubleshooting: Resource Manager

**Domain:** Azure
**Subdomain:** Resource Manager
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Azure Resource Manager template (ARM template) JSON deployment errors?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Validation errors occur before a deployment begins and are caused by syntax errors in your file.
- Preflight validation errors occur when a deployment command is run but resources aren't deployed.
- Deployment errors occur during the deployment process and can only be found by assessing the deployment's progress in your Azure environment.

## Error Codes
N/A

## Root Causes
1. Syntax errors in the ARM template JSON file.
2. Incorrect parameter values causing preflight validation errors.
3. Deployment process errors that are only found by assessing deployment progress.

## Remediation Steps
1. Use a code editor like Visual Studio Code to identify syntax errors in the template file.
2. Check for preflight validation errors when a deployment command is run but resources aren't deployed.
3. Assess the deployment's progress in your Azure environment to find deployment errors.

## Validation
1. Open the ARM template JSON file in Visual Studio Code and verify that no syntax errors are highlighted. 2. Run `az deployment group validate --resource-group <resource-group-name> --template-file <template-file-path>` to confirm preflight validation passes. 3. Execute `az deployment group create --resource-group <resource-group-name> --template-file <template-file-path>` and then run `az deployment group show --resource-group <resource-group-name> --name <deployment-name>` to check the provisioning state is 'Succeeded'.

## Rollback
1. If syntax errors are found, correct them in the JSON file and revalidate. 2. If preflight validation fails, review error details and adjust parameter values or template structure accordingly. 3. If deployment fails, run `az deployment group delete --resource-group <resource-group-name> --name <deployment-name>` to remove the failed deployment, then fix the template based on error messages and redeploy.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/quickstart-troubleshoot-arm-deployment>
