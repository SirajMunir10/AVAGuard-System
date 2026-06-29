# Incident Response: Mail Flow Incident Response

**Domain:** Exchange Online
**Subdomain:** Mail Flow Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A user reports that emails sent to a specific external domain are being silently dropped without any non-delivery report (NDR). How do you investigate and remediate this issue in Exchange Online?

## Environment Context
- **Tenant Type:** Enterprise Microsoft 365 tenant with Exchange Online
- **Configuration:** Default mail flow rules (transport rules) and connector settings

## Symptoms
- Emails to a particular external domain are not delivered
- Sender does not receive an NDR or bounce-back message
- Message trace shows the message as 'Delivered' but the recipient never receives it
- No quarantine or spam filter notifications for the affected messages

## Error Codes
N/A

## Root Causes
1. A mail flow rule (transport rule) is configured to silently drop messages to the affected domain
2. A connector is misconfigured to reject or redirect messages to the domain
3. The external domain has a restrictive mail exchange (MX) record or is blocking messages without an NDR

## Remediation Steps
1. Use the Exchange admin center or Exchange Online PowerShell to identify the mail flow rule causing the issue: Get-TransportRule | Format-List Name,State,Description,Priority,RejectMessageReasonText,DeleteMessage
2. If a rule is found with 'DeleteMessage' action, disable or modify the rule to allow delivery: Disable-TransportRule -Identity "RuleName"
3. Review connector settings for the affected domain: Get-InboundConnector | Format-List Name,SenderDomains,TlsSettings
4. If a connector is misconfigured, update or remove it: Set-InboundConnector -Identity "ConnectorName" -SenderDomains @{remove="domain.com"}
5. Verify message trace after changes to confirm delivery: Get-MessageTrace -SenderAddress user@contoso.com -RecipientAddress user@externaldomain.com

## Validation
Send a test email from the affected user to the external domain and confirm delivery using Get-MessageTrace. Check that the message appears with status 'Delivered' and the recipient receives it.

## Rollback
Re-enable the mail flow rule if it was disabled for testing: Enable-TransportRule -Identity "RuleName". Restore any connector changes by re-adding the domain to the connector's SenderDomains list.

## References
- <https://learn.microsoft.com/en-us/powershell/module/exchange/get-transportrule>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/set-inboundconnector>
