# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to use Power Automate flows to automate process tasks for a message in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance with Power Automate

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use a Power Automate flow to automate process tasks for a message.
2. By default, Communication Compliance includes the 'Notify manager when a user has a Communication Compliance alert' flow template that reviewers can use to automate the notification process for users with message alerts.
3. For more information about creating and managing Power Automate flows in Communication Compliance, see the Consider Power Automate flows documentation.

## Validation
1. Navigate to the Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select a policy and review the 'Power Automate flows' tab to confirm the 'Notify manager when a user has a Communication Compliance alert' flow is listed and enabled. 3. In Power Automate (https://make.powerautomate.com), verify the flow exists under 'My flows' or 'Team flows' and its run history shows successful executions. 4. Trigger a test alert by sending a policy-matching message to a monitored user, then confirm the flow runs and the manager receives the notification.

## Rollback
1. In Power Automate, turn off the flow by selecting it and clicking 'Turn off'. 2. Optionally, delete the flow by selecting 'Delete' and confirming. 3. In Communication Compliance, remove the flow association by editing the policy, navigating to the 'Power Automate flows' tab, and removing the flow. 4. If the flow was the only automation, revert to manual notification processes as documented in the 'Investigate and remediate' article.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
