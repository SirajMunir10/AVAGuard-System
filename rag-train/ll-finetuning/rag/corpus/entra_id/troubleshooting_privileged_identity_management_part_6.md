# Troubleshooting: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Access to this page requires authorization' error when configuring PIM?

## Environment Context
- **Tenant Type:** Entra ID tenant
- **Configuration:** PIM configuration page access

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
1. User lacks required permissions to access PIM configuration page

## Remediation Steps
1. Try signing in with appropriate credentials
2. Try changing directories (likely referring to switching to a different tenant or directory)

## Validation
1. Sign in to the Entra ID tenant as a user with at least the Privileged Role Administrator role. 2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Settings. 3. Verify that the PIM configuration page loads without the 'Access to this page requires authorization' error. 4. Confirm that the user can view and modify PIM settings (e.g., role activation settings, notification settings).

## Rollback
1. If the validation fails, sign out and sign in again with the original credentials that triggered the error. 2. If the error persists, ensure the user is assigned the Privileged Role Administrator role in the correct directory (tenant). 3. If the user is in the wrong directory, switch directories by selecting the correct tenant from the directory + subscription filter in the Azure portal. 4. If the issue remains, verify that the user has a valid Entra ID P2 license assigned.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
