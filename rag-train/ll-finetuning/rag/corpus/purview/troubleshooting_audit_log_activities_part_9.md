# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify changes to team settings in Microsoft Teams audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Changes made to team settings are not visible in audit log search results

## Error Codes
N/A

## Root Causes
1. The name of the setting that was changed is displayed in the Item column in the audit log search results

## Remediation Steps
1. Access audit log search in Microsoft Purview compliance portal
2. Search for activities related to team settings changes
3. Review the Item column to identify the specific setting that was changed

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search.
2. Set the Date range to cover the period when the team setting change was made.
3. In the Activities list, select 'Team setting changed' under 'Microsoft Teams activities'.
4. Click Search and wait for results to load.
5. In the results, locate the entry for the change and verify that the 'Item' column displays the name of the specific setting that was changed (e.g., 'AllowCreateUpdateChannels', 'AllowDeleteChannels', etc.).
6. If the Item column shows the setting name, the remediation is successful.

## Rollback
1. If the Item column does not display the expected setting name, confirm that audit logging is enabled for the tenant (Settings > Audit log in Microsoft Purview).
2. Verify that the user who made the change has the appropriate license (e.g., Microsoft 365 E5) and is assigned the 'Audit Log' role.
3. Re-run the search with a broader date range or different activity filter (e.g., 'Team created/deleted') to confirm audit data is populating.
4. If no results appear, contact Microsoft Support to investigate potential service issues or configuration gaps.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
