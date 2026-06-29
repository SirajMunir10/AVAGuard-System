# Troubleshooting: Key Vault (HTTP 401)

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot HTTP 401: Unauthenticated Request errors when accessing Azure Key Vault?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- HTTP 401: Unauthenticated Request

## Error Codes
- `HTTP 401`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Run 'az keyvault list --query "[].name" -o tsv' to list all key vaults in the subscription. 2. For each key vault, run 'az keyvault show --name <vault-name> --query "properties.accessPolicies[].objectId" -o tsv' to verify the caller's object ID is present. 3. Execute 'az ad signed-in-user show --query objectId -o tsv' to confirm the signed-in user's object ID. 4. Compare the user's object ID against the access policy list; if missing, the policy must be added. 5. Run 'az keyvault test-vm-access --name <vault-name> --resource-group <rg-name> --vm-name <vm-name>' to test VM access if applicable. 6. Check network rules with 'az keyvault network-rule list --name <vault-name> --resource-group <rg-name>' to ensure the client IP is allowed.

## Rollback
1. If an access policy was added incorrectly, remove it using 'az keyvault delete-policy --name <vault-name> --object-id <object-id>'. 2. If a network rule was added, remove it with 'az keyvault network-rule remove --name <vault-name> --resource-group <rg-name> --ip-address <ip-address>'. 3. If a managed identity was assigned to a resource, remove it via 'az vm identity remove --name <vm-name> --resource-group <rg-name>'. 4. If a firewall was enabled, disable it with 'az keyvault update --name <vault-name> --resource-group <rg-name> --default-action Allow'. 5. If a private endpoint was created, delete it using 'az network private-endpoint delete --name <pe-name> --resource-group <rg-name>'.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
