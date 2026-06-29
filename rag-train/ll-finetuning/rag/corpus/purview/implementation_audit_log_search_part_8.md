# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to set a custom name for an audit log search job in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview Audit Log Search

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enter a custom name for your search job in the Search name field
2. This name is used to identify your search job in the search job history
3. If you don't enter a name, the search job is automatically named using a combination of the date and time defined for the search and other defined search criteria values

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search. 2. Create a new audit log search job and enter a custom name in the 'Search name' field (e.g., 'CustomAuditSearch_2025-01-01'). 3. Run the search. 4. After the search completes, go to the 'Search job history' tab. 5. Verify that the custom name appears in the list of search jobs. 6. Confirm that the search job details (e.g., date, time, criteria) are correctly associated with the custom name.

## Rollback
1. If the custom name is not accepted or causes issues, delete the search job from the 'Search job history' by selecting the job and clicking 'Delete'. 2. Create a new audit log search job without entering a custom name (leave the 'Search name' field blank). 3. Run the search. 4. Verify that the search job is automatically named using a combination of the date, time, and other defined search criteria values, as per default behavior.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
