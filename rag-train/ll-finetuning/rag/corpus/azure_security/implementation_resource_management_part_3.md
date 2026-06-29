# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
How to retrieve a specific management lock for a resource using Python SDK?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Requires Azure CLI authentication and ManagementLockClient

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. import os
2. from azure.identity import AzureCliCredential
3. from azure.mgmt.resource import ManagementLockClient
4. credential = AzureCliCredential()
5. subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
6. lock_client = ManagementLockClient(credential, subscription_id)
7. lock_result = lock_client.management_locks.get_at_resource_level(
8. "exampleGroup",
9. "Microsoft.Web",
10. "",
11. "sites",
12. "examplesite",
13. "lockSite"
14. )
15. print(f"Lock ID: {lock_result.id}")
16. print(f"Lock Name: {lock_result.name}")
17. print(f"Lock Level: {lock_result.level}")

## Validation
1. Run the Python script to retrieve the management lock. 2. Verify the output prints the lock ID, name, and level. 3. Confirm the lock level matches the expected value (e.g., 'CanNotDelete' or 'ReadOnly'). 4. Optionally, run 'az lock list --resource-group exampleGroup --resource-name examplesite --resource-type Microsoft.Web/sites' to cross-check the lock details.

## Rollback
1. If the script fails due to missing environment variable, set AZURE_SUBSCRIPTION_ID using 'export AZURE_SUBSCRIPTION_ID="<subscription-id>"' (Linux/macOS) or '$env:AZURE_SUBSCRIPTION_ID="<subscription-id>"' (PowerShell). 2. If authentication fails, re-authenticate using 'az login'. 3. If the lock does not exist, verify the resource group, resource name, and lock name are correct; no rollback needed as retrieval is read-only.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
