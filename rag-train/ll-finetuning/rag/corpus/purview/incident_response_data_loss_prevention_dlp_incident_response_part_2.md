# Incident Response: Data Loss Prevention (DLP) â€“ Incident Response

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) â€“ Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A user reports that a DLP policy in Microsoft Purview is generating excessive false positive alerts for a specific sensitive information type. How do you investigate and tune the policy to reduce noise while maintaining compliance?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview DLP enabled
- **Configuration:** DLP policy 'Finance Data Protection' configured with the sensitive info type 'Credit Card Number' and action 'Block with override'

## Symptoms
- DLP alerts are generated for legitimate business transactions involving credit card numbers
- End users frequently request overrides, causing administrative overhead
- The DLP policy reports a high number of false positives in the Activity Explorer

## Error Codes
N/A

## Root Causes
1. The DLP policy uses a broad confidence level for the sensitive info type
2. The policy does not include exception rules for trusted financial applications or known business processes

## Remediation Steps
1. Review DLP alerts in the Microsoft Purview compliance portal under Data Loss Prevention > Alerts
2. Use Activity Explorer to analyze the context of false positive matches
3. Modify the DLP policy to adjust the confidence level or instance count for the sensitive info type
4. Add an exception rule to exclude trusted financial applications (e.g., QuickBooks, SAP) from the policy
5. Test the updated policy in simulation mode before enforcing

## Validation
After applying the changes, verify in Activity Explorer that false positive alerts have decreased while legitimate policy violations are still detected.

## Rollback
If tuning does not resolve the issue, revert to the previous policy version by editing the policy back to its original settings or using the 'Restore' option in the policy history.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-investigate>
- <https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy>
