# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to start an audit log search job and what are the limits on concurrent searches?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Purview compliance portal

## Symptoms
- Unable to start a new search job
- Search job limit reached

## Error Codes
N/A

## Root Causes
1. A maximum of 10 search jobs can be run in parallel for one user account

## Remediation Steps
1. Select Search to start your search job
2. If a user requires more than 10 search jobs, they must wait for an In progress job to finish or delete a search job

## Validation
1. In the Microsoft Purview compliance portal, navigate to Audit > Audit log search. 2. Attempt to start a new search job by selecting 'Search'. 3. Confirm that the search job starts successfully and appears in the list with a status of 'In progress'. 4. Verify that the total number of 'In progress' and 'Scheduled' search jobs for your user account does not exceed 10. 5. If the search job fails to start, check the error message to ensure it is not related to the concurrent job limit.

## Rollback
1. If a search job fails to start due to the concurrent job limit, wait for one or more 'In progress' jobs to complete. 2. Alternatively, delete one or more existing search jobs (either 'In progress' or 'Completed') by selecting the job and choosing 'Delete'. 3. After reducing the number of active jobs below 10, retry starting the new search job by selecting 'Search'.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
