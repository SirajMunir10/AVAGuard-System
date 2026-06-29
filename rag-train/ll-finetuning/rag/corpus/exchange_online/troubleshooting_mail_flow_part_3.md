# Troubleshooting: Mail Flow (550 5.7.1)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that emails sent to a specific external domain are being delayed or not delivered. How do I troubleshoot mail flow issues in Exchange Online?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Default mail flow settings, no custom connectors

## Symptoms
- Emails to a specific external domain are delayed or not delivered
- Sender receives non-delivery reports (NDRs) with error codes like 550 5.7.1
- Messages remain in the outbound queue for an extended period

## Error Codes
- `550 5.7.1`

## Root Causes
1. The recipient's email server is rejecting messages due to spam or policy reasons
2. The sender's IP or domain is on a blocklist
3. DNS issues, such as missing or incorrect MX records for the recipient domain

## Remediation Steps
1. Use the Exchange admin center (EAC) to run a message trace for the affected messages to identify where they are being delayed or rejected.
2. Check the message trace details for any error codes or diagnostic information.
3. If the error code is 550 5.7.1, verify that the sender's domain is not listed on any public blocklists and that the recipient's server is not rejecting the message due to SPF, DKIM, or DMARC failures.
4. Ensure that the recipient domain's MX record is correctly configured by using nslookup or a DNS checker.
5. If the issue persists, contact the recipient's email administrator to resolve any server-side blocks.

## Validation
Run a new message trace to confirm that subsequent emails to the same domain are delivered successfully.

## Rollback
If changes were made to SPF, DKIM, or DMARC records, revert them to their previous values using the DNS hosting provider's interface.

## References
- <https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/email-delivery-issues>
