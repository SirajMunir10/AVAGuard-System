# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate and respond to anomalous token and token issuer anomaly detections in Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Identity Protection risk detections

## Symptoms
- Anomalous token detection
- Token issuer anomaly detection

## Error Codes
N/A

## Root Causes
1. Activity not performed by a legitimate user based on risk alert, location, application, IP address, User Agent, or other unexpected characteristics

## Remediation Steps
1. Mark the sign-in as compromised
2. Invoke a password reset if not already performed by self-remediation
3. Block the user if an attacker has access to reset password or perform
4. Set up risk-based Conditional Access policies to require password reset, perform MFA, or block access for all high-risk sign-ins

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Confirm the specific anomalous token or token issuer anomaly detection is listed with a risk level of 'High'. 4. Verify the sign-in status shows 'Compromised' if you marked it as compromised. 5. Check the user's risk history to confirm a password reset was initiated (either by self-remediation or admin-initiated). 6. Confirm the user is blocked from sign-in if you applied a block. 7. Review the Conditional Access policies to ensure risk-based policies (e.g., require password reset, MFA, or block) are enabled and applied to high-risk sign-ins.

## Rollback
1. If a sign-in was incorrectly marked as compromised, navigate to Protection > Identity Protection > Risky sign-ins, select the sign-in, and change the status to 'Dismiss user risk' to clear the risk. 2. If a password reset was invoked in error, the user must contact their helpdesk to reset their password again; there is no direct rollback for a password reset. 3. If a user was blocked, navigate to Azure AD > Users, select the user, and enable sign-in by clearing the block. 4. If a risk-based Conditional Access policy was set up incorrectly, navigate to Protection > Conditional Access > Policies, locate the policy, and either disable it or modify its assignments to exclude the affected user or group.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
