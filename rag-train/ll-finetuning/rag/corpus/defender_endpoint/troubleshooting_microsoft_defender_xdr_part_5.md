# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to access and view the alerts queue in the Microsoft Defender portal when authorization is required?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Access to alerts page requires authorization; sign-in or directory change may be needed.

## Symptoms
- Access to this page requires authorization.

## Error Codes
N/A

## Root Causes
1. User may not be signed in or may need to change directories.

## Remediation Steps
1. Try signing in.
2. Try changing directories.

## Validation
1. Open a new browser session and navigate to https://security.microsoft.com/alerts. 2. If prompted, sign in with a user account that has the appropriate permissions (e.g., Security Reader, Security Operator, or Security Administrator role). 3. Confirm that the Alerts queue page loads successfully and displays a list of alerts. 4. Verify that the directory shown in the portal matches the tenant where you expect to see alerts (e.g., check the tenant picker or the account menu). 5. If the page still shows 'Access to this page requires authorization,' try switching directories via the tenant switcher in the portal header and re-verify access.

## Rollback
1. If the user was previously signed in and the alerts page was accessible, sign out of the Microsoft Defender portal. 2. Clear browser cache and cookies to remove any stale authentication tokens. 3. Revert any directory changes made during troubleshooting by switching back to the original tenant directory using the tenant switcher. 4. If the issue persists after remediation, re-apply the original sign-in method (e.g., use the previous user account or authentication method) and confirm that the alerts page returns to its prior state (either accessible or showing the authorization error).

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
