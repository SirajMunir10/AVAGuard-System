# Implementation: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Implementation

## Scenario / Query
When do I need to set up a connector in Exchange Online for mail flow?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange Online connectors

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Check if you use the Built-in security add-on for on-premises mailboxes.
2. Check if you have your own on-premises email servers, no Exchange Online mailboxes, and licenses for the Built-in security add-on for on-premises mailboxes.
3. Check if some of your mailboxes are on your on-premises email servers and some are in Exchange Online.
4. Check if all mailboxes are in Exchange Online but you need to send email from printers, fax machines, apps, or other devices.
5. Check if you frequently exchange sensitive information with business partners and want to apply security restrictions using TLS or IP address limits.

## Validation
1. Run `Get-InboundConnector` and `Get-OutboundConnector` in Exchange Online PowerShell to list all connectors. 2. Verify that the connector type (OnPremises, Partner) matches the scenario (e.g., hybrid, partner TLS). 3. For hybrid scenarios, confirm the connector points to your on-premises smart host and uses TLS. 4. For partner connectors, verify TLS settings and IP restrictions are applied. 5. Send a test email from on-premises to Exchange Online and vice versa, then check message trace for connector usage.

## Rollback
1. Run `Remove-InboundConnector -Identity "ConnectorName"` and `Remove-OutboundConnector -Identity "ConnectorName"` to delete misconfigured connectors. 2. If the connector was created for a specific scenario, revert to the previous mail flow configuration (e.g., disable hybrid mode, remove partner restrictions). 3. Re-enable any default connectors that were disabled. 4. Verify mail flow resumes using default Exchange Online routing by sending test emails and checking message trace.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
