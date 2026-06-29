# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How to start remediation actions for a Communication Compliance policy alert?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policies with alerts

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the policy associated with the alert to launch the Policy details page
2. From the Policy details page, review a summary of the activities
3. Review and act on policy matches on the Pending tab
4. Summarize a lengthy message by using Microsoft Copilot in Microsoft Purview
5. Review the history of closed policy matches on the Resolved tab

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy associated with the alert and confirm the Policy details page loads with a summary of activities. 3. On the Pending tab, verify that policy matches are listed and actionable (e.g., escalate, resolve, notify). 4. If applicable, open a lengthy message and confirm the 'Summarize' option from Microsoft Copilot is available and generates a summary. 5. On the Resolved tab, confirm that closed policy matches are displayed with history details.

## Rollback
1. If a policy match was incorrectly resolved, navigate to the Resolved tab, select the item, and use 'Reopen' to return it to the Pending tab. 2. If a notification was sent in error, inform the user that the notification was sent by mistake and provide correct guidance. 3. If an escalation was performed incorrectly, contact the assigned reviewer to disregard the escalation and reassign the item to the correct reviewer. 4. If a message was summarized using Copilot, no rollback is needed; the original message remains unchanged. 5. If a policy match was deleted, it cannot be recovered; ensure backups or audit logs are used for investigation.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
