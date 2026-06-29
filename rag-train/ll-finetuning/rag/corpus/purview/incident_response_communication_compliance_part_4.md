# Incident Response: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Incident Response

## Scenario / Query
How to view insider risk activities in communication compliance for a user associated with an alert?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy configured

## Symptoms
- Alert generated for a user's communication activity

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Open in insider risk management to view the insider risk activities.
2. Review the Timeline section which displays a history of all communications for user activities.
3. For each Copilot interaction, review the details for the user prompt and the Copilot response.
4. Note the date and time for each interaction are provided in UTC.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance. 2. Select the policy that generated the alert. 3. Click on the alert for the user. 4. Verify that 'Open in insider risk management' option is available and clickable. 5. Confirm that the Timeline section displays a history of communications for the user's activities. 6. For each Copilot interaction, verify that the user prompt and Copilot response details are visible. 7. Confirm that the date and time for each interaction are displayed in UTC.

## Rollback
1. If the 'Open in insider risk management' option is not available, ensure the user has the necessary permissions (e.g., Communication Compliance admin, Insider Risk Management admin). 2. If the Timeline section does not display activities, verify that the Communication Compliance policy is correctly configured and that the user is included in the policy scope. 3. If Copilot interaction details are missing, check that the policy includes Copilot as a communication channel. 4. If date/time are not in UTC, adjust the user's time zone settings in the compliance portal or verify the system default.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
