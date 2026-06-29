# Implementation: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Purview, the Data Map shows no assets even though I have scanned an Azure Data Lake Storage Gen2 account. The scan runs successfully but returns zero assets. What is the most likely cause and how do I fix it?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Purview account with a single collection, Azure Data Lake Storage Gen2 as a data source, system-assigned managed identity enabled, and a scan rule set that includes all file types.

## Symptoms
- Scan of Azure Data Lake Storage Gen2 completes with status 'Completed' but reports 0 assets discovered.
- No assets appear in the Purview Data Map under the scanned collection.
- No errors are logged in the scan history or in the Azure resource logs for the Purview account.

## Error Codes
N/A

## Root Causes
1. The managed identity of the Purview account does not have the required Azure RBAC role (e.g., 'Storage Blob Data Reader') on the storage account, or the storage account's firewall settings block access from the Purview managed identity.
2. The scan rule set is configured to exclude all file types or the scan scope is set to an empty path.

## Remediation Steps
1. Verify that the Purview system-assigned managed identity has the 'Storage Blob Data Reader' role on the Azure Data Lake Storage Gen2 account. If not, assign it via Azure Portal or Azure CLI: `az role assignment create --assignee <purview-msi-object-id> --role 'Storage Blob Data Reader' --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Storage/storageAccounts/<account>`.
2. If the storage account has a firewall enabled, add the Purview managed identity as an exception under 'Firewalls and virtual networks' -> 'Resource instances' -> add the Purview account's resource ID.
3. Check the scan rule set: ensure it includes the file types present in the storage account (e.g., .csv, .parquet). If using a custom rule set, verify it is not empty.
4. Re-run the scan after applying the above changes.

## Validation
After remediation, re-run the scan and confirm that the Data Map shows the expected assets (e.g., folders and files). The scan history should show a non-zero asset count.

## Rollback
Remove the role assignment or firewall exception if the scan was previously working and the change caused unintended access.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-scans#scan-completes-but-no-assets-are-discovered>
