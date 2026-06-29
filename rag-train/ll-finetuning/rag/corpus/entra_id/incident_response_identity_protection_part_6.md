# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to perform initial triage of identity risk detections using Entra ID Protection?

## Environment Context
- **Tenant Type:** Entra ID (Azure AD) tenant with Identity Protection enabled
- **Configuration:** Identity Protection dashboard, risk reports, Impact analysis workbook, sign-in logs, Conditional Access policies, Insider Risk Management (Purview)

## Symptoms
- Number of attacks detected
- High risk users identified
- Recent risky users, sign-ins, or detections in risk reports
- Similar sign-in activities with same characteristics (IP address, geography, success/failure)

## Error Codes
N/A

## Root Causes
1. Compromised accounts indicated by similar sign-in activities
2. Possible attacker impersonation of user
3. Risky activities such as downloading large volume of files from new location

## Remediation Steps
1. Review the ID Protection dashboard to visualize number of attacks, number of high risk users, and other important metrics based on detections in your environment.
2. Review the risk reports to examine the details of any recent risky users, sign-ins, or detections.
3. Review the Impact analysis workbook to understand the scenarios where risk is evident in your environment and what risk-based access policies should be enabled to manage high-risk users and sign-ins.
4. Review the sign-in logs to identify similar activities with the same characteristics. This activity could be an indication of more compromised accounts. If there are common characteristics, like IP address, geography, success/failure, etc., consider blocking them with a Conditional Access policy.
5. Review which resources might be compromised, including potential data downloads or administrative modifications.
6. Enable self-remediation policies through Conditional Access.
7. With Insider Risk Management through Microsoft Purview, you can check to see if the user performed other risky activities, such as downloading a large volume of files from a new location. This behavior is a strong indication of a possible compromise.
8. If you suspect an attacker can impersonate the user, you should require the user to reset their password and perform MFA or block the user and revoke all refresh and access tokens.

## Validation
1. Navigate to the Identity Protection dashboard in the Entra admin center and confirm the number of attacks and high-risk users have decreased or returned to baseline. 2. Open the Risk reports (Risky users, Risky sign-ins, Risk detections) and verify that no new high-risk detections are present for the remediated users. 3. Review the Impact analysis workbook to ensure risk-based access policies are enabled and no active high-risk scenarios remain. 4. Check the sign-in logs for the affected users to confirm no further similar activities (same IP, geography, success/failure) are occurring. 5. Verify that Conditional Access policies requiring MFA or password reset are triggered for the remediated users. 6. In Microsoft Purview Insider Risk Management, confirm no new risky activities (e.g., large file downloads from new locations) are associated with the users. 7. If tokens were revoked, confirm the users are prompted to re-authenticate.

## Rollback
1. If a user was blocked, unblock the user in the Entra admin center under Users > user > Authentication methods > Block sign-in. 2. If refresh and access tokens were revoked, the user will need to re-authenticate; no direct rollback is possible. 3. If a Conditional Access policy was created to block IPs or geographies, disable or delete that policy in Conditional Access > Policies. 4. If a password reset was forced, the user can change their password again via self-service password reset. 5. If MFA registration was reset, the user can re-register via https://aka.ms/mfasetup. 6. If the user was dismissed from risk, re-confirm the risk level by reviewing the risk detection details and, if needed, confirm the user as compromised again via the Risky users report.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
