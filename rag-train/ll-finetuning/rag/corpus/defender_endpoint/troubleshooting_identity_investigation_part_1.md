# Troubleshooting: Identity Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Identity Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How to access the Identity page in Microsoft Defender when authorization is required?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** User must have appropriate permissions to access the Identity page

## Symptoms
- Access to this page requires authorization
- Cannot view identity details

## Error Codes
N/A

## Root Causes
1. User lacks required permissions
2. User is not signed in to the correct directory

## Remediation Steps
1. Try signing in with appropriate credentials
2. Try changing directories to the correct tenant

## Validation
1. Open a new InPrivate/Incognito browser session and navigate to https://security.microsoft.com. 2. Sign in with the user account that has the required permissions (e.g., Global Administrator, Security Administrator, or Security Reader). 3. In the left navigation pane, select 'Users' under 'Investigation & response' to access the Identity page. 4. Confirm that the user details and alerts are displayed without any 'Access to this page requires authorization' error. 5. Verify that the directory shown in the top-right corner matches the correct tenant (e.g., the tenant where the user has permissions).

## Rollback
1. If the remediation fails, sign out of the current session and sign in with the original user account that was experiencing the issue. 2. Navigate to https://security.microsoft.com and attempt to access the Identity page again to confirm the error persists. 3. If the error is resolved but the wrong tenant is displayed, use the directory switcher in the top-right corner to change back to the original tenant. 4. If the user still cannot access the Identity page, verify that the user has been assigned the required role (e.g., Security Reader) in the Microsoft 365 Defender portal by checking Azure AD roles or Microsoft 365 Defender role groups.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
