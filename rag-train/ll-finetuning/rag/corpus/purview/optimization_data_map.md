# Optimization: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Optimization

## Scenario / Query
How can I optimize the performance of Microsoft Purview Data Map scanning by reducing the number of assets scanned in a data source without removing the data source registration?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Multiple Azure SQL databases registered in Purview Data Map with full scans scheduled daily

## Symptoms
- Scan jobs take longer than expected to complete
- High resource consumption on the data source during scans
- Scan completion times exceed the scheduled window

## Error Codes
N/A

## Root Causes
1. Scan rule sets are configured to scan all tables and views in the database, including those that are not needed for compliance or catalog purposes
2. No use of scan filters to exclude specific schemas or tables

## Remediation Steps
1. Create a custom scan rule set that includes only the tables and views required for your catalog
2. Apply a scan filter to exclude schemas or tables that are not needed (e.g., exclude 'dbo' schema if not required)
3. Re-run the scan with the optimized rule set and filter to verify reduced scan scope

## Validation
Confirm that the scan duration has decreased and that only the intended assets appear in the Purview Data Map catalog.

## Rollback
Revert to the default scan rule set and remove any custom scan filters. Re-run the scan to restore the previous scanning scope.

## References
- <https://learn.microsoft.com/en-us/purview/how-to-create-manage-scan-rule-sets>
