# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
How to configure connectors with TLS encryption for secure mail flow with a partner organization in Microsoft 365 or Office 365?

## Environment Context
- **Tenant Type:** Microsoft 365 or Office 365
- **Configuration:** Connectors with TLS encryption for mail flow with partner organization

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create two connectors in Microsoft 365 or Office 365.
2. Require TLS for mail flow in both directions.
3. Ensure ContosoBank.com has a valid encryption certificate.
4. Use a certificate from a commercial certification authority (CA) that's automatically trusted by both parties.

## Validation
1. Verify that two connectors are created: run 'Get-InboundConnector' and 'Get-OutboundConnector' in Exchange Online PowerShell to confirm both connectors exist. 2. Check TLS enforcement: for each connector, run 'Get-InboundConnector | fl TlsSenderCertificateName, RequireTls' and 'Get-OutboundConnector | fl TlsDomain, TlsSettings, RequireTls' to confirm TLS is required and the certificate subject name matches ContosoBank.com. 3. Confirm certificate validity: use 'Test-OutboundConnector' and 'Test-InboundConnector' to validate TLS connectivity and certificate trust.

## Rollback
1. Remove the inbound connector: run 'Remove-InboundConnector -Identity "ConnectorName"'. 2. Remove the outbound connector: run 'Remove-OutboundConnector -Identity "ConnectorName"'. 3. If connectors were modified instead of created, revert TLS settings: set 'RequireTls' to $false and clear 'TlsSenderCertificateName' or 'TlsDomain' using Set-*Connector cmdlets. 4. Notify the partner organization to revert any certificate changes if applicable.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
