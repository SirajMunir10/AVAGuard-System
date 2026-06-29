# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to search audit logs in Microsoft Purview Audit (Standard) and Audit (Premium) to investigate user activities?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit (Standard) or Audit (Premium) enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the Microsoft Purview portal to start audit log search jobs.
2. Search jobs continue running even after closing the browser window.
3. Completed search jobs are kept for 30 days.
4. Each admin Audit account user can have up to 10 search jobs running simultaneously, with a limit of one unfiltered search job.

## Validation
1. Navigate to Microsoft Purview portal > Audit solutions > Audit. 2. Verify that the search job initiated in remediation steps appears in the list of audit log searches with status 'Completed' or 'In progress'. 3. Confirm that the search job was created within the last 30 days. 4. Ensure that the total number of running search jobs for the admin account does not exceed 10, and that no more than one unfiltered search job is active.

## Rollback
1. In the Microsoft Purview portal > Audit solutions > Audit, locate the search job created during remediation. 2. If the job is still running, wait for it to complete or cancel it by selecting the job and choosing 'Cancel search'. 3. If the job has completed and is causing issues, delete the search job by selecting it and choosing 'Delete search'. 4. Verify that the search job is removed from the list and no longer appears in audit log searches.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
