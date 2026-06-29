# Implementation: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Purview, the Data Map shows no assets even though the scan rule set appears correctly configured and the scan ran successfully. What is the most likely cause and how do you resolve it?

## Environment Context
- **Tenant Type:** Enterprise (multi-subscription)
- **Configuration:** Purview account with managed event hub; scan rule set includes all system types; scan registration uses a managed identity with Reader and Data Reader roles on the source subscription.

## Symptoms
- Scan completes with status 'Succeeded' but zero assets are ingested into the Data Map.
- No error messages appear in the scan history or Azure Activity log.
- The collection hierarchy is empty under the root collection.

## Error Codes
N/A

## Root Causes
1. The managed identity used by the Purview account does not have the required 'Reader' and 'Storage Blob Data Reader' roles on the Azure Data Lake Storage Gen2 account or other data source.
2. The data source registration is pointing to a storage account that is in a different Azure region than the Purview account, and cross-region scanning is not supported for that source type.

## Remediation Steps
1. Verify that the Purview managed identity has the 'Reader' role on the subscription or resource group containing the data source, and the 'Storage Blob Data Reader' role on the specific storage account. This is documented in 'Microsoft Purview permissions' at https://learn.microsoft.com/en-us/azure/purview/how-to-access-policies-storage.
2. If the data source is in a different region, either move the data source to the same region as Purview or use a supported cross-region scanning configuration (only available for certain source types like Azure SQL Database). See 'Supported data sources and file types in Microsoft Purview' at https://learn.microsoft.com/en-us/azure/purview/sources-and-scans.

## Validation
Re-run the scan after correcting permissions. Confirm that the Data Map now shows the expected assets under the correct collection.

## Rollback
Remove the incorrect role assignments added during troubleshooting. If the data source was moved, restore it to its original region.

## References
- <https://learn.microsoft.com/en-us/azure/purview/how-to-access-policies-storage>
- <https://learn.microsoft.com/en-us/azure/purview/sources-and-scans>
