# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and investigate sharing activities in SharePoint or OneDrive using audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- User shared a resource with a user not in the organization's directory
- Secure sharing link was deleted
- Access request to a site, folder, or document was denied
- Company-wide link to a resource was removed
- Anonymous link to a resource was removed
- File, folder, or site shared with a user in the organization's directory
- File, folder, or site unshared with another user
- Access request to an item was updated
- Anonymous link to a resource was updated
- External sharing invitation was updated
- Resource accessed using a company-wide link
- Anonymous user accessed a resource using an anonymous link
- User used a secure link
- User added to the list of entities who can use a secure sharing link
- User removed from the list of entities who can use a secure sharing link
- Sharing invitation to a resource was withdrawn

## Error Codes
N/A

## Root Causes
1. Sharing invitation created for external user
2. Secure link deleted by user
3. Access request denied by owner
4. Company shareable link removed by user
5. Anonymous link removed by user
6. File, folder, or site shared with internal user
7. File, folder, or site unshared by user
8. Access request updated
9. Anonymous link updated
10. Sharing invitation updated
11. Company shareable link used
12. Anonymous link used by anonymous user
13. Secure link used
14. User added to secure link
15. User removed from secure link
16. Sharing invitation revoked

## Remediation Steps
1. Review the SharingInvitationCreated event to identify external sharing invitations
2. Check SecureLinkDeleted event for deleted secure links
3. Investigate AccessRequestDenied event for denied access requests
4. Monitor CompanyLinkRemoved event for removal of company-wide links
5. Track AnonymousLinkRemoved event for removal of anonymous links
6. Examine User (member or guest) shared a file, folder, or site event for internal sharing
7. Review SharingRevoked event for unsharing activities
8. Check AccessRequestUpdated event for updates to access requests
9. Review AnonymousLinkUpdated event for updates to anonymous links
10. Examine SharingInvitationUpdated event for updates to external sharing invitations
11. Monitor CompanyLinkUsed event for usage of company-wide links
12. Track AnonymousLinkUsed event for anonymous link usage
13. Review SecureLinkUsed event for secure link usage
14. Check AddedToSecureLink event for additions to secure link entities
15. Review RemovedFromSecureLink event for removals from secure link entities
16. Examine SharingInvitationRevoked event for withdrawn sharing invitations

## Validation
1. Run the following command in the Microsoft 365 Defender portal or via Search-UnifiedAuditLog in Exchange Online PowerShell to confirm that the relevant audit events are present:
   Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations "SharingInvitationCreated", "SecureLinkDeleted", "AccessRequestDenied", "CompanyLinkRemoved", "AnonymousLinkRemoved", "SharingRevoked", "AccessRequestUpdated", "AnonymousLinkUpdated", "SharingInvitationUpdated", "CompanyLinkUsed", "AnonymousLinkUsed", "SecureLinkUsed", "AddedToSecureLink", "RemovedFromSecureLink", "SharingInvitationRevoked" | Format-Table CreationDate, UserIds, Operations, ItemName
2. Verify that the output includes records for the specific sharing activities you are investigating (e.g., external sharing invitations, secure link deletions, denied access requests).
3. For each event type, confirm that the audit record contains the expected details such as user, target resource, and timestamp.
4. If using the Purview compliance portal, navigate to Audit > Search and apply the same operations filter to visually confirm the events are logged.

## Rollback
1. If the audit log search returns no results or incomplete data, verify that audit logging is enabled in the Microsoft 365 Defender portal under Audit > Audit log settings.
2. If audit logging is disabled, enable it by running: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true (requires Exchange Online PowerShell).
3. If the issue is that specific events are missing, ensure that the correct workload (SharePoint or OneDrive) is selected in the audit log search filter.
4. If the audit log search is still not returning expected events, check the Microsoft 365 Service Health Dashboard for any known issues with audit log ingestion.
5. As a last resort, contact Microsoft Support to investigate potential data loss or ingestion delays.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
