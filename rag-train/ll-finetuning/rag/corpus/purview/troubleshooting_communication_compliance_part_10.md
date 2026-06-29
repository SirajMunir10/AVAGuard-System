# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to remediate a message that is misclassified in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy with trainable classifier

## Symptoms
- Message appears in Pending queue but is spurious or incorrectly matched to a policy

## Error Codes
N/A

## Root Causes
1. Message misclassified by policy

## Remediation Steps
1. Select Resolve and Item was misclassified to leave a note in the item's history that it's misclassified and remove it from the Pending queue
2. To share misclassified content with Microsoft, select Send message content, attachments, and subject to remove it from the Pending queue and report the items to Microsoft

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the relevant policy and review the Pending queue to confirm the misclassified message is no longer listed. 3. Check the item's history to verify the 'Resolve and Item was misclassified' note is recorded. 4. If reported to Microsoft, confirm the message content, attachments, and subject were sent and removed from the Pending queue.

## Rollback
1. If the message was incorrectly removed from the Pending queue, contact Microsoft Support to restore the item from the audit log. 2. If reported to Microsoft, there is no automated rollback; contact Microsoft Support to request removal of the reported data from Microsoft's systems. 3. Re-evaluate the policy's trainable classifier settings to prevent future misclassifications.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
