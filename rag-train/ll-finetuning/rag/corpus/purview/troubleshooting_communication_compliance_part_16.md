# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate and remediate an alert triggered by a meeting transcript policy match in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy with conditions for meeting transcripts

## Symptoms
- Alert triggers when policy detects a transcript containing offending content

## Error Codes
N/A

## Root Causes
1. Meeting transcript contains content matching policy conditions such as classifiers, sensitive info types, or keywords

## Remediation Steps
1. Select the Source tab and review the transcript for the offending content; the transcript automatically scrolls to the line containing the policy match, with the offensive keyword or phrase highlighted
2. Use the Plain text tab for a line-by-line review of the text, including start and stop times in relation to the overall meeting time; text is captured 30 seconds before and after the offending communication
3. Select the Translation tab to review translations in up to eight languages for the Plain text tab; messages in other languages are automatically converted to the display language of the reviewer
4. Select the User history tab to see a historical view of all user message remediation activities, such as past notifications and escalations for policy matches
5. Use Resolve, Notify, Tag as, Escalate, and Escalate for investigation options to resolve the alert

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. Select the policy that triggered the alert. 2. Under the Alerts tab, locate the specific alert for the meeting transcript match. 3. Click on the alert to open the message details pane. 4. Select the Source tab and verify that the transcript automatically scrolls to the line containing the policy match and that the offending keyword or phrase is highlighted. 5. Select the Plain text tab and confirm that the text is displayed line-by-line with start and stop times relative to the overall meeting time, and that 30 seconds of text before and after the offending communication is included. 6. Select the Translation tab and verify that translations in up to eight languages are available for the Plain text tab. 7. Select the User history tab and confirm that historical remediation activities (e.g., past notifications, escalations) for the user are displayed. 8. Confirm that the Resolve, Notify, Tag as, Escalate, and Escalate for investigation options are available and functional.

## Rollback
1. If the remediation actions (e.g., Resolve, Notify, Tag as, Escalate) were applied incorrectly, navigate back to the same alert in Communication Compliance. 2. If the alert was resolved, use the 'Reopen' option (if available) to revert the resolution status. 3. If a notification was sent, there is no direct rollback; inform the recipient that the notification was sent in error and provide corrected information. 4. If the alert was escalated, contact the escalation team to cancel or correct the escalation. 5. If the alert was tagged, remove or change the tag by selecting the alert and choosing a different tag or clearing the tag. 6. If the alert was escalated for investigation, contact the investigation team to withdraw or correct the escalation. 7. Document the rollback actions taken for audit purposes.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
