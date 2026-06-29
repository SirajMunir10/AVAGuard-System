# Implementation: Mail Flow (554 5.4.0 SMTPSEND.DNS.NonExistentDomain)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator has configured a new connector in Exchange Online to route all outbound email through a third-party email security gateway. After the connector is created, outbound mail delivery fails with a '554 5.4.0 SMTPSEND.DNS.NonExistentDomain' error. What is the likely root cause and how should it be remediated?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Outbound connector configured with MX record routing to a third-party gateway

## Symptoms
- Outbound email delivery fails with non-delivery report (NDR)
- NDR contains error code 554 5.4.0 SMTPSEND.DNS.NonExistentDomain

## Error Codes
- `554 5.4.0 SMTPSEND.DNS.NonExistentDomain`

## Root Causes
1. The connector's 'MX record' routing option is incorrectly used for outbound mail, causing Exchange Online to attempt delivery to the recipient's MX record instead of the specified smart host
2. The connector's smart host FQDN is misconfigured or does not resolve in DNS

## Remediation Steps
1. Edit the outbound connector in the Exchange admin center
2. Change the 'Routing' setting from 'MX record' to 'Smart host'
3. Enter the correct FQDN of the third-party email security gateway as the smart host
4. Ensure the smart host FQDN resolves correctly in public DNS

## Validation
Send a test message to an external recipient and verify successful delivery without NDR. Use the Exchange admin center message trace to confirm the message was routed through the connector.

## Rollback
Delete or disable the outbound connector and revert to default Exchange Online outbound routing.

## References
- <https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/email-delivery-issues-error-code-554-5-4-0>
