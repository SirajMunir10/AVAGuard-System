# Optimization: Microsoft Defender for Office 365 â€“ Optimization

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365 â€“ Optimization
**Incident Type:** Optimization

## Scenario / Query
A security operations team notices that Microsoft Defender for Office 365 is generating a high volume of false positive alerts for phishing campaigns. They want to reduce noise without lowering security posture. How can they optimize the alert tuning by using the built-in 'Optimize' tab in the Microsoft 365 Defender portal?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Anti-phishing policies and alert policies are configured with default thresholds.

## Symptoms
- High number of phishing alerts that are manually dismissed as false positives
- Analyst fatigue due to excessive low-fidelity alerts
- Alert volume exceeds 500 per day for a single policy

## Error Codes
N/A

## Root Causes
1. Alert policies are set to generate alerts for every detected suspicious email without aggregation or threshold tuning
2. The 'Optimize' tab in the Microsoft 365 Defender portal has not been used to review and adjust alert generation settings

## Remediation Steps
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com) > Incidents & alerts > Alerts > Optimize tab.
2. Review the list of alert policies that are generating high volumes of false positives.
3. For each policy, select 'Edit alert settings' and adjust the 'Alert threshold' to a higher value (e.g., from 'Every email' to 'Aggregated per campaign') as documented in Microsoft Learn.
4. Enable 'Alert suppression' for known benign senders or domains if applicable.
5. Test changes by monitoring the alert volume over 48 hours and verifying that true positive detection remains effective.

## Validation
After adjustment, the alert volume should decrease by at least 50% while maintaining detection of actual phishing campaigns. Verify by checking the 'Optimize' tab again after 48 hours to confirm reduced false positive rate.

## Rollback
Revert the alert threshold to the previous setting by editing the same alert policy in the Microsoft 365 Defender portal and selecting the original threshold value.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/optimize-defender>
