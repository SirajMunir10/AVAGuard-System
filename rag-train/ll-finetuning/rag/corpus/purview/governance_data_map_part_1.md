# Governance: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Governance

## Scenario / Query
Why are assets in my Microsoft Purview Data Map not appearing in search results or lineage even though they were successfully scanned and registered?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Purview Data Map with automated scanning of Azure SQL Database and Azure Data Lake Storage Gen2; collection hierarchy configured with multiple sub-collections; scan rule sets use default system rule sets.

## Symptoms
- Assets are registered and scanned without errors in the Purview governance portal
- Search and browse in the Purview portal return no results for those assets
- Lineage tab for known assets shows no lineage information
- No error messages are displayed during scanning or registration

## Error Codes
N/A

## Root Causes
1. Assets are not assigned to a collection, or are assigned to a collection that the searching user does not have read permission on
2. The collection hierarchy is not properly configured, causing assets to be orphaned or invisible to users with default permissions

## Remediation Steps
1. Verify that each asset is assigned to at least one collection in the Purview Data Map
2. Ensure that the user or group performing the search has at least the 'Data Reader' role on the collection containing the assets
3. Review collection permissions and assign the appropriate roles (e.g., Data Reader, Data Curator) to users or groups via the Purview governance portal under 'Collections' > 'Role assignments'
4. If assets were scanned before collection assignment, reassign them by editing the asset properties in the Purview portal or by re-running the scan with a scan rule set that includes collection mapping

## Validation
After applying the remediation, the user should be able to search for the assets and see them in the search results. Additionally, the user should be able to view the asset details and lineage if applicable.

## Rollback
Remove the user from the Data Reader role on the collection to revert the permission change. If assets were reassigned to a different collection, reassign them back to the original collection.

## References
- <https://learn.microsoft.com/en-us/purview/manage-data-assets>
- <https://learn.microsoft.com/en-us/purview/create-manage-collections>
