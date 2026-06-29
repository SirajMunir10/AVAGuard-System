# Implementation: Data Map â€“ Collection Hierarchy

**Domain:** Purview
**Subdomain:** Data Map â€“ Collection Hierarchy
**Incident Type:** Implementation

## Scenario / Query
A customer is deploying Microsoft Purview and cannot register an Azure SQL Database as a data source. The 'Register' button is grayed out, and the user has Global Administrator and Purview Data Source Administrator roles. What is the likely cause and how should the collection hierarchy be configured to enable registration?

## Environment Context
- **Tenant Type:** Enterprise (E5)
- **Configuration:** Purview account created with system-assigned managed identity; no collection hierarchy defined; user assigned Purview Data Source Administrator at root collection.

## Symptoms
- Register button for Azure SQL Database is disabled in the Purview governance portal.
- No error message is displayed; the UI simply prevents registration.
- User has both Global Administrator and Purview Data Source Administrator roles.

## Error Codes
N/A

## Root Causes
1. No collection has been created under the root collection. In Purview, data sources must be registered under a collection, and the root collection alone cannot host data sources.
2. The user has not been assigned the Data Source Administrator role at the specific collection where the source would be registered, or the collection does not exist.

## Remediation Steps
1. 1. In the Purview governance portal, navigate to Data Map â†’ Collections.
2. 2. Create at least one sub-collection under the root collection (e.g., 'Production').
3. 3. Assign the user the 'Data Source Administrator' role on that sub-collection.
4. 4. Refresh the portal and attempt to register the Azure SQL Database under the new collection.

## Validation
After creating the sub-collection and assigning the role, the Register button should become active. The user should be able to complete the registration wizard.

## Rollback
Delete the sub-collection and remove role assignments. The root collection will remain, but no data sources can be registered until a new sub-collection is created.

## References
- <https://learn.microsoft.com/en-us/purview/manage-data-sources?tabs=azure-portal#prerequisites>
- <https://learn.microsoft.com/en-us/purview/register-scan-azure-sql-database>
