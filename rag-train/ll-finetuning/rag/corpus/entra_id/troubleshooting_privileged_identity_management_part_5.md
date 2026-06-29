# Troubleshooting: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to deactivate a role assignment in PIM when the deactivate option is not available?

## Environment Context
- **Tenant Type:** Entra ID tenant with PIM enabled
- **Configuration:** Role assignment activated in PIM

## Symptoms
- Deactivate option is not visible in the PIM portal for the role assignment

## Error Codes
N/A

## Root Causes
1. Cannot deactivate a role assignment within five minutes after activation

## Remediation Steps
1. Wait at least five minutes after activation before attempting to deactivate
2. Use the Deactivate option in the PIM portal for the role assignment

## Validation
1. Wait at least 5 minutes after the role activation timestamp. 2. Sign in to the Entra admin center (https://entra.microsoft.com) as the user who activated the role. 3. Navigate to Identity Governance > Privileged Identity Management > My roles > Azure AD roles (or Azure resources, as applicable). 4. Locate the activated role assignment. 5. Verify that the 'Deactivate' option is now visible and clickable next to the role. 6. Optionally, click 'Deactivate' and confirm the deactivation completes without error.

## Rollback
1. If the deactivation fails or the 'Deactivate' option remains unavailable, wait an additional 5 minutes from the last activation attempt. 2. Re-attempt deactivation via the same PIM portal path: Identity Governance > Privileged Identity Management > My roles > Azure AD roles. 3. If the issue persists, sign out and sign back in to refresh the session, then repeat steps 1-2. 4. As a last resort, contact the PIM administrator to remove the eligible assignment or deactivate the role via the PIM management interface (Azure AD roles > select role > Active assignments > select assignment > Remove).

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
