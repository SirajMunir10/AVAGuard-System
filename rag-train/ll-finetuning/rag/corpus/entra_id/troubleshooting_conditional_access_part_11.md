# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve authorization errors when accessing Conditional Access policy documentation?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
1. Insufficient permissions to view the documentation page

## Remediation Steps
1. Sign in with appropriate credentials
2. Change directories to access the page

## Validation
1. Open a new InPrivate or Incognito browser session. 2. Navigate to https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common. 3. Confirm the page loads without any 'Access to this page requires authorization' or 'You can try signing in or changing directories' error messages. 4. Verify that the user is signed in with an account that has at least the Global Reader role in the tenant associated with the directory being accessed.

## Rollback
1. Sign out of the current session. 2. Clear browser cache and cookies. 3. Re-attempt access to the documentation page without signing in, or sign in with an account that does not have sufficient permissions to confirm the original error reappears. 4. If the remediation involved changing directories, switch back to the original directory and verify the error returns.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
