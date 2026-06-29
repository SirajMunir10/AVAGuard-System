# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
How to specify domain or IP address ranges when creating a connector for a partner organization to ensure secure mail flow?

## Environment Context
- **Tenant Type:** Exchange Online
- **Configuration:** Connector configuration for partner organization

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When you create a connector, specify the domain or IP address ranges that your partner sends mail from.
2. If email messages don't meet the security conditions that you set on the connector, the message will be rejected.

## Validation
1. Run the following Exchange Online PowerShell command to verify the connector's domain or IP address restrictions: Get-InboundConnector -Identity "PartnerConnectorName" | Format-List SenderDomains, TlsSenderCertificateName, RestrictDomainsToIPAddresses, IPAllowList. 2. Send a test email from the partner's specified domain or IP range to a mailbox in your organization and confirm it is delivered. 3. Send a test email from a domain or IP address not in the allowed list and verify it is rejected with a non-delivery report (NDR) indicating the connector security condition was not met.

## Rollback
1. If the connector was just created and causes issues, remove it using: Remove-InboundConnector -Identity "PartnerConnectorName". 2. If the connector was modified, revert to previous settings by updating the connector with the original domain or IP address ranges using: Set-InboundConnector -Identity "PartnerConnectorName" -SenderDomains @("originaldomain.com") -IPAllowList @("originalIPrange"). 3. If the connector was enabled and needs to be disabled temporarily, run: Set-InboundConnector -Identity "PartnerConnectorName" -Enabled $false.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow#additional-partner-organization-connector-options>
