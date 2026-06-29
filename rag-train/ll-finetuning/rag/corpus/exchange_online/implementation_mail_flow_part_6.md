# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
An organization has enabled the 'Use Exchange Online's built-in Protection' mail flow rule for all internal senders, but external recipients report that messages from the organization are being silently dropped without any non-delivery report (NDR). What is the likely cause and how should the rule be configured to avoid silent message loss?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Mail flow rule (transport rule) with action 'Use Exchange Online's built-in Protection' applied to all internal senders.

## Symptoms
- External recipients do not receive emails sent from internal users
- No NDR is generated for the sender
- Messages are not visible in Exchange message trace as delivered

## Error Codes
N/A

## Root Causes
1. The mail flow rule is configured to reject messages without generating an NDR (e.g., using the 'Reject the message with the explanation' action and setting the rejection code to a value that suppresses NDR generation, or the rule is set to silently delete the message).
2. The rule's action 'Use Exchange Online's built-in Protection' is misapplied: it is intended for outbound messages to apply protection settings, but when combined with a reject or delete action, it can cause silent drops.

## Remediation Steps
1. Identify the mail flow rule using the Exchange admin center or PowerShell: Get-TransportRule -Identity "RuleName" | fl
2. If the rule uses 'Reject the message with the explanation', ensure the rejection code is set to a valid DSN code (e.g., 5.7.1) and that the 'Reject the message with the status code' parameter is not set to a value that suppresses NDR (e.g., 550 5.7.1).
3. If the rule is intended to apply protection, change the action to 'Apply a disclaimer to the message' or 'Set the message header' instead of reject/delete.
4. Test the rule with a small group of users before broad deployment.
5. Review Microsoft documentation on mail flow rule actions: 'Mail flow rule actions in Exchange Online'.

## Validation
Send a test message from an internal user to an external recipient and verify delivery using Exchange message trace. Confirm that the mail flow rule no longer drops the message silently.

## Rollback
Disable or remove the problematic mail flow rule: Disable-TransportRule -Identity "RuleName" or Remove-TransportRule -Identity "RuleName".

## References
- <https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rule-actions>
