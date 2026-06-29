# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator is configuring a connector to route outbound email through an on-premises email security gateway. After creating the connector, outbound messages are not being routed through the gateway and instead are delivered directly to external recipients. What configuration step is missing?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise (E5)
- **Configuration:** Outbound connector configured with 'Route email through these smart hosts' pointing to the on-premises gateway IP address, but the connector's 'Scoping' setting is not set to 'On'.

## Symptoms
- Outbound messages bypass the on-premises gateway and are delivered directly to external recipients.
- No messages appear in the on-premises gateway's mail flow logs.
- The connector status shows as 'Enabled' but no mail is routed through it.

## Error Codes
N/A

## Root Causes
1. The connector's 'Scoping' setting is not enabled. When scoping is off, the connector applies to all outbound messages but may be overridden by other routing rules. When scoping is on, the connector is used only for messages sent from domains specified in the connector's 'Accepted domains' list.

## Remediation Steps
1. 1. Sign in to the Exchange admin center (EAC) at https://admin.exchange.microsoft.com.
2. 2. Navigate to Mail flow > Connectors.
3. 3. Select the outbound connector that should route mail through the on-premises gateway.
4. 4. In the connector properties, go to the 'Scoping' section.
5. 5. Set 'Scoping' to 'On' and specify the accepted domains that should be routed through this connector.
6. 6. Save the connector configuration.
7. 7. Send a test message from a domain listed in the scoping settings and verify it arrives at the on-premises gateway.

## Validation
After enabling scoping and specifying the correct accepted domain, outbound messages for that domain are routed through the on-premises gateway. Use the message trace in the Exchange admin center to confirm the connector was used.

## Rollback
Set 'Scoping' back to 'Off' to revert to the previous routing behavior where the connector applies to all outbound messages (or none, depending on other connectors).

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/scoping-connectors>
