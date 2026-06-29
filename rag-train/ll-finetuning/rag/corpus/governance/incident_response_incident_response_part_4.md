# Incident Response: Incident Response

**Domain:** Governance
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How can I use Microsoft Defender for Cloud Apps to detect and respond to a suspicious sign-in from an unfamiliar location by a user with an admin role?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Cloud Apps (formerly Microsoft Cloud App Security) enabled
- **Configuration:** Activity policy configured to alert on anomalous sign-in from unfamiliar locations for Global Administrator role

## Symptoms
- User receives email alert from Microsoft Defender for Cloud Apps about a suspicious sign-in
- Sign-in event shows location that is not in the user's typical travel pattern
- User has Global Administrator role assigned

## Error Codes
N/A

## Root Causes
1. No conditional access policy requiring multi-factor authentication for unfamiliar sign-in locations
2. No activity policy in Defender for Cloud Apps to automatically suspend the user account upon detection

## Remediation Steps
1. In Microsoft Defender for Cloud Apps, investigate the alert by navigating to Alerts and selecting the suspicious sign-in alert
2. Use the Activity log to review the sign-in details (IP address, user agent, timestamp)
3. If confirmed malicious, immediately disable the user account via the Microsoft 365 admin center or via PowerShell using the documented cmdlet: `Disable-AzureADUser -ObjectId <user-object-id>`
4. Reset the user's password and revoke all sessions using the Microsoft 365 admin center or via `Revoke-AzureADUserAllRefreshToken -ObjectId <user-object-id>`
5. Create an activity policy in Defender for Cloud Apps to automatically suspend a user when a suspicious sign-in from an unfamiliar location is detected for admin roles

## Validation
Verify that the user account is disabled and that no further suspicious sign-ins occur from the same IP or location. Confirm that the activity policy is enabled and triggers alerts for similar future events.

## Rollback
Re-enable the user account after password reset and session revocation, and ensure the user can authenticate with MFA from a trusted location.

## References
- <https://learn.microsoft.com/en-us/defender-cloud-apps/investigate-alerts>
- <https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal>
