# Troubleshooting: Mail Flow (550 5.7.1)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that emails sent to a specific external domain are being delayed or not delivered. How can I troubleshoot this issue using Exchange Online message trace and the Get-MessageTrace PowerShell cmdlet?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Default mail flow settings; no custom connectors or transport rules affecting the domain

## Symptoms
- Emails to a specific external domain are delayed or not delivered
- Sender receives non-delivery report (NDR) with status code 550 5.7.1 or 450 4.7.1
- Message trace shows status 'Pending' or 'Failed' for messages to that domain

## Error Codes
- `550 5.7.1`
- `450 4.7.1`

## Root Causes
1. Recipient domain has restrictive SPF/DKIM/DMARC policies causing rejection
2. Recipient mail server is temporarily unavailable or throttling connections
3. Exchange Online has been rate-limited by the recipient server

## Remediation Steps
1. Run Get-MessageTrace -SenderAddress user@contoso.com -RecipientAddress user@fabrikam.com -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) to review message status and details
2. Check the 'StatusDetail' field in the trace output for specific failure reasons
3. If NDR indicates a policy issue, advise the sender to contact the recipient's IT team to adjust SPF/DKIM/DMARC records
4. If the issue is temporary, retry delivery after 24 hours; if persistent, open a support case with Microsoft

## Validation
Run Get-MessageTrace again after remediation to confirm messages to the domain show status 'Delivered'

## Rollback
No rollback required; remediation steps are informational and do not change tenant configuration

## References
- <https://learn.microsoft.com/en-us/exchange/monitoring/trace-an-email-message/run-a-message-trace-and-view-results>
