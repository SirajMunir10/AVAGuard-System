# Implementation: Identity Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Identity Investigation
**Incident Type:** Implementation

## Scenario / Query
How to open the Identity page in Microsoft Defender to investigate a user?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Identity page accessible from multiple areas in Defender portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select an identity from the Identities inventory
2. Select an identity from the Alerts queue
3. Select an identity from individual alert pages
4. Select an identity from Incidents or devices
5. Select an identity from Advanced hunting results
6. Select an identity from the Activity log
7. Select an identity from the Action center

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to the Identities inventory (Identities > Identities) and confirm the user identity page loads with profile details, alerts, and activity.
3. Open an alert from the Alerts queue and click on the user name to verify the identity page opens correctly.
4. From an incident, select a user entity and confirm the identity page displays.
5. Run an Advanced hunting query (e.g., IdentityLogonEvents) and click a user name in results to verify the identity page loads.
6. Check the Activity log for a user and click the user name to confirm the identity page opens.
7. Verify the Action center shows user-related actions and clicking a user name opens the identity page.

## Rollback
1. If the identity page fails to load from any entry point, clear browser cache and cookies, then retry.
2. If the issue persists, verify that the user has the required permissions (e.g., 'View identity' permission in Microsoft Entra ID or Defender roles).
3. Ensure the Microsoft 365 Defender portal is accessible and not blocked by network policies.
4. If the problem is isolated to a specific user, check that the user account is synchronized and active in Microsoft Entra ID.
5. As a last resort, contact Microsoft Support for portal-level issues.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
