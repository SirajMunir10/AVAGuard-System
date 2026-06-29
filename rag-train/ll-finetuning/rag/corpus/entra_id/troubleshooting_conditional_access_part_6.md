# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Conditional Access policy issues when access to the troubleshooting page requires authorization?

## Environment Context
- **Tenant Type:** Entra ID tenant
- **Configuration:** Conditional Access policies

## Symptoms
- Access to the Conditional Access troubleshooting page requires authorization
- Cannot access the troubleshooting page due to authorization errors

## Error Codes
N/A

## Root Causes
1. User may not have signed in
2. User may need to change directories

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) with a user account that has at least the Conditional Access Administrator or Security Administrator role. 2. Navigate to 'Microsoft Entra ID' > 'Security' > 'Conditional Access' > 'Troubleshoot' and verify the page loads without authorization errors. 3. If the page still fails, open a private/incognito browser session, sign in again, and repeat step 2. 4. Confirm that the user's directory context is correct by checking the tenant switcher in the Azure portal top bar; if needed, select the correct directory.

## Rollback
1. If the troubleshooting page remains inaccessible after signing in, switch to a different directory by clicking the 'Directory + subscription' icon in the Azure portal top bar and selecting the correct tenant. 2. If the user still cannot access the page, ensure the user account has been assigned the required role (Conditional Access Administrator or Security Administrator) via 'Microsoft Entra ID' > 'Roles and administrators'. 3. As a last resort, use a different user account with the required permissions to access the troubleshooting page.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
