# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify when a user or group is removed from a SharePoint group in audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- User removed from SharePoint group unexpectedly
- Unsharing event occurred

## Error Codes
N/A

## Root Causes
1. Intentional removal by a user
2. Result of another activity such as an unsharing event

## Remediation Steps
1. Search for all activities in the audit log
2. Look for the activity 'Removed user or group from SharePoint group' with the operation 'RemovedFromGroup'

## Validation
1. Go to Microsoft Purview compliance portal > Audit > Search. 2. Set the date range to cover the time of the unexpected removal. 3. In the Activities list, select 'Removed user or group from SharePoint group' (operation 'RemovedFromGroup'). 4. Run the search and confirm the audit log shows the specific user or group removal event with the correct target user/group and SharePoint group name. 5. Optionally, use Search-UnifiedAuditLog -Operations 'RemovedFromGroup' -StartDate <date> -EndDate <date> in Exchange Online PowerShell to verify the event.

## Rollback
1. Identify the SharePoint group and the removed user/group from the audit log event details. 2. Add the user or group back to the SharePoint group using SharePoint admin center or via PowerShell: Add-SPOUser -Group 'GroupName' -LoginName 'user@domain.com'. 3. If the removal was part of an unsharing event, review and restore the sharing link or permissions as needed. 4. Verify the user/group is now a member of the SharePoint group by checking group membership in SharePoint site settings.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
