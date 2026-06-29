# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to respond to an atypical travel detection in Microsoft Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Identity Protection risk detections

## Symptoms
- Atypical travel detection alert in Identity Protection

## Error Codes
N/A

## Root Causes
1. Activity not performed by a legitimate user
2. User known to use the IP address in the scope of their duties
3. User recently traveled to the destination mentioned in the alert
4. IP address range is from a sanctioned VPN

## Remediation Steps
1. If you confirm the activity was not performed by a legitimate user: Mark the sign-in as compromised, and invoke a password reset if not already performed by self-remediation.
2. Block the user if attacker has access to reset password or perform MFA and reset password.
3. If a user is known to use the IP address in the scope of their duties, confirm sign-in as safe.
4. If you confirm that the user recently traveled to the destination mentioned detailed in the alert, confirm sign-in as safe.
5. If you confirm that the IP address range is from a sanctioned VPN, confirm sign-in as safe and add the VPN IP address range to named locations in Microsoft Entra ID and Microsoft Defender for Cloud Apps.

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Locate the specific sign-in associated with the atypical travel detection. 4. Verify that the risk state has been updated to 'Confirmed compromised' or 'Dismissed' as appropriate. 5. If a password reset was invoked, confirm that the user's password has been reset by checking the user's audit logs or by attempting to sign in with the old credentials. 6. If the user was blocked, verify that the user's sign-in is blocked by checking the user's sign-in logs or by attempting to sign in with the user's credentials. 7. If the sign-in was confirmed as safe, verify that the risk state is 'Dismissed' and that no further risk detections are triggered for the same activity. 8. If a VPN IP address range was added to named locations, navigate to Protection > Named locations and confirm the new location is listed with the correct IP range.

## Rollback
1. If a sign-in was incorrectly marked as compromised, navigate to Identity Protection > Risky sign-ins, select the sign-in, and choose 'Dismiss user risk' to revert the risk state. 2. If a password reset was performed unnecessarily, the user must be contacted to set a new password; there is no automated rollback for a password reset. 3. If a user was blocked incorrectly, navigate to Azure AD > Users, select the user, go to 'Sign-ins' and unblock the user by removing any sign-in block. 4. If a sign-in was incorrectly confirmed as safe, navigate to Identity Protection > Risky sign-ins, select the sign-in, and choose 'Confirm compromised' to revert the risk state. 5. If a VPN IP address range was added to named locations incorrectly, navigate to Protection > Named locations, select the location, and delete it.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
