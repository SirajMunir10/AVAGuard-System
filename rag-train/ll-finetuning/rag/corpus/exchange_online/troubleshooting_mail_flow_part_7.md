# Troubleshooting: Mail Flow

**Domain:** Exchange Online
**Subdomain:** Mail Flow
**Incident Type:** Troubleshooting

## Scenario / Query
How to view, troubleshoot, and update hybrid connectors after running the Hybrid Configuration Wizard?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Hybrid Configuration Wizard already run

## Symptoms
- Hybrid connectors already configured but need review or modification

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View hybrid connectors on the Connectors page in the EAC
2. Use procedures described in Set up connectors to route mail between Microsoft 365 or Office 365 and your own email servers to troubleshoot and update connectors
3. Re-run the Hybrid Configuration wizard to make changes

## Validation
1. Open the Exchange admin center (EAC) and navigate to Mail flow > Connectors. 2. Verify that the inbound connector from your on-premises organization is present with a status of 'Enabled' and the correct on-premises server(s) listed. 3. Verify that the outbound connector to your on-premises organization is present with a status of 'Enabled' and the correct on-premises server(s) listed. 4. Send a test message from an on-premises mailbox to a Microsoft 365 mailbox and confirm delivery. 5. Send a test message from a Microsoft 365 mailbox to an on-premises mailbox and confirm delivery. 6. Review the message trace for both test messages to ensure they were routed through the hybrid connectors.

## Rollback
1. If connector modifications cause mail flow issues, re-run the Hybrid Configuration Wizard from the on-premises Exchange server to restore default hybrid connectors. 2. Alternatively, manually delete the modified inbound and outbound connectors in the EAC (Mail flow > Connectors) and then re-run the Hybrid Configuration Wizard to recreate them. 3. After re-running the wizard, verify mail flow as described in the validation steps.

## References
- <https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow>
