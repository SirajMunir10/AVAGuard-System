# Optimization: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Optimization

## Scenario / Query
How can I reduce the number of false positive risk detections in Entra ID Identity Protection by adjusting user risk policies?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Entra ID Identity Protection user risk policy is enabled with default thresholds

## Symptoms
- High volume of user risk detections flagged as medium or high risk
- Frequent MFA prompts for legitimate users
- Helpdesk tickets reporting blocked access due to risk-based conditional access

## Error Codes
N/A

## Root Causes
1. User risk policy thresholds are set too low, causing excessive detections
2. Risk detection sensitivity may be too high for the organization's risk appetite

## Remediation Steps
1. Review and adjust the user risk policy threshold in the Entra admin center under Identity Protection > User risk policy
2. Consider raising the threshold from Low and above to Medium and above if false positives are frequent
3. Use the Identity Protection risk detections report to analyze patterns and exclude trusted locations or known good IPs
4. Implement risk-based conditional access policies that require MFA only for medium or high risk users, as documented in Microsoft Learn

## Validation
After adjusting the user risk policy threshold, monitor the risk detections report for a reduction in low-risk flags and verify that legitimate users are not blocked.

## Rollback
Revert the user risk policy threshold to the previous setting (e.g., Low and above) if false negatives increase or security incidents occur.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection>
