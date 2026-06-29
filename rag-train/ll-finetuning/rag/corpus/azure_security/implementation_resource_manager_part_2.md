# Implementation: Resource Manager

**Domain:** Azure
**Subdomain:** Resource Manager
**Incident Type:** Implementation

## Scenario / Query
How to apply a resource lock to a specific resource within a resource group using Bicep?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Bicep template with scope property set to resource name

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When applying a lock to a resource within the resource group, add the scope property.
2. Set the scope to the name of the resource to lock.
3. Example: create an app service plan, a website, and a lock on the website with the lock's scope set to the website.

## Validation
1. Deploy the Bicep template using: az deployment group create --resource-group <rg-name> --template-file <bicep-file>. 2. Verify the lock exists: az lock list --resource-group <rg-name> --resource-name <website-name> --resource-type Microsoft.Web/sites --query "[?name=='<lock-name>']" -o tsv. 3. Confirm the lock properties: az lock show --name <lock-name> --resource-group <rg-name> --resource-name <website-name> --resource-type Microsoft.Web/sites --query "{level:properties.level, notes:properties.notes}" -o tsv. 4. Attempt a write operation on the locked resource (e.g., az webapp update --name <website-name> --resource-group <rg-name> --set tags.test=value) and verify it fails with a conflict error.

## Rollback
1. Remove the lock: az lock delete --name <lock-name> --resource-group <rg-name> --resource-name <website-name> --resource-type Microsoft.Web/sites. 2. Verify deletion: az lock list --resource-group <rg-name> --resource-name <website-name> --resource-type Microsoft.Web/sites -o tsv. 3. If the lock was part of the Bicep deployment, redeploy the template without the lock resource or with the lock resource removed. 4. Confirm the resource is now writable: az webapp update --name <website-name> --resource-group <rg-name> --set tags.test=value (should succeed).

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
