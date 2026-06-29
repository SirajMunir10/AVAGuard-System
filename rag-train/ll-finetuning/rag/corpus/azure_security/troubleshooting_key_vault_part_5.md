# Troubleshooting: Key Vault

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
How can I give the AD group access to the key vault?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Key Vault access permissions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Give the AD group permissions to your key vault using Azure RBAC with the Azure CLI az role assignment create command, or the Azure PowerShell New-AzRoleAssignment cmdlet.
2. If you are using legacy access policies, you can use the Azure CLI az keyvault set-policy command or the Azure PowerShell Set-AzKeyVaultAccessPolicy cmdlet. However, Azure RBAC is the recommended authorization model.

## Validation
To confirm that the AD group has been granted access to the key vault, run the following Azure CLI command: az role assignment list --assignee <AD_Group_Object_ID> --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<vault-name>. Verify that the output includes the expected role (e.g., 'Key Vault Secrets User') and that the scope matches the key vault. If using legacy access policies, run: az keyvault show --name <vault-name> --query 'properties.accessPolicies[?objectId==`<AD_Group_Object_ID>`]' and confirm the permissions array includes the intended operations (e.g., 'get', 'list').

## Rollback
To remove the RBAC role assignment, run: az role assignment delete --assignee <AD_Group_Object_ID> --role '<role-name>' --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<vault-name>. To remove a legacy access policy, run: az keyvault delete-policy --name <vault-name> --object-id <AD_Group_Object_ID>. If the remediation fails or causes unintended access issues, restore the previous state by re-applying the original role assignment or access policy using the same commands with the original parameters.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
