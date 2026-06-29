# Incident Response: Incident Response

**Domain:** Governance
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I configure Microsoft 365 Defender to automatically create an incident and trigger a response playbook when a user reports a phishing email?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Microsoft 365 Defender portal, Microsoft 365 Defender incident queue, automated investigation and response (AIR) policies

## Symptoms
- Users report phishing emails via the built-in Report Message add-in or Outlook button.
- Reported messages are not automatically generating incidents in the Microsoft 365 Defender portal.
- Automated investigation and response (AIR) is not triggered for user-reported phishing submissions.

## Error Codes
N/A

## Root Causes
1. The 'User reported messages' policy in Microsoft 365 Defender is not configured to automatically create incidents.
2. The 'Automated investigation and response' policy for user-reported messages is disabled or not set to trigger on phishing submissions.
3. The necessary role permissions (e.g., Security Administrator, Incident Responder) are not assigned to the team managing incidents.

## Remediation Steps
1. Navigate to Microsoft 365 Defender portal > Email & collaboration > Policies & rules > Threat policies > User reported messages settings.
2. Under 'User reported messages', select 'Use the built-in Report Message add-in' or 'Use the built-in Report Phishing add-in' as appropriate.
3. Under 'What should happen when a user reports a message?', select 'Create an incident in Microsoft 365 Defender' and enable 'Automatically run an investigation'.
4. Save the policy and verify that the incident queue in Microsoft 365 Defender now shows incidents for user-reported phishing.

## Validation
Submit a test phishing email to a user in the tenant, have the user report it using the Report Message add-in, and confirm that a new incident appears in the Microsoft 365 Defender incident queue within a few minutes.

## Rollback
Revert the 'User reported messages' policy to its previous state (e.g., 'Do not create incidents' or 'Send to Microsoft for analysis only').

## References
- Microsoft 365 Defender documentation: 'Automated investigation and response (AIR) in Microsoft 365 Defender' - https://learn.microsoft.com/en-us/microsoft-365/security/defender/m365d-autoir
- Microsoft 365 Defender documentation: 'Incident response with Microsoft 365 Defender' - https://learn.microsoft.com/en-us/microsoft-365/security/defender/incidents-overview
