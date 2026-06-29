# Troubleshooting: Mail Flow (550 5.7.124)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that emails sent to an external recipient are being delayed or not delivered. The sender receives a non-delivery report (NDR) with error code 550 5.7.124. How do I troubleshoot and resolve this issue?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Exchange Online mail flow rules (transport rules) and spam filter policies are configured.

## Symptoms
- Sender receives NDR with error code 550 5.7.124
- Emails to specific external domain are not delivered

## Error Codes
- `550 5.7.124`

## Root Causes
1. The sender's message was blocked by an Exchange Online mail flow rule (transport rule) that restricts messages to certain external domains.

## Remediation Steps
1. 1. Sign in to the Microsoft 365 Defender portal as a Global Administrator or Exchange Administrator.
2. 2. Navigate to Email & Collaboration > Policies & Rules > Threat policies > Anti-spam policies.
3. 3. Review the mail flow rules (transport rules) that apply to the sender or recipient domain.
4. 4. Identify the rule that is blocking the message (look for rules with conditions like 'The recipient domain is...' and action 'Reject the message with the status code 550 5.7.124').
5. 5. Modify the rule to allow the legitimate messages, or remove the rule if it is no longer needed.
6. 6. Alternatively, add the sender or recipient to an allowed list in the connection filter policy or the tenant allow/block list, if appropriate.

## Validation
Ask the sender to resend the email and confirm that it is delivered without an NDR.

## Rollback
If the change causes unintended mail flow, re-enable the original mail flow rule or revert the allow list entry.

## References
- <https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/email-delivery-issues-error-code-550-5-7-124>
