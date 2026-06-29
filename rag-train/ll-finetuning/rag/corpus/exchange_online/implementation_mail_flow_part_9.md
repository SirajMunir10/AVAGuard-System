# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
How do I set up connectors for secure mail flow with a partner organization using TLS or IP restrictions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Set up connectors for secure mail flow with a partner organization

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set up a connector for incoming email from the partner organization to Office 365.
2. Set up a connector for outgoing email from Office 365 to the partner organization.

## Validation
1. Verify the inbound connector: Run `Get-InboundConnector | Format-List Name, SenderDomains, TlsSenderCertificateName, RequireTls, RestrictDomainsToIPAddresses, IPBlockList` in Exchange Online PowerShell. Confirm the connector for the partner organization shows the expected TLS settings or IP restrictions. 2. Verify the outbound connector: Run `Get-OutboundConnector | Format-List Name, RecipientDomains, TlsDomain, RequireTls, UseMxRecord, SmartHosts` and confirm the connector for the partner organization is configured with the correct TLS domain or smart host IPs. 3. Send a test message from the partner domain to an internal recipient and verify it is received without TLS errors. 4. Send a test message from an internal user to the partner domain and verify delivery and TLS compliance using message trace in the Exchange admin center.

## Rollback
1. Remove the inbound connector: Run `Remove-InboundConnector -Identity "<ConnectorName>"` in Exchange Online PowerShell. 2. Remove the outbound connector: Run `Remove-OutboundConnector -Identity "<ConnectorName>"`. 3. If IP restrictions were applied, remove any IP allow/block lists from the connector before deletion. 4. Verify removal by running `Get-InboundConnector` and `Get-OutboundConnector` to confirm the connectors no longer appear.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
