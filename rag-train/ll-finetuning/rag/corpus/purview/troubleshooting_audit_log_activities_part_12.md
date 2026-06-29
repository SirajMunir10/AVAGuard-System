# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to track team creation and deletion activities in audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Need to monitor when teams are created or deleted

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search for TeamCreated activity to identify when a user creates a team
2. Search for TeamDeleted activity to identify when a team owner deletes a team

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. Set 'Activities' filter to 'TeamCreated' and run a search for the relevant date range. Confirm that results show expected team creation events. 3. Change 'Activities' filter to 'TeamDeleted' and run a search. Confirm that results show expected team deletion events. 4. Optionally, export the audit log records to verify the details (e.g., user, timestamp, team name).

## Rollback
1. If the audit log search is not returning expected results, verify that Audit log search is enabled in the Microsoft 365 Defender portal under 'Audit log search' settings. 2. If disabled, enable it and wait up to 24 hours for historical data to populate. 3. If the issue persists, check that the user performing the search has the 'Audit Logs' role or equivalent permissions (e.g., Compliance Administrator, Audit Administrator). 4. As a last resort, open a support case with Microsoft to investigate missing audit events.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
