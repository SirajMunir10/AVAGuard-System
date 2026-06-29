# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to filter audit log search results by workload services in Microsoft Purview?

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
1. Enter or search for workload services in the Workloads field
2. This filters the search to show activity related to the selected workloads

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search. 2. In the 'Workloads' field, select one or more workload services (e.g., Exchange, SharePoint, Azure Active Directory). 3. Click 'Search'. 4. Confirm that the results list only contains audit records from the selected workload(s). 5. Optionally, export the results and verify that the 'Workload' column matches the selected services.

## Rollback
1. Clear the 'Workloads' field by removing all selected workload services. 2. Click 'Search' to return to the default unfiltered view. 3. Verify that audit log results now include all workload services. 4. If needed, reset any saved search queries that included workload filters by editing or deleting them.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
