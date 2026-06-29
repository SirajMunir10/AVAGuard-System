# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify MemberRoleChanged operations in the audit log and interpret role type values?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Team member role changed

## Error Codes
N/A

## Root Causes
1. Team owner changed role of members in a team

## Remediation Steps
1. Search audit log for MemberRoleChanged operation
2. Review Members property for role type: 1 = Member, 2 = Owner, 3 = Guest

## Validation
1. Run the following command in the Microsoft 365 Defender portal or via Search-UnifiedAuditLog in Exchange Online PowerShell:
   Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations "MemberRoleChanged" | Format-Table CreationTime, UserIds, Operations, AuditData
2. For each returned audit record, inspect the AuditData property (or the JSON in the web UI) and confirm that the Members field contains a role type value of 1 (Member), 2 (Owner), or 3 (Guest).
3. Verify that the role type values match the expected change: e.g., if a member was promoted to owner, the AuditData should show the new role type as 2.
4. Confirm that no other unexpected operations (e.g., RoleChanged) are present for the same team and time period.

## Rollback
1. If the remediation (audit search) reveals incorrect role assignments, the team owner must manually revert the role changes via the Teams admin center or the Remove-TeamUser / Add-TeamUser PowerShell cmdlets.
2. For each affected user, run:
   Add-TeamUser -GroupId <TeamGroupId> -User <UserPrincipalName> -Role <OriginalRole> (e.g., Member or Owner)
   Remove-TeamUser -GroupId <TeamGroupId> -User <UserPrincipalName> (if the user was incorrectly added)
3. Re-run the audit log search to confirm the MemberRoleChanged operations now reflect the corrected roles.
4. If the audit log search itself fails (e.g., no results due to permissions), ensure the user has the Audit Log.Read role in Microsoft Entra ID and that audit logging is enabled in the organization.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
