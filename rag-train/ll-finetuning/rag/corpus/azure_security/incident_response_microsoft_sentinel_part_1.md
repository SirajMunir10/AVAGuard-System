# Incident Response: Microsoft Sentinel

**Domain:** Azure
**Subdomain:** Microsoft Sentinel
**Incident Type:** Incident Response

## Scenario / Query
A security analyst notices that a Microsoft Sentinel incident for 'MFA Denied' is generating a high number of false positives from a legitimate user's IP address. How should the analyst use Sentinel's built-in capabilities to tune the analytics rule and reduce noise without disabling the rule entirely?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD Premium P2, Microsoft Sentinel enabled)
- **Configuration:** Analytics rule 'MFA Denied' based on SigninLogs with threshold of 5 failed attempts in 1 hour

## Symptoms
- Multiple Sentinel incidents created daily for a single user's IP address
- Incidents are closed as false positive after investigation
- No evidence of compromise for that user

## Error Codes
N/A

## Root Causes
1. Analytics rule threshold too low for that user's normal behavior
2. No exception or suppression mechanism applied

## Remediation Steps
1. 1. In Microsoft Sentinel, navigate to Analytics > Active rules and select the 'MFA Denied' rule.
2. 2. Click 'Edit' and go to the 'Set rule logic' tab.
3. 3. Under 'Alert threshold', increase the number of failed attempts (e.g., from 5 to 10) or extend the observation window.
4. 4. Alternatively, add an exception by including a condition that excludes the specific user or IP address in the rule query (e.g., `| where UserPrincipalName != 'user@contoso.com'`).
5. 5. Save the rule and monitor incident generation for the next 24 hours.

## Validation
Verify that no new incidents are created for the excluded user/IP within the next 24 hours, while incidents for other users continue to be generated.

## Rollback
Revert to the previous rule configuration by editing the rule and restoring the original threshold and query conditions.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
