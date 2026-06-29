# Hardening: Microsoft Defender for Cloud â€“ Secure Score

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud â€“ Secure Score
**Incident Type:** Hardening

## Scenario / Query
A customer notices that their Azure Secure Score is lower than expected. They want to identify which security recommendations are not implemented and how to remediate them to improve their security posture.

## Environment Context
- **Tenant Type:** Enterprise (multiple subscriptions)
- **Configuration:** Microsoft Defender for Cloud is enabled on all subscriptions, but Secure Score is below 70%.

## Symptoms
- Secure Score value is lower than the target threshold
- Multiple security recommendations appear as 'Unhealthy' in Defender for Cloud
- Compliance dashboard shows non-compliant controls

## Error Codes
N/A

## Root Causes
1. Security recommendations have not been remediated
2. Some resources are not covered by Defender for Cloud plans
3. Incomplete implementation of security baselines

## Remediation Steps
1. Review the list of unhealthy recommendations in Microsoft Defender for Cloud
2. For each recommendation, follow the remediation steps provided in the Azure portal or use the 'Fix' option if available
3. Enable all Defender for Cloud plans (e.g., Defender for Servers, Defender for SQL) to maximize coverage
4. Apply Azure Policy initiatives that map to security benchmarks (e.g., Azure Security Benchmark)
5. Regularly monitor Secure Score trends and set improvement targets

## Validation
After remediating all unhealthy recommendations, the Secure Score should increase. Verify by refreshing the Secure Score overview page in Defender for Cloud.

## Rollback
If a remediation causes issues, revert the change using the resource's previous configuration or by disabling the applied policy assignment. For policy-based changes, remove or disable the policy assignment.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-access-and-track>
