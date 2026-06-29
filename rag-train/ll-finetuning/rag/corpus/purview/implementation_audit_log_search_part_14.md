# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to set a custom name for an audit log search job?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Microsoft Purview

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enter a custom name for your search job in the Search name field
2. If you don't enter a name, the search job is automatically named using a combination of the date and time defined for the search and other defined search criteria values

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. Verify that the search job appears with the custom name you specified in the 'Search name' field. 3. Confirm that the search job runs successfully and returns expected results. 4. Optionally, use the Search-UnifiedAuditLog cmdlet in Exchange Online PowerShell to retrieve the audit log search job by its custom name and verify its properties.

## Rollback
1. If the custom name caused issues, delete the search job from the Microsoft Purview compliance portal. 2. Recreate the search job without entering a custom name, allowing the system to auto-generate a name based on date, time, and search criteria. 3. Alternatively, use the Remove-UnifiedAuditLogRetentionPolicy cmdlet (if applicable) or manually remove the job via the portal.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
