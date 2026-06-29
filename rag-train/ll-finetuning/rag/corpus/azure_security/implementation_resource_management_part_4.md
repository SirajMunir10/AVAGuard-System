# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
How to delete a management lock for a resource using Python SDK?

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
7. lock_client.management_locks.delete_at_resource_level(
8. "exampleGroup",
9. "Microsoft.Web",
10. "",
11. "sites",
12. "examplesite",
13. "lockSite"
14. )

## Validation
Run the following Python script to confirm the management lock has been deleted:

```python
import os
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ManagementLockClient

credential = AzureCliCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
lock_client = ManagementLockClient(credential, subscription_id)

# Attempt to get the lock; if deleted, this will raise an exception or return None
try:
    lock = lock_client.management_locks.get_at_resource_level(
        "exampleGroup",
        "Microsoft.Web",
        "",
        "sites",
        "examplesite",
        "lockSite"
    )
    print("Lock still exists:", lock.name)
except Exception as e:
    if "NotFound" in str(e) or "ResourceNotFound" in str(e):
        print("Lock successfully deleted.")
    else:
        print("Unexpected error:", e)
```

Alternatively, use Azure CLI to verify:
```bash
az lock list --resource-group exampleGroup --resource-name examplesite --resource-type Microsoft.Web/sites --query "[?name=='lockSite']" --output none
```
If the lock is deleted, the command returns no output.

## Rollback
To recreate the deleted management lock, run the following Python script:

```python
import os
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ManagementLockClient
from azure.mgmt.resource.models import ManagementLockObject, ManagementLockOwner

credential = AzureCliCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
lock_client = ManagementLockClient(credential, subscription_id)

lock_properties = ManagementLockObject(
    level="CanNotDelete",  # or "ReadOnly" as needed
    notes="Recreated after rollback"
)

lock_client.management_locks.create_or_update_at_resource_level(
    "exampleGroup",
    "Microsoft.Web",
    "",
    "sites",
    "examplesite",
    "lockSite",
    lock_properties
)
print("Lock recreated.")
```

Or use Azure CLI:
```bash
az lock create --name lockSite --resource-group exampleGroup --resource-name examplesite --resource-type Microsoft.Web/sites --lock-type CanNotDelete
```

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
