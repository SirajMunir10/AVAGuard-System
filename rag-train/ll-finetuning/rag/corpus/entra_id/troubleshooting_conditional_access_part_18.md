# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Access to this page requires authorization' error when accessing Conditional Access grant documentation?

## Environment Context
- **Tenant Type:** Entra ID tenant
- **Configuration:** Conditional Access policies

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
1. User lacks sufficient permissions to view the documentation page

## Remediation Steps
1. Sign in with appropriate credentials
2. Change directories to a tenant with proper access

## Validation
1. Open an InPrivate or Incognito browser session. 2. Navigate to https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant. 3. If prompted, sign in with credentials that have at least the 'Conditional Access Administrator' or 'Global Reader' role assigned in the target tenant. 4. Confirm the page loads without the 'Access to this page requires authorization' error. 5. Verify the directory shown in the top-right corner matches the tenant where you have appropriate permissions.

## Rollback
1. Sign out of the current session. 2. Clear browser cookies and cache. 3. Reopen a private browser session. 4. Navigate to the same documentation URL. 5. If the error reappears, switch to a different tenant directory by clicking the directory picker in the top-right corner and selecting a tenant where you have at least 'Conditional Access Administrator' or 'Global Reader' permissions. 6. If the issue persists, contact your tenant administrator to verify your role assignments.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
