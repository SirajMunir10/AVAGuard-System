# Troubleshooting: Key Vault (Unknown Policy)

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
I'm seeing 'Unknown Policy' error. What does that mean?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access policy appears in the Unknown section

## Error Codes
- `Unknown Policy`

## Root Causes
1. A previous user had access but that user no longer exists
2. The access policy was added through PowerShell, using the application objectid instead of the service principal

## Remediation Steps
N/A

## Validation
1. Run 'az keyvault show --name <vault-name> --query "properties.accessPolicies[?objectId==`<objectId>`]"' to confirm the policy is no longer listed in the Unknown section.
2. Verify that the correct service principal exists: 'az ad sp show --id <objectId>' should return a valid service principal.
3. Check that the access policy now appears under the correct principal: 'az keyvault show --name <vault-name> --query "properties.accessPolicies[?objectId==`<correct-objectId>`]"'.

## Rollback
1. If the remediation fails, restore the original access policy using the application object ID: 'az keyvault set-policy --name <vault-name> --object-id <original-objectId> --permissions <original-permissions>'.
2. If the policy was removed, re-add it with the same permissions: 'az keyvault set-policy --name <vault-name> --object-id <objectId> --key-permissions <keys> --secret-permissions <secrets> --certificate-permissions <certificates>'.
3. Verify the policy is restored: 'az keyvault show --name <vault-name> --query "properties.accessPolicies"'.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
