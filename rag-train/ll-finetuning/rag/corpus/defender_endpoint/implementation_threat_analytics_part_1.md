# Implementation: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Implementation

## Scenario / Query
How to access and use threat analytics in Microsoft Defender XDR to identify and react to emerging threats?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Access to threat analytics requires authorization; user must be signed in and in the correct directory.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access threat analytics from the upper left-hand side of Microsoft Defender portal's navigation bar.
2. Alternatively, use a dedicated dashboard card that shows the top threats to your organization in terms of known impact and your exposure.

## Validation
1. Sign in to the Microsoft Defender portal (https://security.microsoft.com) with an account that has the required permissions (e.g., Security Administrator, Security Reader).
2. In the navigation bar on the upper left, click 'Threat analytics' to open the dashboard.
3. Verify that the dashboard displays threat reports, including the top threats to your organization with known impact and exposure metrics.
4. Alternatively, check the main dashboard for a card titled 'Top threats' or similar that links to threat analytics; confirm it shows relevant threat data.
5. Select a specific threat report and confirm that detailed information (e.g., description, recommended actions, affected devices) is accessible.

## Rollback
1. If the threat analytics dashboard does not load or shows errors, verify that the user account has the required role (e.g., Security Administrator, Security Reader) and is in the correct tenant directory.
2. Clear browser cache and cookies, then sign out and sign back in to the Microsoft Defender portal.
3. If the issue persists, check the service health status in the Microsoft 365 admin center for any known incidents affecting threat analytics.
4. As a last resort, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
