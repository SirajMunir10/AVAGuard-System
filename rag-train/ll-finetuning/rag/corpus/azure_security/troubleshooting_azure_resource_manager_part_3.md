# Troubleshooting: Azure Resource Manager

**Domain:** Azure
**Subdomain:** Azure Resource Manager
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix a preflight validation error in an ARM template deployment due to invalid storage name prefix?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Template fails preflight validation and deployment is not run
- No deployment history is created
- Activity log shows the preflight error

## Error Codes
N/A

## Root Causes
1. The prefixName parameter is more than 11 characters
2. The prefixName contains special characters and uppercase letters
3. Storage names must be between 3 and 24 characters and use only lowercase letters and numbers

## Remediation Steps
1. Use a prefix that is 11 characters or less
2. Ensure the prefix contains only lowercase letters or numbers

## Validation
1. Run the Azure CLI command: az deployment group validate --resource-group <resource-group-name> --template-file <template-file-path> --parameters prefixName=<valid-prefix> --output json. 2. Verify the output contains 'properties': {'valid': true} and no error messages. 3. Check the Activity Log in the Azure portal for the resource group; confirm no preflight validation errors appear for the deployment.

## Rollback
1. Revert the prefixName parameter to its original invalid value. 2. Run the Azure CLI command: az deployment group validate --resource-group <resource-group-name> --template-file <template-file-path> --parameters prefixName=<original-invalid-prefix> --output json. 3. Confirm the output shows a preflight validation error matching the original error. 4. If the deployment was already attempted with the invalid prefix, no deployment history exists, so no further rollback is needed.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/quickstart-troubleshoot-arm-deployment>
