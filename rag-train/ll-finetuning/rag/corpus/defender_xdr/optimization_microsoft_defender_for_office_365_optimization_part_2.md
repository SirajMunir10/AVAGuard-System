# Optimization: Microsoft Defender for Office 365 â€“ Optimization

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365 â€“ Optimization
**Incident Type:** Optimization

## Scenario / Query
A security operations team notices that Microsoft Defender for Office 365 is generating a high volume of false positive alerts for phishing campaigns. They want to optimize the detection rules to reduce noise without compromising security coverage. What steps should they take to tune the anti-phish policy and improve alert fidelity?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Default anti-phish policy is enabled; no custom allow/block lists are configured; users are reporting frequent false positive quarantine notifications.

## Symptoms
- High volume of phishing alerts that are later confirmed as benign
- Users report legitimate emails being quarantined or moved to Junk Email folder
- Security team spends excessive time investigating and dismissing false positives

## Error Codes
N/A

## Root Causes
1. Default anti-phish policy may be too aggressive for the organization's email traffic patterns
2. No custom allow lists or trusted sender domains configured
3. Impersonation protection settings may be overly broad, flagging internal users or common partner domains

## Remediation Steps
1. 1. Review the current anti-phish policy in the Microsoft 365 Defender portal (Policies & rules > Threat policies > Anti-phish).
2. 2. Add trusted sender domains or email addresses to the 'Allowed senders and domains' list to reduce false positives for known legitimate senders.
3. 3. Adjust impersonation protection settings: under 'Phishing threshold & protection', set the impersonation protection level to 'Standard' (not 'Aggressive') unless a higher level is required.
4. 4. Enable the 'Show first contact safety tip' and 'Show user impersonation safety tip' to help users identify suspicious messages without automatic action.
5. 5. Use the Threat Explorer to analyze false positive patterns and export a sample of misclassified messages for tuning.
6. 6. Create a custom anti-phish policy scoped to specific users or groups if the default policy is too broad.
7. 7. Monitor the 'Quarantine' and 'User-reported' reports for 7 days after changes to validate improvement.

## Validation
After applying the tuning steps, verify that the number of false positive phishing alerts decreases by at least 50% over two weeks, while confirmed phishing detection rates remain stable. Use the 'Threat management > Review' page in Defender for Office 365 to compare alert volumes before and after changes.

## Rollback
If false positive reduction is insufficient or if legitimate phishing detection drops, revert the custom allow list entries and reset impersonation protection to 'Aggressive'. Alternatively, delete the custom anti-phish policy and re-enable the default policy.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-configure>
