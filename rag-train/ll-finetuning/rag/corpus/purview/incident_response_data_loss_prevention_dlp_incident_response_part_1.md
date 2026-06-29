# Incident Response: Data Loss Prevention (DLP) â€“ Incident Response

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) â€“ Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A user reports that a DLP policy in Microsoft Purview is generating false positive alerts for internal financial documents that should be allowed. How do I investigate and remediate the policy to reduce noise while maintaining compliance?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview Data Loss Prevention (DLP) configured
- **Configuration:** DLP policy named 'Financial Data Protection' applied to Exchange Online and SharePoint Online, using default sensitive info types for credit card numbers and bank account numbers.

## Symptoms
- DLP policy alerts are triggered on internal financial spreadsheets that do not contain actual sensitive data
- Users report legitimate work is blocked or flagged incorrectly
- Incident queue in Microsoft 365 Defender shows high volume of low-severity DLP matches

## Error Codes
N/A

## Root Causes
1. DLP policy uses default sensitive info types without adjusting confidence levels or instance counts
2. Policy is not scoped to exclude trusted internal sites or specific user groups
3. No test mode was used before enabling the policy in enforcement mode

## Remediation Steps
1. 1. Review DLP alerts in Microsoft 365 Defender (https://security.microsoft.com) under Incidents & Alerts > Alerts. Filter by DLP policy name.
2. 2. Use the DLP Activity Explorer to analyze the actual content that triggered the alert and identify false positives.
3. 3. Modify the DLP policy: adjust the confidence level for the sensitive info type (e.g., increase from 75 to 85) and set a minimum instance count (e.g., 2) to reduce false positives.
4. 4. Add an exclusion for trusted internal SharePoint sites or Exchange distribution groups that handle financial data legitimately.
5. 5. Set the policy to test mode with policy tips before re-enabling enforcement.
6. 6. Document the changes and notify the security operations team.

## Validation
After changes, verify that the same document no longer triggers an alert by using the DLP Test functionality in the Purview compliance portal or by checking Activity Explorer for a 24-hour period.

## Rollback
Revert the policy to its previous version using the version history in the DLP policy editor, or disable the policy and re-enable the original version from backup.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-investigate-alerts>
- <https://learn.microsoft.com/en-us/purview/dlp-create-policy>
