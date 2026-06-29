# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
How to list all management locks at the subscription level using Python SDK?

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
7. lock_result = lock_client.management_locks.list_at_subscription_level()
8. for lock in lock_result:
9. print(f"Lock name: {lock.name}")
10. print(f"Lock level: {lock.level}")
11. print(f"Lock notes: {lock.notes}")

## Validation
Run the Python script provided in the remediation steps. Confirm that it prints the name, level, and notes for each management lock at the subscription level without errors. Additionally, verify that the output matches the locks visible via Azure CLI command: az lock list --subscription $AZURE_SUBSCRIPTION_ID --output table

## Rollback
If the script fails, ensure the environment variable AZURE_SUBSCRIPTION_ID is set correctly. Re-authenticate with Azure CLI using 'az login' and set the correct subscription with 'az account set --subscription <subscription-id>'. If the ManagementLockClient import fails, install the required package with 'pip install azure-mgmt-resource'. No changes are made to Azure resources, so no further rollback is needed.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
