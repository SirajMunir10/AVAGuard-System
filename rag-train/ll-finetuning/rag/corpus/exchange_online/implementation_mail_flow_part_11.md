# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
How do I create a connector to add security restrictions for email sent between Microsoft 365 and a partner organization?

## Environment Context
- **Tenant Type:** Microsoft 365 or Office 365
- **Configuration:** Partner connector for mail flow

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a partner connector that defines boundaries and restrictions for email sent to or received from your partners.
2. Scope the connector to receive email from specific IP addresses.
3. Require TLS encryption.

## Validation
1. Run the following Exchange Online PowerShell command to verify the connector exists and its configuration: Get-InboundConnector | Where-Object {$_.Name -eq "Partner Connector Name"} | Format-List Name, SenderDomains, TlsSettings, RestrictDomains, IPBlockList, SenderIPAddresses. 2. Confirm the connector's SenderIPAddresses includes the partner's IP addresses. 3. Confirm TlsSettings is set to 'DomainValidation' or 'CertificateValidation' as required. 4. Send a test email from the partner domain to a mailbox in your tenant and verify it is received and TLS is enforced (check message headers for 'TLS' or 'RequiredTLS').

## Rollback
1. Run the following Exchange Online PowerShell command to remove the connector: Remove-InboundConnector -Identity "Partner Connector Name" -Confirm:$false. 2. If the connector was created but needs modification, run: Set-InboundConnector -Identity "Partner Connector Name" -SenderIPAddresses @() -TlsSettings $null -RestrictDomains $false. 3. Verify mail flow resumes without restrictions by sending a test email from the partner domain.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
