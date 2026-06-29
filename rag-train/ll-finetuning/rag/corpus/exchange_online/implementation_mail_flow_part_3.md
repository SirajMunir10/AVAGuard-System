# Implementation: Mail Flow (451 4.7.0)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
An organization is implementing Exchange Online and needs to ensure that all outbound email is sent over TLS 1.2 or higher. They have configured a connector but are unsure if the connector enforces TLS and which cipher suites are used. How can they verify and enforce TLS 1.2 for outbound mail flow?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise (E5)
- **Configuration:** Outbound connector configured in Exchange admin center; TLS settings not explicitly set

## Symptoms
- Outbound email delivery fails to recipients that require TLS 1.2
- Messages are queued with a 451 4.7.0 Temporary server error
- SMTP logs show TLS version negotiation below 1.2

## Error Codes
- `451 4.7.0`

## Root Causes
1. The outbound connector does not have the 'Require TLS' option enabled
2. The connector's TLS version is not restricted to 1.2 or higher
3. The on-premises or partner server does not support TLS 1.2

## Remediation Steps
1. In the Exchange admin center, navigate to Mail flow > Connectors and select the outbound connector.
2. Under 'Security', set 'Require TLS' to 'Yes'.
3. Under 'TLS version', select 'TLS 1.2' (or higher) from the dropdown.
4. Save the connector and test mail flow using the built-in validation in EAC or by sending a test message and reviewing message trace.
5. Alternatively, use Exchange Online PowerShell: Set-OutboundConnector -Identity "ConnectorName" -RequireTLS $true -TlsVersion "TLS 1.2"

## Validation
Run Get-OutboundConnector | Format-List Name,RequireTLS,TlsVersion to confirm settings. Then send a test email and verify in message trace that the 'TLS' property shows '1.2'.

## Rollback
Set-OutboundConnector -Identity "ConnectorName" -RequireTLS $false -TlsVersion "TLS 1.0"

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-for-mail-flow>
