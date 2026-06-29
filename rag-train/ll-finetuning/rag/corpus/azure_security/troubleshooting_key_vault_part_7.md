# Troubleshooting: Key Vault (HTTP 403)

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot HTTP 403: Insufficient Permissions errors when accessing Azure Key Vault?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- HTTP 403: Insufficient Permissions

## Error Codes
- `HTTP 403`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Run 'az keyvault show --name <vault-name> --query "properties.accessPolicies"' to confirm the access policy includes the user or service principal with required permissions (e.g., get, list).
2. Run 'az role assignment list --assignee <user-or-spn-object-id> --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.KeyVault/vaults/<vault-name>' to verify the RBAC role assignment (e.g., Key Vault Secrets User) if using RBAC permission model.
3. Attempt a test operation: 'az keyvault secret list --vault-name <vault-name>' and confirm it returns secrets without 403 error.
4. Check the Key Vault firewall settings: 'az keyvault show --name <vault-name> --query "properties.networkAcls"' to ensure the client IP or virtual network is allowed.

## Rollback
1. If access policy was added, remove it: 'az keyvault delete-policy --name <vault-name> --object-id <object-id>'.
2. If RBAC role assignment was added, remove it: 'az role assignment delete --assignee <user-or-spn-object-id> --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.KeyVault/vaults/<vault-name> --role "Key Vault Secrets User"'.
3. If firewall rule was added, remove the IP rule: 'az keyvault update --name <vault-name> --default-action Deny --remove networkAcls.ipRules <ip-rule-index>' or restore previous firewall configuration.
4. Revert any other configuration changes made during remediation to the original state.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
