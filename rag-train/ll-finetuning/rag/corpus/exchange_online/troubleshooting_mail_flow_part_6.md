# Troubleshooting: Mail Flow (451 4.7.500-699 (ASxxx))

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Troubleshooting

## Scenario / Query
How do I avoid graylisting that occurs due to large volumes of mail sent between Microsoft 365 or Office 365 and my on-premises environment or partners?

## Environment Context
- **Tenant Type:** Microsoft 365 or Office 365
- **Configuration:** On-premises environment or partners

## Symptoms
- Graylisting slows down suspiciously large amounts of email by throttling the message sources based on their IP addresses.
- Microsoft 365 or Office 365 responds to these abnormal influxes of mail by returning a temporary non-delivery report error (also known as an NDR or bounce message) in the range 451 4.7.500-699 (ASxxx).

## Error Codes
- `451 4.7.500-699 (ASxxx)`

## Root Causes
1. Large volume of mail that's regularly sent between your Microsoft 365 or Office 365 organization and your on-premises environment or partners.

## Remediation Steps
1. Use connectors to avoid graylisting that would otherwise occur due to the large volume of mail that's regularly sent between your Microsoft 365 or Office 365 organization and your on-premises environment or partners.

## Validation
1. Verify that connectors are configured correctly: Run `Get-InboundConnector` and `Get-OutboundConnector` in Exchange Online PowerShell to confirm that connectors exist for the on-premises environment or partner. 2. Check that the connector's `SenderDomains` or `IPAddresses` include the expected sources. 3. Send a test message from the on-premises environment or partner to a Microsoft 365 mailbox and confirm it is not delayed or returned with a 451 4.7.500-699 error. 4. Review message trace in Exchange admin center for the test message to ensure it was routed through the connector and not throttled.

## Rollback
1. Remove the connector(s) that were added: Run `Remove-InboundConnector -Identity "ConnectorName"` and `Remove-OutboundConnector -Identity "ConnectorName"` in Exchange Online PowerShell. 2. If existing connectors were modified, restore their original settings using `Set-InboundConnector` or `Set-OutboundConnector` with the previous parameters. 3. Monitor mail flow to confirm that graylisting behavior returns to the previous state (i.e., throttling resumes for large volumes). 4. If needed, re-enable any transport rules or restrictions that were disabled during remediation.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/fix-email-delivery-issues-for-error-code-451-4-7-500-699-asxxx-in-exchange-online>
