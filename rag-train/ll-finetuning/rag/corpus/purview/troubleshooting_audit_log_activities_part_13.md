# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to monitor changes to team access type and classification in audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Need to track when team access type is changed from private to public or vice versa
- Need to track changes to team information classification

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search for activities related to team access type changes (Team access type)
2. Search for activities related to team classification changes (Team classification)
3. Review the Item column to identify the specific change

## Validation
1. Go to Microsoft Purview compliance portal > Audit > Search. 2. Set 'Activities' to 'Team access type' and run a search for the relevant date range. 3. Verify that the search results include entries showing changes from private to public or vice versa. 4. Repeat the search with 'Activities' set to 'Team classification'. 5. Confirm that the results display changes to classification labels. 6. For each result, click the entry and review the 'Item' column to confirm the specific change details.

## Rollback
1. If the audit log search does not return expected results, verify that audit logging is enabled in the Microsoft 365 admin center (Settings > Org Settings > Audit log). 2. Ensure the user performing the search has the 'Audit Logs' role or is assigned to the 'Compliance Administrator' role group. 3. Check that the date range covers the period when the change occurred. 4. If still no results, contact Microsoft Support to confirm audit data is being collected for the tenant.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
