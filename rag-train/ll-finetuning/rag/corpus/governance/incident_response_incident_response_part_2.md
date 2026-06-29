# Incident Response: Incident Response

**Domain:** Governance
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security administrator suspects a user account in the tenant has been compromised. How should they initiate an automated investigation and response using Microsoft 365 Defender, and what are the required permissions?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft 365 Defender enabled
- **Configuration:** Automated investigation and response (AIR) enabled in Microsoft 365 Defender; user assigned to Security Administrator role

## Symptoms
- Suspicious sign-in activity from an unfamiliar location
- Multiple failed login attempts followed by a successful login
- User reports receiving phishing emails from their own account

## Error Codes
N/A

## Root Causes
1. User account credentials were compromised via phishing or password reuse

## Remediation Steps
1. 1. Confirm the user has the required permissions: Security Administrator or Security Reader role in Azure AD.
2. 2. In Microsoft 365 Defender portal (https://security.microsoft.com), navigate to Incidents & alerts > Incidents.
3. 3. Select the relevant incident and choose 'Initiate automated investigation'.
4. 4. Review the investigation graph and recommended actions.
5. 5. Approve or reject pending actions (e.g., soft-delete email, disable user account) as guided by the investigation.
6. 6. After remediation, reset the user's password and revoke all refresh tokens.

## Validation
Verify that the incident is resolved by checking the investigation status shows 'No threats found' or 'Remediated' in the Microsoft 365 Defender portal.

## Rollback
If an action was incorrectly approved, use the Action center in Microsoft 365 Defender to undo the action (e.g., restore a deleted email or re-enable a user account).

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/m365d-autoir>
