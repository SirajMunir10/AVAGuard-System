# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I configure the Storage tab when creating a Logic App for a Microsoft Sentinel playbook?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Logic App Standard workflow creation in Azure portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Storage tab, provide the following information: For Storage type, select Azure Storage, and create or select a storage account.
2. For Blob service diagnostic settings, leave the default setting.

## Validation
1. In the Azure portal, navigate to the Logic App resource you created. 2. Under 'Settings', select 'Configuration'. 3. Verify that 'Storage type' is set to 'Azure Storage' and that a valid storage account is associated. 4. Under 'Diagnostic settings', confirm that 'Blob service' diagnostic settings are set to the default (i.e., not explicitly configured to a custom setting). 5. Optionally, run the Azure CLI command: az logicapp show --name <logic-app-name> --resource-group <resource-group-name> --query 'properties.configuration.storage' to confirm the storage configuration.

## Rollback
1. In the Azure portal, navigate to the Logic App resource. 2. Under 'Settings', select 'Configuration'. 3. Change 'Storage type' back to the previous setting (e.g., 'None' or another storage type if previously configured). 4. If a different storage account was previously used, select that account instead. 5. Reset 'Blob service diagnostic settings' to the previous custom setting if one was applied. 6. Alternatively, use the Azure CLI: az logicapp config storage set --name <logic-app-name> --resource-group <resource-group-name> --storage-type <previous-type> --storage-account <previous-account>.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
