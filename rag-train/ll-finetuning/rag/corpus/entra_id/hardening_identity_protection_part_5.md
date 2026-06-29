# Hardening: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Hardening

## Scenario / Query
How do I handle token theft related detections that are no longer auto-remediated in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection enabled
- **Configuration:** User risk-based Conditional Access policies configured

## Symptoms
- Token theft related detections (Microsoft Entra threat intelligence, Anomalous token, Attacker in the Middle, Verified threat actor IP, Token issuer anomaly) are not auto-remediated during sign-in when MFA claims are present
- Sessions with MFA claims are not closed automatically for these detections

## Error Codes
N/A

## Root Causes
1. Recent update to detection architecture: no longer autoremediate sessions with MFA claims when token theft related or Verified threat actor IP detection triggers during sign-in

## Remediation Steps
1. Investigate risk detection details in the Risk Detection Details pane, which now includes session details: Token Issuer type, Sign-in time, Sign-in location, Sign-in client, Sign-in request ID, Sign-in correlation ID
2. If user risk-based Conditional Access policies are configured and one of these detections fires on a user, require the end user to perform a secure password change and reauthenticate their account with multifactor authentication to clear the risk

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risk detections. 3. Filter by detection type: 'Microsoft Entra threat intelligence', 'Anomalous token', 'Attacker in the Middle', 'Verified threat actor IP', or 'Token issuer anomaly'. 4. Select a recent detection and open the Risk Detection Details pane. 5. Confirm that the pane includes session details: Token Issuer type, Sign-in time, Sign-in location, Sign-in client, Sign-in request ID, and Sign-in correlation ID. 6. Verify that the user risk-based Conditional Access policy is configured and applied to the user. 7. Confirm that the policy requires a secure password change and reauthentication with multifactor authentication (MFA) when such a detection is triggered. 8. Simulate a token theft detection (if possible in a test environment) and verify that the user is prompted to change password and reauthenticate with MFA, and that the user risk is cleared after successful remediation.

## Rollback
1. If the remediation causes issues (e.g., users unable to complete password change or MFA), temporarily disable the user risk-based Conditional Access policy that enforces password change and MFA reauthentication. 2. Navigate to Protection > Identity Protection > User risk policy and set the policy to 'Off' or remove the specific condition that triggers on token theft detections. 3. Alternatively, modify the policy to use a less restrictive control (e.g., require MFA only, without password change) while troubleshooting. 4. After disabling or modifying the policy, monitor user sign-ins and risk detections to ensure no further disruption. 5. Re-enable or adjust the policy once the underlying issue is resolved, following the guidance in the source documentation.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
