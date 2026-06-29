# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
How to set up connectors for mail flow in Exchange Online given the new terminology changes?

## Environment Context
- **Tenant Type:** Microsoft 365 or Office 365
- **Configuration:** Connectors for mail flow

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Specify the start and end points for the connector instead of using the terms 'inbound' and 'outbound'.
2. Note that inbound means into Microsoft 365 or Office 365; outbound means from Microsoft 365 or Office 365.

## Validation
1. Verify the connector's start and end points in the Exchange admin center: navigate to Mail flow > Connectors, select the connector, and confirm the 'From' and 'To' fields correctly reflect the intended mail flow direction (e.g., 'From: Your organization's email server' and 'To: Microsoft 365' for inbound mail into Microsoft 365).
2. Run the Exchange Online PowerShell command: Get-OutboundConnector | Format-List Name,ConnectorType,RecipientDomains (for outbound connectors) or Get-InboundConnector | Format-List Name,ConnectorType,SenderDomains (for inbound connectors) and verify the ConnectorType property matches the expected direction (e.g., 'OnPremises' for inbound into Microsoft 365, 'Partner' for outbound from Microsoft 365).
3. Send a test email from an external domain to a Microsoft 365 mailbox and confirm delivery; send a test email from a Microsoft 365 mailbox to an external domain and confirm delivery.

## Rollback
1. In the Exchange admin center, navigate to Mail flow > Connectors, select the connector, and click 'Edit'. Revert the 'From' and 'To' fields to the previous values if they were changed.
2. If the connector was newly created, delete it by selecting the connector and clicking 'Delete'.
3. In Exchange Online PowerShell, use Remove-OutboundConnector -Identity "ConnectorName" or Remove-InboundConnector -Identity "ConnectorName" to remove the connector.
4. Re-apply any previous connector configuration from backup or documentation, ensuring the start and end points are set according to the original terminology (e.g., 'Inbound' or 'Outbound' if previously used).

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
