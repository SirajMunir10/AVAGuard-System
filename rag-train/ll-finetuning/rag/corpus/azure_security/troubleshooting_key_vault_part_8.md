# Troubleshooting: Key Vault (HTTP 429)

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot HTTP 429: Too Many Requests errors when accessing Azure Key Vault?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- HTTP 429: Too Many Requests

## Error Codes
- `HTTP 429`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Check the Key Vault request logs in Azure Monitor to confirm that the number of requests per second is within the service limits. Use the following KQL query in Log Analytics:
   AzureDiagnostics
   | where ResourceType == "VAULTS" and Category == "AuditEvent"
   | summarize RequestCount = count() by bin(TimeGenerated, 1m)
   | where RequestCount > 1000
   (Note: The default limit is 2000 requests per second per vault, but this may vary based on your vault's configuration.)
2. Verify that the client application is using retry logic with exponential backoff. Check application logs for retry attempts and delays.
3. Confirm that the Key Vault firewall and network settings are correctly configured to allow the client's IP address or virtual network.
4. Use the Azure CLI command to check the current throttling status:
   az keyvault show --name <vault-name> --query "properties.throttlingState"
   (Expected output: "enabled" or "disabled" – if enabled, throttling is active.)

## Rollback
1. If the remediation involved increasing the Key Vault request limit (which is not directly configurable), revert any changes to client-side retry logic to the original implementation.
2. If network or firewall rules were modified, restore the previous rules using Azure CLI:
   az keyvault update --name <vault-name> --default-action Deny
   (If the original setting was Deny, reapply it; if it was Allow, set it back.)
3. If the client application was modified to reduce request rate, revert the code changes and redeploy the previous version.
4. If the issue persists after rollback, consider distributing requests across multiple Key Vaults or using a caching layer to reduce direct calls.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
