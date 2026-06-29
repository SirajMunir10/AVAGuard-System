# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to detect when a SharePoint group settings are updated in audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Group name changed
- Who can view or edit group membership changed
- How membership requests are handled changed

## Error Codes
N/A

## Root Causes
1. Site administrator or owner changed the settings of a group for a site

## Remediation Steps
1. Search for all activities in the audit log
2. Look for the activity 'Updated group' with the operation 'GroupUpdated'

## Validation
1. Go to Microsoft Purview compliance portal > Audit > Search. 2. Set 'Activities' to 'All activities' and search for 'Updated group'. 3. In the results, verify that the 'Operation' column shows 'GroupUpdated'. 4. Select a log entry and confirm the 'Details' pane includes the changed group settings (e.g., group name, membership permissions, request handling).

## Rollback
1. In the same audit log search, identify the original group settings from the 'OldValue' field in the 'GroupUpdated' event details. 2. Navigate to the SharePoint site, go to Site settings > Site permissions > Group settings. 3. Revert the group name, membership permissions, and request handling to the values recorded in the audit log. 4. Optionally, run the command: `Set-SPOSiteGroup -Identity <GroupName> -PermissionLevels <OriginalPermissions>` via SharePoint Online Management Shell.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
