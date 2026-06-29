# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate and remediate a password spray detection in Microsoft Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based Conditional Access policy configured

## Symptoms
- Password spray detection alert in Identity Protection
- Successful credential validation against a user in the tenant from a spray attack

## Error Codes
N/A

## Root Causes
1. Attacker conducting a spray attack achieving a successful credential match against a user in the tenant

## Remediation Steps
1. If you confirm that the activity was not performed by a legitimate user: Mark the sign-in as compromised, and invoke a password reset if not already performed by self-remediation.
2. Block the user if an attacker has access to reset password or perform MFA and reset password and revoke all tokens.
3. If you confirm the user does use the IP address in the scope of their duties, confirm the sign-in as safe.
4. If you confirm that the account isn't compromised and see no brute force or password spray indicators against the account: Allow the user to self-remediate with a risk-based Conditional Access policy or have an admin confirm sign-in as safe.
5. Ensure you have Microsoft Entra smart lockout configured appropriately to avoid unnecessary account lockouts.

## Validation
1. Navigate to Microsoft Entra admin center > Identity Protection > Risky sign-ins. Filter for the user in question and verify that the sign-in is now marked as 'Compromised' or 'Safe' as per the remediation action taken. 2. If a password reset was invoked, confirm the user can sign in with the new credentials and that no further risky sign-ins appear for that user. 3. If the user was blocked, verify the user is in the 'Blocked' state under Users > All users > [user] > Sign-ins. 4. Check the risk-based Conditional Access policy logs to ensure the policy is triggering correctly for risky sign-ins. 5. Review Microsoft Entra smart lockout settings under Authentication methods > Password protection > Smart lockout to confirm thresholds are appropriate.

## Rollback
1. If a sign-in was incorrectly marked as compromised: Navigate to Identity Protection > Risky sign-ins, select the sign-in, and choose 'Dismiss user risk' to revert the state. 2. If a password reset was performed unnecessarily: The user must set a new password via self-service password reset or admin reset; there is no direct rollback. 3. If a user was blocked incorrectly: In Microsoft Entra admin center, go to Users > All users, select the user, and under 'Sign-ins', unblock the user by enabling sign-in. 4. If a sign-in was incorrectly confirmed as safe: Navigate to Identity Protection > Risky sign-ins, select the sign-in, and choose 'Confirm sign-in compromised' to revert. 5. If smart lockout settings were changed: Restore the previous threshold values under Authentication methods > Password protection > Smart lockout.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
