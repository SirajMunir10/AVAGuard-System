# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to search audit log for activities related to specific workloads?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Purview compliance portal

## Symptoms
- Need to filter audit log by workload service

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enter or search for workload services to search for activity related to the selected workloads
2. Enter the name of a workload to jump to the workload in the list or scroll to the workloads you'd like to select

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit solutions > Audit. 2. In the 'Activities' dropdown, verify that the workload-specific activity list appears when you select a workload (e.g., 'Exchange mailbox activities', 'SharePoint list activities'). 3. Confirm that searching for a workload name (e.g., 'SharePoint') in the 'Activities' filter box correctly jumps to and selects the corresponding workload entries. 4. Run a sample audit log search with a selected workload and verify that results are filtered to that workload's activities.

## Rollback
1. Clear any workload-specific filters by selecting 'Show results for all activities' or removing selections in the 'Activities' dropdown. 2. If the workload list does not appear or is incorrect, refresh the browser page to reload the default audit log search interface. 3. If the issue persists, verify that the user has the 'Audit Log' role in Purview compliance portal (permissions > Audit log role). 4. As a last resort, use the Search-UnifiedAuditLog PowerShell cmdlet with the -Operations parameter to manually filter by workload (e.g., Search-UnifiedAuditLog -Operations 'MailboxLogin','FileAccessed').

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
