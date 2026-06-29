# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit changes to Teams channel names or descriptions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Team channel name or description changed unexpectedly

## Error Codes
N/A

## Root Causes
1. Changes to team channel names and descriptions are logged with descriptions in parentheses in the Item column

## Remediation Steps
1. Search the audit log for activities related to channel name or description changes
2. Look for entries like 'Changes name of a team channel ( Channel name )' or 'Changes description of a team channel ( Channel description )' in the Item column

## Validation
Search the audit log for activities related to channel name or description changes. Use the following PowerShell command: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations 'ChannelUpdated' | Where-Object {$_.Item -match 'Changes name of a team channel \(.*\)' -or $_.Item -match 'Changes description of a team channel \(.*\)'} | Format-Table CreationDate, UserIds, Operations, Item -AutoSize. Confirm that the output includes entries with descriptions in parentheses in the Item column, such as 'Changes name of a team channel ( Channel name )' or 'Changes description of a team channel ( Channel description )'.

## Rollback
If the remediation fails or causes issues, restore the original channel name or description using the Teams admin center or PowerShell. For example, use Set-TeamChannel -GroupId <GroupId> -ChannelId <ChannelId> -DisplayName 'OriginalName' -Description 'OriginalDescription'. Verify the change by running the validation command again to ensure the audit log now shows the corrected activity.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
