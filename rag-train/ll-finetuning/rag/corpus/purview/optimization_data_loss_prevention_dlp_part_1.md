# Optimization: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Optimization

## Scenario / Query
How can I optimize DLP policy performance by reducing false positives when sensitive info types like EU debit card numbers are detected in email attachments?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** DLP policy with EU debit card number sensitive info type, configured for Exchange Online and SharePoint Online

## Symptoms
- High volume of DLP policy matches that are not actual data breaches
- Users reporting legitimate business emails being blocked or flagged
- DLP reports show frequent matches for EU debit card numbers in attachments that are test or sample data

## Error Codes
N/A

## Root Causes
1. DLP policy uses default confidence level for EU debit card number, which may trigger on partial matches or test data
2. No proximity or exclusion rules configured to reduce false positives

## Remediation Steps
1. Adjust the confidence level for the EU debit card number sensitive info type in the DLP policy to 'High confidence' to reduce false positives (Microsoft Learn: 'Tune your DLP policy' guidance)
2. Add exclusion rules to the DLP policy to exempt specific sites, users, or file types that are known to contain legitimate test data
3. Use DLP policy tips and incident reports to review and refine the policy over time

## Validation
Monitor DLP reports for a reduction in false positive matches while ensuring true positive detections remain effective.

## Rollback
Revert the confidence level to the default setting and remove any exclusion rules if false negatives increase.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-tuning>
