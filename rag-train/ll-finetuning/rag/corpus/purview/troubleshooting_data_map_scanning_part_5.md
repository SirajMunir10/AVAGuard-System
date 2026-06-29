# Troubleshooting: Data Map / Scanning (18456)

**Domain:** Purview
**Subdomain:** Data Map / Scanning
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Purview scan of an Azure SQL Database fails with 'Login failed for user' even though the credential and system-assigned managed identity appear correctly configured. How do I resolve this?

## Environment Context
- **Tenant Type:** Enterprise (Azure + Microsoft Purview)
- **Configuration:** Purview managed identity (system-assigned) used for scanning; Azure SQL Database firewall enabled for Azure services; credential created in Purview with SQL authentication.

## Symptoms
- Scan status shows 'Failed' with error message 'Login failed for user'.
- No changes have been made to the SQL Database firewall or user permissions recently.
- The managed identity is enabled and appears in the Azure portal under Purview > Identity.

## Error Codes
- `18456`

## Root Causes
1. The SQL Database login for the Purview managed identity does not exist or has insufficient permissions.
2. The Purview credential uses a SQL authentication login that does not match the managed identity or is not granted the 'db_datareader' role.

## Remediation Steps
1. 1. In Azure SQL Database, create a login for the Purview managed identity using the T-SQL command: `CREATE USER [Purview-MSI-Name] FROM EXTERNAL PROVIDER;` (where Purview-MSI-Name is the name of the Purview system-assigned managed identity).
2. 2. Add the user to the `db_datareader` role: `ALTER ROLE db_datareader ADD MEMBER [Purview-MSI-Name];`.
3. 3. If using a SQL authentication credential instead, ensure the login exists in the master database and the user has `db_datareader` on each database to be scanned.
4. 4. Re-run the scan from the Purview governance portal.

## Validation
Run a test scan on a single table; confirm the scan completes successfully and data appears in the Purview Data Map.

## Rollback
Drop the user created for the managed identity: `DROP USER IF EXISTS [Purview-MSI-Name];` and remove any role memberships.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-scanning>
