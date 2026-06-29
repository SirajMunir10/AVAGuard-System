# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate and remediate a suspicious browser detection in Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based Conditional Access policies configured

## Symptoms
- Detection indicates the user doesn't commonly use the browser or activity within the browser doesn't match the user's normal behavior

## Error Codes
N/A

## Root Causes
1. Unusual browser usage or activity pattern by the user

## Remediation Steps
1. Confirm the sign-in as compromised
2. Invoke a password reset if not already performed by self-remediation
3. Block the user if an attacker has access to reset password or perform MFA
4. Set up risk-based Conditional Access policies to require password reset, perform MFA, or block access for all high-risk sign-ins

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Locate the specific risky sign-in detection (e.g., by user name or detection time). 4. Confirm the risk level is now 'Remediated' or 'Dismissed' and the associated risk state is 'Remediated' or 'Dismissed'. 5. Verify the user's sign-in logs (Azure AD > Sign-in logs) show no further suspicious browser detections for that user. 6. If a password reset was performed, confirm the user can sign in with the new password and that MFA registration is complete. 7. If the user was blocked, confirm the user is listed under 'Blocked users' in Identity Protection and that sign-in attempts are denied.

## Rollback
1. If the sign-in was incorrectly confirmed as compromised, navigate to Identity Protection > Risky sign-ins, select the detection, and change the risk state to 'Dismissed'. 2. If a password reset was performed in error, instruct the user to reset their password again via self-service password reset (SSPR) or an administrator can reset the password to a temporary one. 3. If the user was blocked in error, navigate to Identity Protection > Risky users, select the user, and choose 'Unblock user'. 4. If risk-based Conditional Access policies were set up incorrectly, modify or disable the policies in Azure AD > Security > Conditional Access to revert to previous settings.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
