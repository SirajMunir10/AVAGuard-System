# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to examine message details in Communication Compliance to determine remediation actions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy configured

## Symptoms
- Message sentiment shows 'Not available' for unsupported file formats
- Message sentiment shows 'Scanning' while processing

## Error Codes
N/A

## Root Causes
1. Sentiment analysis not available for image attachments, OCR text, or Teams transcript recordings
2. Message exceeds 5,120 words
3. File format not supported for sentiment analysis

## Remediation Steps
1. Select a message to view the complete message header and body information
2. Use the Sentiment column to prioritize messages: Positive (lower priority), Negative (prioritize), Neutral (neither positive nor negative)
3. For lengthy messages, use Copilot in Microsoft Purview to summarize the message including attachments, transcripts, and recordings

## Validation
1. In the Microsoft Purview compliance portal, navigate to Communication Compliance > Policies and select the relevant policy. 2. Open the Messages tab and locate a message that previously showed 'Not available' or 'Scanning' sentiment. 3. Verify that the message header and body are fully displayed and that the Sentiment column now shows 'Positive', 'Negative', or 'Neutral' (or remains 'Not available' only for unsupported formats). 4. For a message exceeding 5,120 words, confirm that Copilot in Microsoft Purview can generate a summary including attachments, transcripts, and recordings. 5. Confirm that no error messages appear and that the message details are actionable for remediation.

## Rollback
1. If sentiment values revert to 'Not available' or 'Scanning', re-select the message to refresh its details. 2. If Copilot summary fails, manually review the full message body and attachments. 3. If the policy configuration was changed during remediation, restore the original policy settings from the policy history or backup. 4. If issues persist, contact Microsoft Support with the message ID and policy name.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
