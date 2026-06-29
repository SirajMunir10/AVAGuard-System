# Troubleshooting: Key Vault

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Access to this page requires authorization' error when accessing Azure Key Vault?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access to this page requires authorization

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Open a private/incognito browser session and navigate to the Azure portal (https://portal.azure.com).
2. Sign in with the user account that previously received the 'Access to this page requires authorization' error.
3. In the Azure portal, go to 'Key Vaults' and select the specific vault that was inaccessible.
4. Click on 'Secrets', 'Keys', or 'Certificates' under 'Objects' to verify that the vault contents are now accessible without the authorization error.
5. Alternatively, use Azure CLI: run 'az keyvault secret list --vault-name <vault-name>' (replace <vault-name> with the actual vault name) and confirm it returns the list of secrets without an authorization error.

## Rollback
1. If the user still receives the 'Access to this page requires authorization' error after signing in, instruct the user to sign out of the current session.
2. Clear the browser cache and cookies, or use a different browser/private window.
3. Sign in again with the correct user account that has appropriate permissions (e.g., Key Vault Reader, Key Vault Secrets User) assigned via Azure RBAC or vault access policy.
4. If the error persists, verify the user's directory context: in the Azure portal top bar, click the 'Directory + subscription' filter icon and ensure the correct directory (tenant) is selected.
5. If the directory was incorrect, switch to the correct directory and retry accessing the Key Vault.
6. If the issue remains, refer to the official troubleshooting guide at https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues for further steps.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
