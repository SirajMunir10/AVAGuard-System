# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How do I resolve a communication compliance policy match and optionally mark it as misclassified?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance roles: Communication Compliance, Communication Compliance Investigators, Communication Compliance Analyst

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Resolve to immediately remove the message from the Pending queue and prevent any further action on the message.
2. When you select Resolve, you close the message without further classification.
3. You can also mark the message as misclassified if the alerting process or any Microsoft provided trainable classifiers incorrectly generated it.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with an account that has the Communication Compliance, Communication Compliance Investigators, or Communication Compliance Analyst role.
2. Navigate to Communication Compliance > Policies > select the relevant policy.
3. Under the 'Pending' tab, confirm the specific message is no longer listed.
4. Optionally, check the 'Resolved' tab to verify the message appears there with a status of 'Resolved' or 'Misclassified' (if marked as misclassified).
5. If the message was marked as misclassified, confirm that the 'Misclassified' flag is visible in the message details.

## Rollback
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with an account that has the Communication Compliance, Communication Compliance Investigators, or Communication Compliance Analyst role.
2. Navigate to Communication Compliance > Policies > select the relevant policy.
3. Under the 'Resolved' tab, locate the message that was resolved.
4. Select the message to open its details.
5. If the message was marked as misclassified, remove the misclassification flag by editing the message classification (if the interface allows) or by re-escalating the message for review.
6. If the message needs to be returned to the pending queue, use the 'Reassign' or 'Escalate' option (if available) to send it back for further investigation. Note: Direct reversal of 'Resolve' may not be supported; re-escalation is the recommended recovery action.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
