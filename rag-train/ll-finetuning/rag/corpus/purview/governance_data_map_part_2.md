# Governance: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Governance

## Scenario / Query
A Microsoft Purview administrator notices that newly scanned Azure SQL Database assets are not appearing in the Purview Data Map, even though the scan rule set includes the SQL Server type and the scan registration appears successful. What governance misconfiguration could cause this, and how can it be resolved?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD + Microsoft Purview)
- **Configuration:** Purview collection hierarchy with scan rule set assigned to a parent collection; Azure SQL Database registered as a data source in a child collection that does not inherit the scan rule set.

## Symptoms
- Scan registration completes without error but no assets are ingested
- Data Map shows zero assets for the scanned Azure SQL Database
- Scan history shows 'Completed' status with 0 assets scanned

## Error Codes
N/A

## Root Causes
1. The scan rule set is not assigned to the collection where the data source is registered, or inheritance is disabled on the child collection
2. The data source registration is in a collection that does not have a valid scan rule set applied

## Remediation Steps
1. Navigate to the Microsoft Purview governance portal, go to Data Map > Collections, and select the collection containing the data source
2. Under 'Scan rule sets', assign the appropriate scan rule set (e.g., 'AzureSQLDatabase') to that collection
3. Alternatively, ensure that the parent collection has the scan rule set assigned and that inheritance is enabled for the child collection
4. Re-run the scan for the affected data source

## Validation
After assigning the scan rule set to the correct collection and re-running the scan, verify that the expected Azure SQL Database assets appear in the Data Map under that collection.

## Rollback
Remove the scan rule set assignment from the collection, or disable inheritance, to revert to the previous state where assets were not ingested.

## References
- <https://learn.microsoft.com/en-us/purview/manage-scan-rule-sets>
