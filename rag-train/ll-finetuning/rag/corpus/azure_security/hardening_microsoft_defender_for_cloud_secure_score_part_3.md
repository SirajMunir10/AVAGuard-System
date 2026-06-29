# Hardening: Microsoft Defender for Cloud â€“ Secure Score

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud â€“ Secure Score
**Incident Type:** Hardening

## Scenario / Query
An Azure subscription shows a low Secure Score due to unaddressed security recommendations. How can I identify and remediate the most impactful recommendations to harden the environment?

## Environment Context
- **Tenant Type:** Enterprise (single subscription)
- **Configuration:** Microsoft Defender for Cloud is enabled on the subscription; Secure Score is below 30%.

## Symptoms
- Secure Score in Microsoft Defender for Cloud is significantly lower than expected
- Multiple security recommendations are listed as 'Unhealthy' in the Recommendations blade
- Compliance dashboard shows non-compliance with built-in Azure Security Benchmark policies

## Error Codes
N/A

## Root Causes
1. Security policies (initiatives) have not been assigned or are not enforced
2. Recommended security controls (e.g., enable MFA, encrypt disks, enable NSG flow logs) are not implemented
3. No regular review and remediation of security recommendations

## Remediation Steps
1. 1. In Microsoft Defender for Cloud, navigate to 'Recommendations' and sort by 'Potential score increase' to prioritize high-impact items.
2. 2. For each recommendation, select it and follow the 'Remediation steps' tab which provides Azure Portal, PowerShell, or CLI instructions as documented by Microsoft.
3. 3. For example, to enable MFA for all users with owner permissions, follow the guidance in 'MFA should be enabled on accounts with owner permissions on your subscription' (recommendation ID: 6240402e-f77c-46fa-9062-9c8cbfa22b34).
4. 4. Apply remediation using the 'Fix' button where available, or manually implement the documented steps.
5. 5. After remediation, verify the recommendation status updates to 'Healthy' within a few hours.

## Validation
After applying the top five recommendations, the Secure Score should increase proportionally. Check the Secure Score overview page in Defender for Cloud to confirm the new score.

## Rollback
If a remediation causes issues, revert the change using the opposite action (e.g., if you enabled MFA via conditional access, disable the policy; if you applied a disk encryption, remove the encryption). Each recommendation's documentation includes reversal steps.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls>
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/recommendations-reference>
