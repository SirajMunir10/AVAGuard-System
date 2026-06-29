# Implementation: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Implementation

## Scenario / Query
After deploying Microsoft Purview, the Data Map shows no assets even though I have registered Azure SQL Database sources. What are the common configuration issues that prevent asset ingestion?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Purview account created with system-assigned managed identity; sources registered via the Purview governance portal; scanning permissions set at the resource level.

## Symptoms
- No assets appear in the Data Map after scanning completes
- Scan status shows 'Completed' but asset count remains zero
- No errors are reported in the scan history

## Error Codes
N/A

## Root Causes
1. The managed identity of the Purview account does not have the required role (e.g., Reader on the Azure SQL Database) to read metadata
2. The scan rule set does not include the asset types present in the source
3. The source registration uses an incorrect connection string or authentication method

## Remediation Steps
1. Verify that the Purview managed identity has been granted the 'Reader' role on the Azure SQL Database (or equivalent for other sources) â€“ see 'Grant permissions to the Purview managed identity' in the official documentation
2. Confirm that the scan rule set includes the asset types you expect to discover (e.g., tables, views)
3. Re-register the source using the correct connection string and authentication (e.g., system-assigned managed identity) and run a full scan again

## Validation
After applying the correct permissions and re-scanning, the Data Map should populate with the expected assets. You can verify by navigating to the Data Map and checking the asset count for the scanned source.

## Rollback
Remove the role assignment from the Purview managed identity if you need to revert permissions. Delete the scan and re-register the source with the original settings.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-scanning>
