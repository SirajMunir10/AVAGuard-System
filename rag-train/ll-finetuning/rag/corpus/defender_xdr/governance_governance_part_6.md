# Governance: Governance

**Domain:** Defender XDR
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security operations team needs to ensure that only authorized personnel can modify threat indicators in Microsoft Defender for Endpoint. What built-in role-based access control (RBAC) mechanism should be configured to prevent unauthorized creation or deletion of indicators, and how is it applied?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Custom RBAC roles under Microsoft 365 Defender > Permissions > Endpoint roles

## Symptoms
- Users without explicit permissions are able to create or delete indicators of compromise (IOCs) via the Microsoft 365 Defender portal or API
- Audit logs show indicator modifications by accounts not assigned to a security operations role

## Error Codes
N/A

## Root Causes
1. The default 'Security administrator' role in Azure AD grants broad permissions, including indicator management, without granular control
2. No custom RBAC role has been created to restrict indicator management to specific groups

## Remediation Steps
1. Navigate to Microsoft 365 Defender > Permissions > Endpoint roles > Turn on roles
2. Create a new custom role with the permission 'Manage security settings in Security Center' set to 'View' (or 'No access') to prevent indicator creation/deletion
3. Assign the custom role to a dedicated Azure AD security group containing only authorized SOC analysts
4. Remove any direct assignment of the 'Security administrator' role from users who should not manage indicators

## Validation
Verify that a user in the restricted group cannot create or delete indicators via the portal or API, and that audit logs show 'Access denied' for such attempts.

## Rollback
Reassign the default 'Security administrator' role to affected users, or delete the custom RBAC role and reassign users to the built-in role.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/rbac>
