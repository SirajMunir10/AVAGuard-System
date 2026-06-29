# Governance: Microsoft Entra ID (Azure AD) Governance

**Domain:** Azure
**Subdomain:** Microsoft Entra ID (Azure AD) Governance
**Incident Type:** Governance

## Scenario / Query
A security auditor reports that the Azure AD 'Guest user access' setting is set to 'Guest user access is restricted to properties and memberships of their own directory objects' instead of the more restrictive 'Guest user access is restricted to properties and memberships of their own directory objects (most restrictive)'. What are the governance implications and how should this be remediated?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) tenant with guest users
- **Configuration:** External Identities / External collaboration settings / Guest user access

## Symptoms
- Guest users can read properties and memberships of directory objects beyond their own
- Audit logs show guest users enumerating group memberships or user properties outside their scope
- Compliance violation report flags guest user access level as not most restrictive

## Error Codes
N/A

## Root Causes
1. Guest user access level was not set to the most restrictive option in External Identities settings
2. Lack of governance policy enforcing the most restrictive guest access level

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as a Global Administrator
2. Navigate to Identity > External Identities > External collaboration settings
3. Under 'Guest user access', select 'Guest user access is restricted to properties and memberships of their own directory objects (most restrictive)'
4. Click Save

## Validation
Verify that the setting is now 'Guest user access is restricted to properties and memberships of their own directory objects (most restrictive)' and confirm via audit logs that guest users can no longer enumerate directory objects outside their own scope.

## Rollback
Revert to the previous less restrictive setting by selecting 'Guest user access is restricted to properties and memberships of their own directory objects' and saving.

## References
- Microsoft Learn: 'Configure external collaboration settings' - https://learn.microsoft.com/en-us/entra/identity/users/users-restrict-guest-permissions
