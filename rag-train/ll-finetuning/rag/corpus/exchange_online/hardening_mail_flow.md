# Hardening: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Hardening

## Scenario / Query
How to configure partner connectors for mail flow without mixing IPs and certificates?

## Environment Context
- **Tenant Type:** Exchange Online
- **Configuration:** Partner connectors

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. IPs and certificates configured in the same partner connector cause precedence issues

## Remediation Steps
1. Use separate connectors for IP-based and certificate-based partner connectors
2. Do not configure IPs and certificates in the same partner connector

## Validation
1. Run Get-InboundConnector | Format-List Name, SenderDomains, TlsSenderCertificateName, SenderIPAddresses to verify that no connector has both SenderIPAddresses and TlsSenderCertificateName populated. 2. For each connector, confirm that either SenderIPAddresses is empty or TlsSenderCertificateName is empty. 3. Test mail flow by sending a test message from each partner domain to a mailbox in the tenant and verify delivery. 4. Review message trace for any authentication or connector matching errors.

## Rollback
1. If a connector was split, recombine the original IP addresses and certificate name into a single connector by running Set-InboundConnector -Identity <ConnectorName> -SenderIPAddresses <IPs> -TlsSenderCertificateName <CertificateName>. 2. Remove any newly created duplicate connectors with Remove-InboundConnector -Identity <NewConnectorName>. 3. Verify mail flow returns to previous state by sending test messages and checking message trace.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
