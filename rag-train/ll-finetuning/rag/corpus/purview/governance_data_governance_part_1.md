# Governance: Data Governance

**Domain:** Purview
**Subdomain:** Data Governance
**Incident Type:** Governance

## Scenario / Query
A Microsoft Purview Data Map administrator notices that newly registered Azure SQL Database sources are not appearing in the Purview Data Catalog after scanning. The scan runs successfully but no assets are ingested. What is the likely cause and how should it be remediated?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Purview Data Map with managed virtual network enabled; Azure SQL Database with firewall rules restricting access to Azure services

## Symptoms
- Scan of Azure SQL Database completes with status 'Succeeded' but zero assets ingested
- No error or warning messages in the scan history
- Data source appears in the Purview Data Map but no tables or views are cataloged

## Error Codes
N/A

## Root Causes
1. The Azure SQL Database firewall is not configured to allow access from the Purview managed virtual network. Even though the scan status shows success, connectivity failures during metadata extraction cause zero assets to be ingested.

## Remediation Steps
1. 1. In the Azure portal, navigate to the Azure SQL Database resource.
2. 2. Under 'Security', select 'Networking' and then 'Firewall rules'.
3. 3. Add a firewall rule with the start and end IP addresses of the Purview managed virtual network (found in Purview Management Center > Managed virtual networks).
4. 4. Alternatively, enable 'Allow Azure services and resources to access this server' if the Purview managed virtual network is not used.
5. 5. Re-run the scan from the Purview Data Map.

## Validation
After applying the firewall rule, re-run the scan. Confirm that assets (tables, views) appear in the Purview Data Catalog.

## Rollback
Remove the added firewall rule from the Azure SQL Database networking settings.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-scans#scan-succeeds-but-no-assets-are-ingested>
