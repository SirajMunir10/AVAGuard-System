# Implementation: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Purview, the Data Map shows no assets from an Azure SQL Database that was registered as a data source. The collection is configured, and the scan rule set is the default 'AzureSQL' system rule. What is the most likely cause and how do you resolve it?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Purview account with System-assigned managed identity, Azure SQL Database with firewall enabled, default scan rule set applied, collection path set to root collection.

## Symptoms
- Azure SQL Database appears in the Purview Data Map as a registered source but shows zero assets after a full scan completes with status 'Succeeded'.
- No tables or views are visible under the database node in the Purview governance portal.

## Error Codes
N/A

## Root Causes
1. The Purview system-assigned managed identity (or user-assigned managed identity) has not been granted the necessary SQL permissions (e.g., db_datareader) on the Azure SQL Database.
2. The Azure SQL Database firewall is blocking connections from Purview's managed identity because the 'Allow Azure services and resources to access this server' setting is disabled.

## Remediation Steps
1. 1. In the Azure portal, navigate to the Azure SQL Server (logical server) that hosts the database.
2. 2. Under 'Security' > 'Firewalls and virtual networks', set 'Allow Azure services and resources to access this server' to 'Yes'.
3. 3. Connect to the Azure SQL Database using SQL Server Management Studio or Azure Data Studio with an account that has the AAD admin role.
4. 4. Run the following T-SQL command to grant the Purview managed identity the db_datareader role (replace 'Purview-MSI-Name' with the actual managed identity name from Purview > Managed identities):
5. CREATE USER [Purview-MSI-Name] FROM EXTERNAL PROVIDER;
6. ALTER ROLE db_datareader ADD MEMBER [Purview-MSI-Name];
7. 5. Re-run the scan from the Purview governance portal.

## Validation
After applying the firewall rule and granting db_datareader, re-trigger a full scan of the Azure SQL Database. Confirm that the Data Map now populates with the expected tables and views.

## Rollback
Remove the firewall exception by setting 'Allow Azure services and resources to access this server' back to 'No' and drop the database user created for the managed identity using DROP USER [Purview-MSI-Name].

## References
- <https://learn.microsoft.com/en-us/purview/register-scan-azure-sql-database>
