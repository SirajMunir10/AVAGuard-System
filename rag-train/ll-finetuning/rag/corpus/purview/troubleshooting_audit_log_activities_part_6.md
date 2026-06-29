# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and interpret TeamSettingChanged operations in the audit log for changes to team access type or classification?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Team access type changed from private to public or vice versa
- Team classification changed

## Error Codes
N/A

## Root Causes
1. Team owner performed a TeamSettingChanged operation

## Remediation Steps
1. Search audit log for TeamSettingChanged operation
2. Review Item column for description of setting changed (e.g., 'Team access type' or 'Team classification')

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with appropriate permissions. 2. Navigate to Audit > Search. 3. Set the Activities filter to 'TeamSettingChanged' (under 'Microsoft Teams activities'). 4. Set the date range to cover the suspected change period. 5. Run the search and verify that one or more events with 'TeamSettingChanged' appear. 6. Click on an event to open the details flyout. 7. In the 'Item' column, confirm the description matches either 'Team access type' or 'Team classification'. 8. Optionally, use the Search-UnifiedAuditLog cmdlet in Exchange Online PowerShell: Search-UnifiedAuditLog -Operations 'TeamSettingChanged' -StartDate <start> -EndDate <end> | Select-Object -Property Operations,Item,UserIds,CreationDate | Format-Table -AutoSize

## Rollback
1. If the change was unintended, contact the team owner who performed the operation (identified from the UserIds field in the audit log). 2. Request the team owner to revert the setting: a. For access type: In Microsoft Teams, go to the team > Manage team > Settings > change 'Privacy' back to the original setting (Private or Public). b. For classification: In Microsoft Teams, go to the team > Manage team > Settings > change 'Classification' back to the original value. 3. After reversion, re-run the audit log search to confirm no new 'TeamSettingChanged' events for the same team and setting. 4. If the team owner is unavailable, use the Set-Team cmdlet in Teams PowerShell: Set-Team -GroupId <GroupId> -AccessType <Private|Public> or Set-Team -GroupId <GroupId> -Classification <ClassificationValue>.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
