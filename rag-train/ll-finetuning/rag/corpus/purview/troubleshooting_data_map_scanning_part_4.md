# Troubleshooting: Data Map â€“ Scanning (403 Forbidden)

**Domain:** Purview
**Subdomain:** Data Map â€“ Scanning
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Purview scan of an Azure SQL Database fails with error 'System.AggregateException: One or more errors occurred. (The remote server returned an error: (403) Forbidden.)' How do I resolve this?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure SQL Database with Purview managed identity authentication, firewall enabled, and no private endpoint configured.

## Symptoms
- Scan status shows 'Failed' with error message 'System.AggregateException: One or more errors occurred. (The remote server returned an error: (403) Forbidden.)'
- No data assets are discovered from the Azure SQL Database.

## Error Codes
- `403 Forbidden`

## Root Causes
1. The Purview managed identity (or service principal) does not have the necessary Azure RBAC role (e.g., 'SQL DB Contributor') on the Azure SQL Database resource.
2. The Azure SQL Database firewall rules do not allow the Purview managed identity IP range or the 'Allow Azure services and resources to access this server' setting is disabled.

## Remediation Steps
1. 1. In the Azure portal, navigate to the Azure SQL Server that hosts the database. Under 'Security', select 'Firewalls and virtual networks'.
2. 2. Set 'Allow Azure services and resources to access this server' to 'Yes'.
3. 3. Assign the 'SQL DB Contributor' role to the Purview managed identity at the Azure SQL Server scope. (Alternatively, use a system-assigned managed identity and grant it the necessary permissions via RBAC.)
4. 4. If using a user-assigned managed identity, ensure the identity is assigned to the Purview account and has the same permissions.
5. 5. Re-run the scan from the Purview governance portal.

## Validation
After applying the firewall rule and RBAC role, the scan completes successfully and data assets appear in the Purview Data Map.

## Rollback
Remove the firewall exception and revoke the RBAC role assignment if the scan is no longer needed.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-azure-sql-database-scanning>
