# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate incidents that affect your network in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** N/A

## Symptoms
- Access to the investigation page requires authorization
- Unable to view incident details, comments, or actions

## Error Codes
N/A

## Root Causes
1. Lack of authorization to access the page

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Confirm that the user account has the required role (e.g., Security Administrator, Security Reader, or a custom role with 'View data – Security operations' permission) assigned in Microsoft 365 Defender. 2. Sign out of the current session, then sign in again at https://security.microsoft.com. 3. Navigate to Incidents & alerts > Incidents and verify that the incident list loads and that you can open an incident to view details, comments, and the action center. 4. If the issue persists, switch directories by selecting the tenant directory from the account picker in the top-right corner and repeat step 3.

## Rollback
1. If the user was granted a new role as part of remediation, remove that role assignment in Azure AD (Azure Active Directory) > Roles and administrators. 2. If the user signed in with a different account, sign out and sign back in with the original account. 3. If the directory was changed, switch back to the original tenant directory using the account picker. 4. Verify that the user can no longer access the investigation page (expected behavior if authorization was correctly removed).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/investigate-incidents>
