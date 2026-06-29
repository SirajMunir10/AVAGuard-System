# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How to escalate a message for additional review in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy with configured reviewers

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Escalate to choose other people in your organization who should review the message.
2. Choose from a list of reviewers configured in the Communication Compliance policy to send an email notification requesting additional review of the message.
3. The selected reviewer can use a link in the email notification to go directly to items escalated to them for review.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with an account that has the Communication Compliance Analyst or Administrator role. 2. Navigate to Communication Compliance > Policies and select the relevant policy. 3. Open the policy and go to the 'Pending' or 'Reviewed' tab. 4. Locate the message that was escalated and verify that its status shows 'Escalated' or that the escalation action is recorded in the message details. 5. Confirm that the designated reviewer received an email notification with a direct link to the escalated item. 6. As the designated reviewer, click the link in the email and verify that the message opens in the Communication Compliance review interface.

## Rollback
1. If the escalation was performed in error, the original reviewer can use the 'Resolve' or 'Dismiss' action on the escalated message to remove it from the reviewer's queue. 2. Alternatively, the Communication Compliance Administrator can modify the policy to remove the incorrectly added reviewer from the reviewer list, which will prevent future escalations to that person. 3. If the escalation caused a notification to be sent, the sender can follow up with the reviewer via email to disregard the notification. 4. No automated rollback command exists; manual intervention is required to revert the escalation status.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
