# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
How do I set up connectors to route mail between Microsoft 365 or Office 365 and my own email servers?

## Environment Context
- **Tenant Type:** Microsoft 365 or Office 365
- **Configuration:** accepted domains must be configured before setting up connectors

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the accepted domains for Microsoft 365 or Office 365. For more information, see Manage accepted domains in Exchange Online.
2. Set up connectors to route mail between Microsoft 365 or Office 365 and your own email servers.
3. Set up connectors for secure mail flow with a partner organization.

## Validation
1. Verify accepted domains are configured: Run 'Get-AcceptedDomain | Format-List Name, DomainType, Default' in Exchange Online PowerShell. Confirm the domain you intend to route mail for appears with the correct DomainType (Authoritative or InternalRelay).
2. Verify connectors exist: Run 'Get-InboundConnector | Format-List Name, ConnectorType, TlsSettings' and 'Get-OutboundConnector | Format-List Name, ConnectorType, TlsSettings'. Confirm connectors with the expected names and settings are present.
3. Test mail flow: Send a test message from an external mailbox to a recipient in your on-premises environment, and from your on-premises environment to an external mailbox. Verify delivery and that messages are routed through the connectors as intended.

## Rollback
1. Remove inbound connector: Run 'Remove-InboundConnector -Identity "<ConnectorName>" -Confirm:$false'.
2. Remove outbound connector: Run 'Remove-OutboundConnector -Identity "<ConnectorName>" -Confirm:$false'.
3. If accepted domains were added or changed, revert to previous configuration: Run 'Set-AcceptedDomain -Identity "<DomainName>" -DomainType <OriginalDomainType>' or 'Remove-AcceptedDomain -Identity "<DomainName>"' if the domain was newly added and should not remain.
4. Verify mail flow returns to previous behavior by sending test messages.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
