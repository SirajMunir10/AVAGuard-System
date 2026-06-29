# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to view incidents and alerts involving a specific user identity in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Supported retention window for incidents and alerts

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Incidents and alerts tab for the user identity.
2. Review all alerts and incidents involving the identity within the supported retention window.
3. Refer to the incidents page or the alerts page for a detailed description of the specific item.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to 'Incidents & alerts' > 'Incidents' and apply a filter for the specific user identity (e.g., user@domain.com) to confirm incidents are listed.
3. Go to 'Alerts' and apply the same user filter to confirm alerts are listed.
4. Verify that the incidents and alerts shown fall within the supported retention window (e.g., last 30 days for incidents, last 180 days for alerts).
5. Select an incident or alert and confirm the detailed description includes the user identity and relevant activity.

## Rollback
1. If the user identity filter returns no results or incorrect data, remove the filter and verify that incidents and alerts are visible for other users.
2. If the portal fails to load or shows errors, clear browser cache and cookies, then retry.
3. If the issue persists, check service health at https://admin.microsoft.com/AdminPortal/Home#/servicehealth for any ongoing incidents.
4. As a last resort, use Microsoft Graph API (GET /security/incidents?$filter=userPrincipalName eq 'user@domain.com') to retrieve the same data and compare results.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
