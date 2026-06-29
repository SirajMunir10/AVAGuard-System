# Troubleshooting: Data Map / Scanning

**Domain:** Purview
**Subdomain:** Data Map / Scanning
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Purview scan of an Azure SQL Database fails with the error 'Scan setup failed: The underlying connection was closed: An unexpected error occurred on a send.' How do I resolve this?

## Environment Context
- **Tenant Type:** Enterprise (Azure subscription with Purview account)
- **Configuration:** Purview managed virtual network (VNet) enabled; Azure SQL Database firewall configured to allow Azure services; scan uses system-assigned managed identity

## Symptoms
- Scan status shows 'Failed' with message 'Scan setup failed'
- Underlying error: 'The underlying connection was closed: An unexpected error occurred on a send.'
- No connectivity issues from other Azure services to the same SQL Database

## Error Codes
N/A

## Root Causes
1. The Purview managed VNet does not have outbound connectivity to the Azure SQL Database endpoint, or the SQL Database firewall is blocking the Purview managed identity's IP range.
2. The TLS version required by the SQL Database is not supported by the Purview runtime environment.

## Remediation Steps
1. 1. Verify that the Azure SQL Database firewall rule includes the Purview managed VNet's IP range. In the Azure portal, navigate to the SQL server, select 'Networking', and under 'Firewall rules', add a rule with the start and end IP of the Purview managed VNet subnet (found in Purview > Managed VNets).
2. 2. If using a private endpoint, ensure the private DNS zone for the SQL server is correctly linked to the Purview managed VNet.
3. 3. Confirm that the Purview managed identity has been granted the necessary permissions on the SQL Database (e.g., db_datareader role).
4. 4. If the error persists, check that the SQL Database is configured to accept TLS 1.2 connections (Purview runtime uses TLS 1.2). In the SQL server's 'Connection security' blade, set 'Minimum TLS version' to 1.2.

## Validation
Rerun the scan. If successful, the status will change to 'In Progress' and eventually 'Completed'.

## Rollback
Remove any added firewall rules or revert TLS version changes if they cause other connectivity issues.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-azure-sql-database-scanning>
