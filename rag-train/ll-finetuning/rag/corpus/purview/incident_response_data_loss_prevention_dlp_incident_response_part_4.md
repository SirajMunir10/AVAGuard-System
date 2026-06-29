# Incident Response: Data Loss Prevention (DLP) â€“ Incident Response

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) â€“ Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I respond to a DLP alert in Microsoft Purview where a user attempted to share a file containing sensitive information (e.g., credit card numbers) with an external domain, and the policy was configured to audit only?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** DLP policy named 'Credit Card Data â€“ External Sharing' set to 'Audit only' mode, applied to Exchange Online and SharePoint Online

## Symptoms
- DLP alert triggered in Microsoft Purview compliance portal under Alerts
- Alert details show 'Activity: Shared externally' for a file containing credit card numbers
- Policy match rule: 'Credit Card Number â€“ High Confidence'
- User action: 'Blocked' (audit-only policies still log the attempt as blocked in activity explorer)

## Error Codes
N/A

## Root Causes
1. DLP policy was configured in 'Audit only' mode, which logs the activity but does not enforce a block or notify the user
2. User attempted to share a file containing sensitive information (credit card numbers) with an external recipient

## Remediation Steps
1. 1. Review the alert in the Microsoft Purview compliance portal: Navigate to Data Loss Prevention > Alerts, select the alert, and review the activity details.
2. 2. Use Activity Explorer to investigate the specific file and user: Filter by policy name and activity 'Shared externally'.
3. 3. If the file was shared externally, contact the external recipient to request deletion of the file (if still possible).
4. 4. Consider changing the DLP policy action from 'Audit only' to 'Block with override' or 'Block' to prevent future occurrences. This is documented in 'Create and deploy a data loss prevention policy' â€“ see the 'Actions' section.
5. 5. Educate the user on data handling policies and the consequences of sharing sensitive data externally.

## Validation
After changing the policy action to 'Block', attempt to share a test file containing a credit card number with an external domain. Verify that the share is blocked and an alert is generated.

## Rollback
If the policy change causes unintended business disruption, revert the action to 'Audit only' by editing the DLP policy and selecting 'Audit only' under Actions.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dlp-investigate>
- <https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy>
