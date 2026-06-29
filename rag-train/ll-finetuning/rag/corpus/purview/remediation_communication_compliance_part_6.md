# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How to remove inappropriate messages in Teams using Communication Compliance policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policies with machine-learning and classifier-based detection

## Symptoms
- Inappropriate messages detected in Microsoft Teams channels, 1:1 chats, or group chats
- Messages reported by users or flagged by machine-learning/classifier-based policies

## Error Codes
N/A

## Root Causes
1. Policy violation detected by Communication Compliance policy

## Remediation Steps
1. Use Remove message in Teams to block potentially inappropriate messages and content identified in messages from Microsoft Teams channels and 1:1 and group chats.
2. This action includes Teams chat messages reported by users and chat messages detected using machine-learning and classifier-based Communication Compliance policies.
3. Removed messages and content are replaced with a policy tip that explains that it's blocked and the policy that applies to its removal from view.
4. Recipients are provided a link in the policy tip to learn more about the applicable policy and the review process.
5. The sender receives a policy tip for the blocked message and content but can review the details of the blocked message and content for context regarding the removal.

## Validation
1. Confirm the Communication Compliance policy is active and assigned to the correct users/groups. 2. In the Microsoft 365 Purview compliance portal, navigate to Communication Compliance > Policies and select the relevant policy. 3. Under the 'Pending' or 'Resolved' tab, locate the flagged message. 4. Verify that the 'Remove message in Teams' action was applied by checking the message's remediation history (e.g., 'Remediation actions' column shows 'Remove message in Teams'). 5. In Microsoft Teams, open the channel or chat where the message was removed. Confirm the original message is replaced with a policy tip stating the message is blocked and includes a link to learn more about the policy. 6. As the sender, check the policy tip for the blocked message and ensure the sender can review the details of the blocked content. 7. As a recipient, verify the policy tip includes a link to the applicable policy and review process.

## Rollback
1. In the Microsoft 365 Purview compliance portal, navigate to Communication Compliance > Policies and select the relevant policy. 2. Under the 'Resolved' tab, locate the message that was removed. 3. Select the message and choose 'Restore message' (if available) to undo the removal and make the original message visible again in Teams. 4. If 'Restore message' is not available, manually re-post the original message content in the Teams channel or chat (ensure compliance with organizational policies). 5. Verify in Teams that the policy tip is no longer displayed and the original message is visible to all participants. 6. Review the policy configuration to adjust classifiers or conditions if the removal was incorrect. 7. Document the rollback action and notify relevant stakeholders (e.g., compliance team, message sender) as per organizational procedures.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
