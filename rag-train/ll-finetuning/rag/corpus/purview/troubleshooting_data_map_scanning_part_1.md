# Troubleshooting: Data Map / Scanning (The underlying provider failed on Open.)

**Domain:** Purview
**Subdomain:** Data Map / Scanning
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Purview scan of an Azure SQL Database fails with the error 'The underlying provider failed on Open.' How do I resolve this?

## Environment Context
- **Tenant Type:** Enterprise (Azure + Microsoft Purview)
- **Configuration:** Purview managed virtual network enabled; Azure SQL Database firewall configured to allow Azure services; scan credential uses SQL authentication.

## Symptoms
- Scan status shows 'Failed' with message 'The underlying provider failed on Open.'
- No connectivity errors from other Azure services to the same SQL Database.

## Error Codes
- `The underlying provider failed on Open.`

## Root Causes
1. The Purview managed virtual network's private endpoint or service endpoint is not correctly configured for the Azure SQL Database.
2. The SQL Database firewall does not include the Purview managed VNet's IP range or the private endpoint's subnet.
3. The SQL authentication credential used in the scan has insufficient permissions or the password has expired.

## Remediation Steps
1. Verify that the Azure SQL Database firewall allows connections from the Purview managed VNet's private endpoint IP address or the Azure service tag 'Sql.management' if using service endpoints. See 'Configure Azure SQL Database firewall for Purview scans' in the official documentation.
2. Ensure the credential used for the scan has the correct SQL login and password, and that the login has at least db_datareader role on the database(s) being scanned.
3. If using a private endpoint, confirm that the private endpoint is in the 'Approved' state and that the DNS resolution for the SQL server name resolves to the private IP address.
4. Re-run the scan after applying the above changes.

## Validation
After remediation, the scan should complete successfully. You can also test connectivity by running a test connection from the Purview governance portal for the data source.

## Rollback
If changes to firewall rules or credentials cause other connectivity issues, revert the firewall rules to the previous state and restore the original credential. If a private endpoint was modified, delete and recreate it with the original configuration.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-azure-sql-database-scanning>
