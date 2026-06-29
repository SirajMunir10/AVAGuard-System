# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to monitor the status and progress of audit log search jobs in the Purview compliance portal?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview audit log search

## Symptoms
- Search job status shows Queued, In Progress, or Completed
- Progress percentage displayed for each search job
- Total results count shown for completed searches

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the search job dashboard in Purview compliance portal
2. View the Job status column to check if search is Queued, In Progress, or Completed
3. Check Progress (%) column to see completion percentage
4. Review Search time column for total running time
5. Examine Total results column for number of returned results
6. Verify Creation time and Search performed by for audit trail

## Validation
Search job dashboard displays active and completed search jobs with status, progress, and results information

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
