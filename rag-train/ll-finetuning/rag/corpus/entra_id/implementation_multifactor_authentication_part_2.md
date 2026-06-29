# Implementation: Multifactor Authentication

**Domain:** Entra ID
**Subdomain:** Multifactor Authentication
**Incident Type:** Implementation

## Scenario / Query
How to monitor MFA registration and usage across an organization using the Authentication Methods Activity dashboard?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** MFA deployment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Have your business and technical application owners assume ownership of and consume these reports based on your organization's requirements.
2. Monitor authentication method registration and usage across your organization using the Authentication Methods Activity dashboard.

## Validation
1. Sign in to the Microsoft Entra admin center as a Global Administrator or Reports Reader. 2. Navigate to Identity > Monitoring & health > Authentication Methods Activity. 3. Under the 'Registration' tab, verify that the report shows the expected number of users registered for MFA and the breakdown by authentication method (e.g., Microsoft Authenticator, SMS, phone call). 4. Under the 'Usage' tab, confirm that the report displays successful and failed MFA attempts, including the top authentication methods used and trends over the selected time period. 5. Optionally, export the report to CSV and compare the data with your organization's MFA deployment records to ensure accuracy.

## Rollback
1. If the Authentication Methods Activity dashboard is not displaying expected data, verify that the user has the correct license (Microsoft Entra ID P1 or P2) and role (Global Administrator, Reports Reader, Security Administrator, or Authentication Administrator). 2. Ensure that the 'Authentication Methods Activity' feature is enabled in the tenant by checking under Identity > Monitoring & health > Diagnostic settings and confirming that the 'AuditLogs' and 'SignInLogs' categories are being sent to a Log Analytics workspace if custom reporting is needed. 3. If the dashboard shows no data, wait up to 24 hours for data to populate, as the dashboard aggregates data from the last 30 days. 4. If the issue persists, contact Microsoft Support and provide the tenant ID and time range of the missing data.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
