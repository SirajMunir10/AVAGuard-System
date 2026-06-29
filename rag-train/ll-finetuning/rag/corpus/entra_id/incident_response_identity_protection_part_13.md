# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to confirm a sign-in as safe when anomalous token or token issuer anomaly is detected but characteristics are expected?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Identity Protection risk detections

## Symptoms
- Anomalous token detection
- Token issuer anomaly detection

## Error Codes
N/A

## Root Causes
1. Location, application, IP address, User Agent, or other characteristics are expected for the user and there aren't other indications of compromise

## Remediation Steps
1. Allow the user to self-remediate with a risk-based Conditional Access policy
2. Have an admin confirm sign-in as safe

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator or Global Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Locate the specific risky sign-in by filtering for the user or time period. 4. Verify the sign-in status shows 'Confirmed safe' and the risk state is 'Dismissed'. 5. Optionally, use the Microsoft Graph API: GET /identityProtection/riskySignIns?$filter=userId eq '{user-id}' and riskState eq 'dismissed' to confirm the sign-in is no longer in the risky state.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Security Administrator or Global Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Locate the previously confirmed safe sign-in by filtering for the user or time period. 4. Select the sign-in and choose 'Confirm sign-in compromised' to revert the status. 5. Alternatively, use the Microsoft Graph API: POST /identityProtection/riskySignIns/{riskySignInId}/confirmCompromised to mark the sign-in as compromised again.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
