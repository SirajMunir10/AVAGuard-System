# Incident Response: Data Loss Prevention (DLP) â€“ Incident Response

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) â€“ Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A user reports that a DLP policy is generating false positive alerts for sensitive information types that are not actually present in the scanned content. How should a security analyst investigate and remediate this issue using Microsoft Purview compliance portal?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview DLP enabled
- **Configuration:** DLP policy configured with default sensitive info types (e.g., Credit Card Number, U.S. Social Security Number) and alert notifications enabled

## Symptoms
- DLP alerts are triggered for content that does not contain the sensitive information type specified in the policy
- End users receive policy tip notifications incorrectly
- Security team observes high volume of low-confidence alerts in Microsoft 365 Defender

## Error Codes
N/A

## Root Causes
1. Sensitive information type detection may be based on proximity or confidence level thresholds that are too low
2. DLP policy may be using a custom sensitive info type with inaccurate regex or keyword list
3. Policy scope may include locations or conditions that inadvertently match benign content

## Remediation Steps
1. 1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the affected policy.
2. 2. Review the 'Locations' and 'Conditions' to ensure the policy is scoped correctly and not overly broad.
3. 3. Examine the 'Rules' section and verify the sensitive info types used. Use the 'Test' functionality to simulate content and confirm detection behavior.
4. 4. If using a custom sensitive info type, review its definition in Data Classification > Sensitive info types and adjust the regex, keyword list, or confidence level as needed.
5. 5. Adjust the 'Instance count' and 'Match accuracy' (confidence level) for the sensitive info type in the rule to reduce false positives.
6. 6. After changes, re-run the test with sample content to validate the fix.
7. 7. Monitor alert volume in Microsoft 365 Defender to confirm reduction in false positives.

## Validation
Use the DLP policy test functionality in Purview to simulate the same content and confirm that alerts are no longer generated for non-sensitive data.

## Rollback
If adjustments increase false negatives, revert the sensitive info type confidence level or instance count to the previous values, or restore the policy from a backup copy.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-investigate-alerts>
- <https://learn.microsoft.com/en-us/purview/dlp-create-policy>
