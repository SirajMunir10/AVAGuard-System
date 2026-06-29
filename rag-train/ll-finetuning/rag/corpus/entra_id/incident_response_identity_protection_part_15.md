# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate and remediate malicious IP address detections in Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based Conditional Access policies

## Symptoms
- Sign-in from a malicious IP address detected by Identity Protection

## Error Codes
N/A

## Root Causes
1. Activity performed from a malicious IP address not associated with legitimate user

## Remediation Steps
1. Confirm the sign-in as compromised
2. Invoke a password reset if not already performed by self-remediation
3. Block the user if an attacker has access to reset password or perform MFA and reset password and revoke all tokens
4. Set up risk-based Conditional Access policies to require password reset or perform MFA for all high-risk sign-ins

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Filter for the user and sign-in event that was detected as malicious IP. 4. Confirm the risk state is now 'Dismissed' or 'Remediated' (if you confirmed compromised and reset password). 5. Verify the user's sign-in logs show no further activity from the malicious IP. 6. If a risk-based Conditional Access policy was set, use the Conditional Access What If tool to simulate a high-risk sign-in for that user and confirm the policy requires password reset or MFA.

## Rollback
1. If you incorrectly confirmed a sign-in as compromised, navigate to Protection > Identity Protection > Risky sign-ins, select the sign-in, and change the risk state to 'Dismiss user risk' to revert the confirmation. 2. If you blocked the user, unblock them by going to Users > select the user > Properties, set 'Block sign-in' to No. 3. If you reset the user's password, provide the user with a temporary password via a secure channel and instruct them to change it on next sign-in. 4. If you revoked all tokens, the user will need to re-authenticate; no direct rollback exists for token revocation. 5. If you added a risk-based Conditional Access policy, disable or delete the policy from Protection > Conditional Access > Policies.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
