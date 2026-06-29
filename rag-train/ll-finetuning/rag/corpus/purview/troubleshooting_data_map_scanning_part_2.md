# Troubleshooting: Data Map / Scanning (Login failed for user '<token-identified principal>')

**Domain:** Purview
**Subdomain:** Data Map / Scanning
**Incident Type:** Troubleshooting

## Scenario / Query
A customer reports that after registering an Azure SQL Database as a data source in Microsoft Purview, the scan fails with status 'Failed' and no assets are discovered. How should the administrator troubleshoot and resolve this issue?

## Environment Context
- **Tenant Type:** Enterprise (Azure + Purview)
- **Configuration:** Azure SQL Database registered in Purview Data Map; scan rule set uses default 'Azure SQL Database' scan rule; managed identity authentication enabled for the Purview account.

## Symptoms
- Scan run shows status 'Failed' in Purview Studio
- No assets (tables/views) appear in the Data Map after scan completion
- Scan history shows error: 'Login failed for user' or 'Cannot open server'

## Error Codes
- `Login failed for user '<token-identified principal>'`
- `Cannot open server '<server-name>' requested by the login. Login failed.`

## Root Causes
1. The Purview managed identity has not been granted the necessary database permissions (e.g., db_datareader) on the Azure SQL Database.
2. The Azure SQL Database firewall is blocking the Purview managed identity IP range (if using public endpoint).
3. The Purview account's managed identity is not enabled or is misconfigured.

## Remediation Steps
1. 1. In Azure portal, navigate to the Azure SQL Server logical server, select 'Azure Active Directory admin' and set the Purview managed identity as an Azure AD admin (or grant it db_datareader role on the specific database).
2. 2. Connect to the Azure SQL Database using SQL Server Management Studio or Azure Data Studio and run: CREATE USER [<Purview-managed-identity-name>] FROM EXTERNAL PROVIDER; ALTER ROLE db_datareader ADD MEMBER [<Purview-managed-identity-name>];
3. 3. If using public endpoint, add a firewall rule on the Azure SQL Server to allow the Purview managed identity's outbound IP range (see Microsoft documentation for Purview IP ranges).
4. 4. In Purview Management Center, under 'Data sources', edit the Azure SQL Database data source and ensure 'Authentication method' is set to 'Managed Identity'.
5. 5. Re-run the scan from Purview Studio.

## Validation
After remediation, re-run the scan and confirm it completes with status 'Completed' and that tables/views appear in the Data Map.

## Rollback
If the issue persists, revert the firewall rule or database user creation by removing the added user and firewall rule, then re-evaluate network connectivity and permissions.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-azure-sql-database-scanning>
