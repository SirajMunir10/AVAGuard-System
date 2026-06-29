# Troubleshooting: Key Vault

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
I'm not able to list or get secrets/keys/certificate. I'm seeing a 'something went wrong' error

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Unable to list or get secrets/keys/certificate
- Seeing a 'something went wrong' error

## Error Codes
N/A

## Root Causes
1. Missing appropriate Azure RBAC role assignment
2. Missing appropriate Key Vault access policy (legacy model)

## Remediation Steps
1. Ensure you have the appropriate Azure RBAC role assigned. See Azure RBAC for Key Vault.
2. If using the legacy access policy model, assign a Key Vault access policy. See Assign a Key Vault access policy.

## Validation
1. Run 'az role assignment list --assignee <user-or-service-principal-object-id> --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<vault-name>' to confirm the user or service principal has a role like 'Key Vault Secrets User' (for secrets) or 'Key Vault Reader' (for listing).
2. Run 'az keyvault show --name <vault-name>' and check the 'properties.accessPolicies' array to confirm the user or service principal has an access policy with at least 'get' and 'list' permissions for secrets, keys, and certificates.
3. Run 'az keyvault secret list --vault-name <vault-name>' and 'az keyvault secret show --vault-name <vault-name> --name <test-secret-name>' to verify listing and getting a secret succeed without error.

## Rollback
1. Remove the Azure RBAC role assignment: 'az role assignment delete --assignee <user-or-service-principal-object-id> --role "Key Vault Secrets User" --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<vault-name>' (or the specific role assigned).
2. Remove the Key Vault access policy: 'az keyvault delete-policy --name <vault-name> --object-id <user-or-service-principal-object-id>'.
3. Re-test by running 'az keyvault secret list --vault-name <vault-name>' and confirm the original 'something went wrong' error returns.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
