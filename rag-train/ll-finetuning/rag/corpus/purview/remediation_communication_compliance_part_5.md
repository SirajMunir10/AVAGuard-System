# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How to remove a message in Teams using Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy with machine-learning or classifier-based detection

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Remove message in Teams to block potentially inappropriate messages and content identified in messages from Microsoft Teams channels and 1:1 and group chats.
2. This action includes Teams chat messages reported by users and chat messages detected using machine-learning and classifier-based Communication Compliance policies.
3. Removed messages and content are replaced with a policy tip that explains that it's blocked and the policy that applies to its removal from view.
4. Recipients are provided a link in the policy tip to learn more about the applicable policy and the review process.

## Validation
1. Confirm the message was removed: In the Communication Compliance investigation view, locate the message that was removed. Verify that the message content is no longer visible and is replaced with a policy tip stating 'This message has been blocked' or similar, including a link to the applicable policy. 2. Check recipient experience: As a test recipient (or via a test user), open the same Teams chat or channel where the message was removed. Confirm that the policy tip appears in place of the original message. 3. Verify audit log: Run the following command in the Microsoft 365 Defender portal or via the Audit log search: Search for 'Removed message from Teams' action by the reviewer. Use the command: `Search-UnifiedAuditLog -Operations 'Removed message from Teams' -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date)` (Exchange Online PowerShell). Confirm the audit record shows the message ID, policy name, and reviewer. 4. Confirm policy tip link: Click the link in the policy tip to ensure it navigates to the correct policy description page (e.g., https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate).

## Rollback
1. If the removal was in error, contact the user who sent the message and request they resend the original content (if appropriate and compliant). 2. To restore the message visibility (if supported by the policy), the reviewer can use the 'Undo removal' option in the Communication Compliance investigation view (if available). Otherwise, no direct rollback exists; the message must be resent. 3. If the policy tip is incorrect or the removal was unintended, modify the Communication Compliance policy to exclude the classifier or rule that triggered the removal. Use the Microsoft 365 Purview compliance portal: Communication Compliance > Policies > Select the policy > Edit > Adjust conditions or classifiers. 4. After policy adjustment, notify affected users that the policy has been updated and that future messages will be evaluated accordingly. 5. If the removal caused a compliance gap (e.g., evidence lost), export the audit log for the removed message using: `Search-UnifiedAuditLog -Operations 'Removed message from Teams' -StartDate <date> -EndDate <date> | Export-Csv -Path 'RemovedMessages.csv'` to retain a record.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
