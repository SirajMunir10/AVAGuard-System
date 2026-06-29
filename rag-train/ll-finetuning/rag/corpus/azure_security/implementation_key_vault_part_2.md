# Implementation: Key Vault

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Implementation

## Scenario / Query
How can I redeploy Key Vault with ARM template without deleting existing access policies?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Key Vault redeployment deletes any access policy in Key Vault and replaces them with access policy in ARM template

## Error Codes
N/A

## Root Causes
1. There's no incremental option for Key Vault access policies

## Remediation Steps
1. Read existing access policies in Key Vault and populate ARM template with those policies to avoid any access outages
2. Use Azure RBAC and roles as an alternative to access policies. With Azure RBAC, you can redeploy the key vault without specifying the policy again

## Validation
Run the following Azure CLI command to list the current access policies in the key vault and confirm they match the policies defined in the ARM template: az keyvault show --name <vault-name> --query 'properties.accessPolicies' --output json. Then compare the output with the accessPolicies array in your ARM template. If they are identical, the redeployment succeeded without losing policies.

## Rollback
If the redeployment caused access outages, immediately restore the original access policies by running: az keyvault update --name <vault-name> --set properties.accessPolicies='[{"objectId":"<object-id>","permissions":{"keys":["get","list"],"secrets":["get","list"]}}]' (repeat for each policy). Alternatively, redeploy the key vault using the ARM template that includes the original access policies. If using Azure RBAC, assign the necessary roles via: az role assignment create --assignee <object-id> --role 'Key Vault Secrets User' --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<vault-name>.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
