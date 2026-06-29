# Governance: Microsoft Entra ID (Azure AD) Governance

**Domain:** Azure
**Subdomain:** Microsoft Entra ID (Azure AD) Governance
**Incident Type:** Governance

## Scenario / Query
A user reports they can no longer access an Azure resource that was previously accessible. Investigation shows the userâ€™s Azure AD role assignment was removed unexpectedly. What governance controls should be in place to detect and prevent unauthorized or accidental removal of role assignments?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure AD Privileged Identity Management (PIM) is not enabled; no access reviews configured; audit logs are not being monitored.

## Symptoms
- User receives '403 Forbidden' when attempting to access an Azure resource
- Azure AD audit logs show a 'Remove member from role' activity for the affected user
- No alert was generated when the role assignment was removed

## Error Codes
N/A

## Root Causes
1. No Azure AD Privileged Identity Management (PIM) configured to require approval for role removals
2. No access reviews established to periodically validate role assignments
3. Audit log monitoring and alerting not implemented

## Remediation Steps
1. Enable Azure AD Privileged Identity Management (PIM) for the tenant and configure role activation to require approval
2. Create access reviews for all privileged roles to ensure only authorized users retain assignments
3. Set up Azure Monitor alerts on the 'Remove member from role' audit log event to notify security operations
4. Implement a change management process that requires documented approval before any role assignment removal

## Validation
Verify that PIM is active and that a test role removal triggers the configured alert. Confirm that access reviews are scheduled and that reviewers receive notifications.

## Rollback
Disable PIM only after ensuring alternative governance controls (e.g., manual approval workflow) are in place. Remove alert rules only after verifying that the monitoring gap is closed by other means.

## References
- Microsoft Learn: 'What is Privileged Identity Management?' - https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure
- Microsoft Learn: 'What are Microsoft Entra access reviews?' - https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview
- CIS Microsoft Azure Foundations Benchmark v2.0.0 - Control 1.4: 'Ensure that 'Notify all global administrators when other admins are activated' is set to 'Yes''
