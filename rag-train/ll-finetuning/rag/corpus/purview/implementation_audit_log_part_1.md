# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to implement auditing for sharing and access request activities in SharePoint and OneDrive?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable audit log in Microsoft 365 compliance center
2. Monitor events such as AccessRequestAccepted, SharingInvitationAccepted, PermissionLevelAdded, CompanyLinkCreated, AccessRequestCreated, AnonymousLinkCreated, SecureLinkCreated
3. Use the Detail column under Results to identify the user or group the item was shared with and whether they are a member or guest

## Validation
Confirm that sharing events appear in the audit log with correct details

## Rollback
Disable audit logging if needed

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/purview/use-sharing-auditing>
