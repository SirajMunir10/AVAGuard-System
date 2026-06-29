# Governance: Governance

**Domain:** Defender XDR
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
How can I ensure that only authorized users can create or modify custom detection rules in Microsoft 365 Defender, and that all changes are audited?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft 365 Defender roles and permissions, specifically the 'Custom detections' permission under the 'Security administrator' role group.

## Symptoms
- Unauthorized users are able to create or modify custom detection rules in the Microsoft 365 Defender portal.
- No audit log entries are generated when custom detection rules are created or modified.
- Security team cannot track who made changes to custom detection rules.

## Error Codes
N/A

## Root Causes
1. The 'Custom detections' permission is assigned to too many users or groups.
2. Audit logging for custom detection rule changes is not enabled or configured.
3. Role-based access control (RBAC) is not properly scoped to limit custom detection rule management to authorized security administrators.

## Remediation Steps
1. Review and restrict the 'Custom detections' permission to only the 'Security administrator' role group or a custom role group with a limited set of users.
2. Enable audit logging for Microsoft 365 Defender activities by ensuring the 'AuditLog' is turned on in the Microsoft 365 compliance center.
3. Use the Microsoft 365 Defender portal to assign the 'Custom detections' permission only to users who require it for their job function.
4. Regularly review audit logs for any unauthorized changes to custom detection rules.

## Validation
Verify that only users in the 'Security administrator' role group can create or modify custom detection rules, and that audit log entries are generated for each change.

## Rollback
If the restriction causes operational issues, temporarily add the affected user to the 'Security administrator' role group and then investigate the root cause.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/custom-detection-rules?view=o365-worldwide>
