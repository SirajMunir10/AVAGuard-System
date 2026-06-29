# Incident Response: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Incident Response

## Scenario / Query
How to investigate unauthorized access or sharing incidents using audit log activities?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Suspicious sharing activity detected
- Unauthorized access to resources

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search audit log for events like AccessRequestAccepted, SharingInvitationAccepted, AnonymousLinkCreated, SecureLinkCreated
2. Identify the user who created the sharing link or accepted the invitation
3. Check the Detail column for the target user or group and whether they are a member or guest
4. Review the UserType property to determine if the user is a member or guest

## Validation
Confirm that the incident is contained and no further unauthorized sharing occurs

## Rollback
Revoke sharing permissions or remove guest accounts if necessary

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/purview/use-sharing-auditing>
