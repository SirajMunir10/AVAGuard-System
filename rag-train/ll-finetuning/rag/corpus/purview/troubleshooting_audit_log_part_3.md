# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and troubleshoot blocked sharing invitations in SharePoint and OneDrive using audit log activities?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** External sharing policies based on domain allow/block lists

## Symptoms
- Sharing invitations are blocked
- Users report inability to share resources externally

## Error Codes
N/A

## Root Causes
1. Target user's domain is not included in the list of allowed domains
2. Target user's domain is included in the list of blocked domains

## Remediation Steps
1. Review the SharingInvitationBlocked event in the audit log to identify the blocked invitation
2. Check the external sharing policy for domain restrictions
3. Update the allowed or blocked domains list in SharePoint and OneDrive settings

## Validation
Verify that the SharingInvitationBlocked event no longer appears for the target domain after policy changes

## Rollback
Revert domain allow/block list changes to previous state

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/sharepoint/restricted-domains-sharing>
