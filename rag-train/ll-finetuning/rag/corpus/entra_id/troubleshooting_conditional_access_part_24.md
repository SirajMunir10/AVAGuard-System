# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve authorization errors when accessing Conditional Access policy documentation for compliant device configuration?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access to this page requires authorization. You can try signing in or changing directories.
- Access to this page requires authorization. You can try changing directories.

## Error Codes
N/A

## Root Causes
1. Insufficient authorization to access the documentation page.

## Remediation Steps
1. Sign in with appropriate credentials.
2. Change directories to access the page.

## Validation
1. Open a new InPrivate or Incognito browser session.
2. Navigate to https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device.
3. If prompted, sign in with a user account that has at least the Conditional Access Administrator role assigned in the target tenant.
4. Confirm the page loads without any authorization error messages (e.g., 'Access to this page requires authorization').
5. Verify that the documentation content for compliant device configuration is fully displayed and accessible.

## Rollback
1. If the page still shows an authorization error after signing in, sign out of the current session.
2. Clear browser cache and cookies, or use a different browser/device.
3. Attempt to access the page again without signing in (i.e., as an anonymous user) to confirm the error persists.
4. If the error persists for all users, verify that the tenant's Conditional Access policies are not blocking access to learn.microsoft.com. Temporarily disable any policy that might interfere, then retry.
5. If the issue remains, contact Microsoft Support for further assistance, referencing the specific error and tenant ID.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
