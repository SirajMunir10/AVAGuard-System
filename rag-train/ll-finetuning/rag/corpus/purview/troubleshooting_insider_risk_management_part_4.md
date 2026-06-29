# Troubleshooting: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Troubleshooting

## Scenario / Query
How do I investigate an Insider Risk Management case to review user risk activity history, alert details, and risk events?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Insider Risk Management enabled with appropriate permissions

## Symptoms
- Need to dive deeper into user risk activity history
- Need to review alert details and sequence of risk events
- Need to explore content and messages exposed to risks

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select a case to open the case management tools
2. Use the case management tools to dig into the details of the case
3. Centralize review feedback and notes
4. Process case resolution

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Insider Risk Management > Cases.
3. Select the specific case you investigated.
4. Confirm that the case details page displays the user's risk activity history, alert details, and the sequence of risk events.
5. Verify that you can expand each alert to view associated activities and content (e.g., emails, files, messages).
6. Check that the 'Notes' section contains any review feedback you added.
7. Ensure the case status reflects the resolution action taken (e.g., 'Resolved' or 'Dismissed').

## Rollback
1. If the case was incorrectly resolved or dismissed, reopen it by selecting the case and choosing 'Reopen case' from the action menu.
2. If notes or feedback were added in error, edit or delete them using the 'Notes' section within the case.
3. If alerts were incorrectly escalated or dismissed, adjust the alert status by selecting the alert and choosing the appropriate action (e.g., 'Dismiss alert' or 'Escalate to investigation').
4. If any user risk score was manually adjusted, revert to the original score by contacting Microsoft support or using the audit log to identify the change and restore it.
5. Ensure that any changes to case assignments or permissions are reversed by reassigning the case to the original owner or restoring default permissions.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
