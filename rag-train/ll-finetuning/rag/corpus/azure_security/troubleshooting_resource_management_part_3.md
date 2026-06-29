# Troubleshooting: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve authorization errors when accessing Azure resource tagging documentation?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Access to documentation page requires authorization

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Open a private/incognito browser session and navigate to https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources. 2. Confirm the page loads without any 'Access to this page requires authorization' or 'You can try signing in or changing directories' error messages. 3. If prompted, sign in with a valid Azure account that has at least Reader permissions on any Azure subscription. 4. After signing in, refresh the page and verify the full documentation content is displayed without authorization errors.

## Rollback
1. If the page still shows authorization errors after signing in, sign out of the current account. 2. Clear browser cookies and cache for learn.microsoft.com. 3. Open a new private/incognito session and navigate to the same URL. 4. Select 'Sign in' and use a different Azure account (e.g., from a different tenant/directory). 5. If the error persists, try accessing the page from a different network or device to rule out IP/network restrictions. 6. If none of the above resolves the issue, contact your Azure AD administrator to verify your account has the necessary permissions to access Microsoft Learn documentation.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
