# Troubleshooting: Mail Flow (550 5.7.1)

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that emails sent to a specific external domain are being delayed or not delivered. How do I troubleshoot mail flow issues using Exchange Online message trace and identify the root cause?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise
- **Configuration:** Default mail flow rules and connector settings

## Symptoms
- Emails to a specific external domain are delayed or not delivered
- Sender receives non-delivery report (NDR) with error code 550 5.7.1
- Message trace shows status 'Failed' or 'Pending' for the affected domain

## Error Codes
- `550 5.7.1`

## Root Causes
1. Mail flow rule (transport rule) blocking messages to the domain
2. Connector misconfiguration (e.g., TLS settings, IP restrictions)
3. External domain's mail server rejecting messages due to sender reputation or policy

## Remediation Steps
1. Run a message trace in the Exchange admin center (EAC) for the affected user and domain to identify the failure point.
2. Review mail flow rules in EAC > Mail flow > Rules to check if any rule blocks or modifies messages to the domain.
3. Check connectors in EAC > Mail flow > Connectors for correct configuration (e.g., TLS, IP allow list).
4. If the issue is with the external domain, contact the recipient's IT team to verify their mail server policies.
5. Use Get-MessageTrace and Get-MessageTraceDetail in Exchange Online PowerShell to retrieve detailed delivery information.

## Validation
Run a new message trace after remediation to confirm successful delivery to the domain.

## Rollback
Disable or modify any mail flow rule that was changed, or revert connector settings to previous values.

## References
- <https://learn.microsoft.com/en-us/exchange/monitoring/trace-an-email-message/run-a-message-trace-and-view-results>
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/troubleshoot-mail-flow>
