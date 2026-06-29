# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
How do I set up connectors to route mail between Microsoft 365 and my own on-premises email servers when I have Exchange 2016 or later and cloud mailboxes, but do not want a hybrid deployment?

## Environment Context
- **Tenant Type:** Microsoft 365 with on-premises Exchange 2016 or later and Exchange Online cloud mailboxes
- **Configuration:** Built-in security add-on for on-premises mailboxes not available

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Consider whether an Exchange hybrid deployment will better meet your organization's needs by reviewing the article that matches your current situation in Exchange Server Hybrid Deployments.
2. If a hybrid deployment is the right option, use the Hybrid Configuration wizard to integrate Exchange Online with your on-premises Exchange organization.
3. If you don't want a hybrid deployment and only want connectors that enable mail routing, follow the instructions in Set up connectors to route mail between Microsoft 365 and your own email servers.

## Validation
1. Verify that the inbound connector from your on-premises email server to Microsoft 365 is configured correctly by running the following Exchange Online PowerShell command: Get-InboundConnector | Where-Object {$_.ConnectorType -eq 'OnPremises'} | Format-List Name, ConnectorType, SenderDomains, TlsSettings, RequireTls. Confirm that the connector's SenderDomains includes your on-premises domain and that TLS settings match your requirements. 2. Verify that the outbound connector from Microsoft 365 to your on-premises email server is configured correctly by running: Get-OutboundConnector | Where-Object {$_.ConnectorType -eq 'OnPremises'} | Format-List Name, ConnectorType, RecipientDomains, TlsSettings, SmartHosts. Confirm that the RecipientDomains includes your on-premises domain and that SmartHosts points to your on-premises server's FQDN or IP address. 3. Send a test email from an on-premises mailbox to a cloud mailbox and verify delivery within a few minutes. 4. Send a test email from a cloud mailbox to an on-premises mailbox and verify delivery within a few minutes. 5. Check the message trace in the Exchange admin center (EAC) under 'mail flow' > 'message trace' for both test emails to ensure they were routed through the connectors.

## Rollback
1. Remove the inbound connector by running: Remove-InboundConnector -Identity "<InboundConnectorName>" -Confirm:$false. 2. Remove the outbound connector by running: Remove-OutboundConnector -Identity "<OutboundConnectorName>" -Confirm:$false. 3. If you had previously disabled any existing connectors, re-enable them by running: Set-InboundConnector -Identity "<ConnectorName>" -Enabled $true or Set-OutboundConnector -Identity "<ConnectorName>" -Enabled $true. 4. Verify that mail flow returns to its previous state by sending test emails between on-premises and cloud mailboxes and confirming they are not delivered (if that was the previous behavior) or are delivered via the original path. 5. If you made any DNS changes (e.g., MX record updates) as part of the connector setup, revert those changes to the original values.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
