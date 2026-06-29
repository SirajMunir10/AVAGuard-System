# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator is configuring a connector to route outbound email through a third-party email security gateway. After creating the connector, messages sent from internal users to external recipients are not being routed through the gateway. What configuration step is missing?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Outbound connector configured with 'Route email through these smart hosts' set to the gateway's FQDN

## Symptoms
- Outbound messages bypass the third-party gateway
- Message trace shows delivery directly to external recipients
- No errors in Exchange admin center or message trace

## Error Codes
N/A

## Root Causes
1. The connector's 'Scoping' setting is not configured to apply to all outbound messages
2. The connector is not set as the default outbound connector for the organization

## Remediation Steps
1. In the Exchange admin center, navigate to Mail flow > Connectors and select the outbound connector.
2. Under 'Scoping', select 'All outbound mail' to ensure the connector applies to all outbound messages.
3. Alternatively, use the Exchange Online PowerShell cmdlet: Set-OutboundConnector -Identity "ConnectorName" -AllAcceptedDomains $true -ConnectorType OnPremises
4. Verify the connector's 'UseMXRecord' property is set to $false when using smart hosts.

## Validation
Send a test message from an internal user to an external recipient and run a message trace. Confirm the message was routed through the smart host IP address.

## Rollback
Set the connector scoping back to 'Only when I have a transport rule set up that redirects messages to this connector' or set -AllAcceptedDomains to $false.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-for-email-routing>
