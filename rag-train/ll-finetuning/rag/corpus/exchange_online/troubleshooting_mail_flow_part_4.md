# Troubleshooting: Mail Flow (550 5.7.1)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that emails sent to recipients in a specific external domain are being delayed or not delivered. How do I troubleshoot mail flow issues using Exchange Online message trace and the Get-MessageTrace PowerShell cmdlet?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Default mail flow settings with no custom connectors for the affected domain

## Symptoms
- Emails to recipients in a specific external domain are delayed or not delivered
- Sender receives non-delivery reports (NDRs) with error codes like 550 5.7.1
- Message trace shows the messages as 'Pending' or 'FilteredAsSpam'

## Error Codes
- `550 5.7.1`

## Root Causes
1. The recipient domain may be blocked by Exchange Online Protection (EOP) due to high spam confidence level (SCL)
2. The sender's IP may be on a block list
3. Mail flow rules (transport rules) may be intercepting the messages

## Remediation Steps
1. Run a message trace in the Exchange admin center (EAC) under Mail flow > Message trace, or use the Exchange Online PowerShell cmdlet Get-MessageTrace with parameters like -SenderAddress and -RecipientAddress to identify the status of the messages.
2. If the trace shows 'FilteredAsSpam', check the spam filter policy (Get-HostedContentFilterPolicy) and ensure the sender or domain is not incorrectly blocked.
3. If the trace shows 'Pending', verify that the recipient domain's MX record is correct and that there are no connectivity issues by using the Remote Connectivity Analyzer (testconnectivity.microsoft.com).
4. If an NDR with code 550 5.7.1 is received, check if the recipient domain has a mail flow rule that rejects messages from your tenant, and contact the recipient's admin to resolve.
5. Review mail flow rules (Get-TransportRule) to ensure no rule is blocking messages to that domain.

## Validation
After remediation, run a new message trace for a test email to the same recipient domain and confirm the delivery status is 'Delivered'.

## Rollback
If a mail flow rule was modified, restore the original rule by using Set-TransportRule with the previous parameters. If a spam filter policy was changed, revert to the default policy using Set-HostedContentFilterPolicy -Identity Default.

## References
- <https://learn.microsoft.com/en-us/powershell/module/exchange/get-messagetrace>
- <https://learn.microsoft.com/en-us/exchange/antispam-and-antimalware/antispam-protection/antispam-protection>
