# Implementation: Mail Flow (550 5.7.1)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator configured a new Exchange Online connector for hybrid mail flow, but messages sent from on-premises to Exchange Online are being rejected with a 550 5.7.1 error. What is the likely cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Hybrid (Exchange Online + on-premises Exchange Server)
- **Configuration:** Inbound connector configured to accept messages from the on-premises organization's IP address range

## Symptoms
- Messages from on-premises to Exchange Online are rejected with a 550 5.7.1 error
- The rejection message includes 'Service not available' or 'Client was not authenticated'
- No other mail flow issues are reported for other senders

## Error Codes
- `550 5.7.1`

## Root Causes
1. The inbound connector in Exchange Online is not configured to accept messages from the on-premises IP address, or the connector's certificate validation settings are incorrect
2. The on-premises send connector is not using TLS with the correct certificate that matches the FQDN expected by Exchange Online

## Remediation Steps
1. Verify that the inbound connector in Exchange Online includes the correct on-premises IP address(es) in the 'IP address' list under 'Received from' settings
2. Ensure the inbound connector's 'Require TLS' setting is enabled and the certificate subject name matches the FQDN of the on-premises server
3. On the on-premises Exchange server, verify the send connector's FQDN matches the certificate subject name and that TLS 1.2 is enabled
4. Test mail flow using the Remote Connectivity Analyzer's Exchange Online Outbound SMTP test

## Validation
Send a test message from on-premises to a mailbox in Exchange Online and confirm it is delivered without error. Check the message trace in Exchange admin center for success.

## Rollback
If the connector changes cause issues, revert to the previous connector configuration by restoring from backup or re-entering the original IP addresses and TLS settings.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-for-secure-mail-flow-with-a-partner-organization>
- <https://learn.microsoft.com/en-us/exchange/mail-flow/test-mail-flow-with-remote-connectivity-analyzer>
