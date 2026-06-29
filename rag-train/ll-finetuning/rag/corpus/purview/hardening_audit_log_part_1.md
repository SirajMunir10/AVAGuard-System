# Hardening: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Hardening

## Scenario / Query
How to harden external sharing by auditing and blocking sharing invitations based on domain policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** External sharing policies with domain allow/block lists

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure domain allow or block lists in SharePoint and OneDrive external sharing settings
2. Monitor SharingInvitationBlocked events to ensure policy enforcement
3. Review SharingInvitationAccepted events to verify only allowed domains are granted access

## Validation
Check that SharingInvitationBlocked events appear for blocked domains and no unauthorized sharing occurs

## Rollback
Remove domain restrictions from external sharing policy

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/sharepoint/restricted-domains-sharing>
