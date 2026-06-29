# Incident Response: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Incident Response

## Scenario / Query
A user reports that a DLP policy in Microsoft Purview is not triggering alerts for sensitive data shared externally, even though the policy is configured to block and alert. How do you investigate and resolve this issue?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview DLP enabled
- **Configuration:** DLP policy applied to Exchange Online and SharePoint Online, with 'Block with override' action and low-volume alert configured

## Symptoms
- DLP policy does not generate alerts when sensitive data (e.g., credit card numbers) is shared externally via email or SharePoint
- Policy appears as 'Enabled' in the Purview compliance portal but no incidents are recorded in the Activity Explorer
- Users are not blocked or warned when attempting to share sensitive data externally

## Error Codes
N/A

## Root Causes
1. The DLP policy is not applied to the correct workload (e.g., missing Exchange or SharePoint location)
2. The policy's 'Instance count' threshold is set too high, preventing alerts for low-volume matches
3. The sensitive information type (e.g., Credit Card Number) is not correctly configured or is disabled in the tenant

## Remediation Steps
1. Verify that the DLP policy includes the affected workload (Exchange, SharePoint, OneDrive) under 'Locations' in the Purview compliance portal
2. Check the policy's 'Instance count' and 'Match accuracy' settings; reduce the instance count to 1 and ensure accuracy is set to 'High confidence' for testing
3. Confirm that the sensitive information type (e.g., 'Credit Card Number') is enabled and correctly defined in the 'Sensitive info types' library
4. Use the 'Test with sample data' feature in the DLP policy to validate detection
5. Review the 'Activity Explorer' for any filtered or missed events; ensure the user has appropriate audit logging permissions

## Validation
After remediation, send a test email containing a credit card number to an external address and verify that the DLP policy triggers an alert and blocks the message. Check the Activity Explorer for the corresponding event.

## Rollback
If the policy becomes overly restrictive, revert the 'Instance count' to its original value or disable the policy temporarily while adjusting the sensitive info type rules.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-investigate>
- <https://learn.microsoft.com/en-us/purview/dlp-create-policy>
