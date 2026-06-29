# Implementation: Key Vault

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Implementation

## Scenario / Query
How can I provide key vault authentication using access control policy?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Key Vault access control policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The simplest way to authenticate a cloud-based application to Key Vault is with a managed identity; see Authenticate to Azure Key Vault for details.
2. If you're creating an on-premises application, doing local development, or otherwise unable to use a managed identity, you can instead register a service principal manually and provide access to your key vault using Azure RBAC. See Azure RBAC for Key Vault data plane operations.

## Validation
1. Verify that the managed identity is enabled for the Azure resource (e.g., VM, App Service) by running: az vm identity show --resource-group <rg> --name <vm-name> --query 'principalId' --output tsv (or equivalent for other resource types). 2. Confirm the managed identity has been granted the correct Key Vault access policy by executing: az keyvault show --name <kv-name> --query 'properties.accessPolicies[?objectId==`<principalId>`]' --output json. 3. Test authentication by retrieving a secret using the managed identity: az keyvault secret show --name <secret-name> --vault-name <kv-name> --query 'value' --output tsv (this command must be run from the resource with the managed identity). 4. If using a service principal, verify the service principal exists: az ad sp show --id <app-id> --query 'objectId' --output tsv. 5. Confirm the service principal has the required Azure RBAC role assignment on the key vault: az role assignment list --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.KeyVault/vaults/<kv-name> --assignee <objectId> --output json.

## Rollback
1. Remove the managed identity from the Azure resource: az vm identity remove --resource-group <rg> --name <vm-name> (or equivalent for other resource types). 2. Delete the access policy for the managed identity from the key vault: az keyvault delete-policy --name <kv-name> --object-id <principalId>. 3. If a service principal was created, delete it: az ad sp delete --id <app-id>. 4. Remove any Azure RBAC role assignments for the service principal on the key vault: az role assignment delete --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.KeyVault/vaults/<kv-name> --assignee <objectId> --role '<role-name>'.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
