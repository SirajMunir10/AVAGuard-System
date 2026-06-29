# Implementation: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Purview, the Data Map shows no assets even though the scan rule set includes the entire Azure Storage account. What configuration step was missed?

## Environment Context
- **Tenant Type:** Enterprise (Azure subscription with multiple resource groups)
- **Configuration:** Purview account deployed with system-assigned managed identity; scan rule set configured to scan all blob containers in a storage account; collection hierarchy uses default root collection.

## Symptoms
- Scan registration succeeds but no assets appear in the Data Map
- Scan status shows 'Completed' with 0 assets scanned
- No errors in the scan history or Azure Activity log

## Error Codes
N/A

## Root Causes
1. The Purview managed identity was not granted the required 'Storage Blob Data Reader' role on the storage account, preventing the scanner from enumerating or reading blob metadata.

## Remediation Steps
1. Navigate to the Azure Storage account in the Azure portal.
2. Select 'Access Control (IAM)' and then 'Add role assignment'.
3. Assign the 'Storage Blob Data Reader' role to the Purview system-assigned managed identity (or user-assigned identity if configured).
4. Wait up to 15 minutes for role propagation, then re-run the scan from the Purview governance portal.

## Validation
Confirm that the managed identity appears in the storage account's role assignments with the 'Storage Blob Data Reader' role. Re-run the scan and verify that assets populate in the Data Map.

## Rollback
Remove the role assignment from the storage account's IAM blade. Note: This will cause future scans to fail with zero assets.

## References
- <https://learn.microsoft.com/en-us/azure/purview/concept-best-practices-scanning#configure-azure-storage-permissions>
