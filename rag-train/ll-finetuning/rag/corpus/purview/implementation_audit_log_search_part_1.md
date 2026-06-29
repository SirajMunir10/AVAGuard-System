# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to delete an audit log search job and understand what gets removed?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview audit log search job management

## Symptoms
- Need to remove a search job from the dashboard

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the search job from the dashboard
2. Select Delete on the command bar

## Validation
Deleting a search job doesn't delete the backend data associated with search. It only deletes the search job definition and the associated search result.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
