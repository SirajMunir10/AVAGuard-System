# Troubleshooting: Microsoft 365 Defender

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft 365 Defender
**Incident Type:** Troubleshooting

## Scenario / Query
How can Copilot generate an identity summary to assess a user's risk?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Copilot enabled in Microsoft 365 Defender

## Symptoms
- Need to quickly assess a user's risk and identify when an identity is at risk or suspicious

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Generate an identity summary with Copilot
2. Copilot provides contextualized information about a user's role and role changes, sign in behaviors, devices signed in to, and relevant contact information

## Validation
1. In Microsoft 365 Defender, navigate to Incidents & Alerts > Incidents and select an incident involving a user. 2. Open the Copilot pane (top-right icon). 3. Type or select 'Identity summary' for the user. 4. Verify the response includes: user role and recent role changes, sign-in behaviors (e.g., unusual locations, failed attempts), devices the user is signed into, and relevant contact information. 5. Confirm the summary is contextualized to the incident and provides risk indicators.

## Rollback
1. If the identity summary is inaccurate or incomplete, close the Copilot pane and manually investigate the user in Microsoft 365 Defender: go to Users > select the user to review sign-in logs, role assignments, and device inventory. 2. Cross-reference with Azure AD Identity Protection reports for risk detections. 3. If Copilot generated incorrect data, submit feedback via the thumbs-down icon in the Copilot pane to improve future responses. 4. No configuration changes were made, so no direct rollback of settings is required.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
