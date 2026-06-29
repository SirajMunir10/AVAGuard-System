# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I start remediation actions for a communication compliance alert?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance alert management

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
4. Optionally, summarize a lengthy message by using Microsoft Copilot in Microsoft Purview
5. Review the history of closed policy matches on the Resolved tab

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy associated with the alert. 3. On the Policy details page, confirm the 'Pending' tab shows the alert item with status 'Pending'. 4. Click the alert item to open the message details pane. 5. Verify that the message details, including sender, recipients, and flagged content, are displayed. 6. If using Copilot, click 'Summarize' and confirm a summary is generated. 7. On the 'Resolved' tab, confirm that previously resolved items show a status of 'Resolved' and have an associated resolution note.

## Rollback
1. If a message was incorrectly resolved, navigate to the 'Resolved' tab of the policy. 2. Select the message and click 'Reopen' to move it back to the 'Pending' tab. 3. If a message was incorrectly tagged (e.g., as a false positive), remove the tag by editing the message details. 4. If a message was escalated to another reviewer, cancel the escalation by selecting the message and clicking 'Remove escalation'. 5. If a message was forwarded to an external reviewer, recall the email if possible or notify the reviewer to disregard. 6. If a message was deleted, restore it from the 'Deleted items' folder in the policy (if available) or contact Microsoft Support for recovery.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
