# Incident Response: Microsoft Sentinel

**Domain:** Azure
**Subdomain:** Microsoft Sentinel
**Incident Type:** Incident Response

## Scenario / Query
An Azure Active Directory sign-in log shows a successful authentication from an anonymous IP address (e.g., Tor exit node) for a user who has never used such an IP before. How should a security operations analyst triage and respond to this incident in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD Premium P2)
- **Configuration:** Microsoft Sentinel enabled with Azure AD connector; Anomalous Token and Anonymous IP detection analytics rules enabled

## Symptoms
- User successfully signed in from an IP address classified as anonymous (Tor, VPN, or proxy) in Azure AD Sign-in logs
- Sign-in event shows 'Anonymous IP address' risk detection in Azure AD Identity Protection
- No prior sign-ins from this IP address for the user

## Error Codes
N/A

## Root Causes
1. User credentials may have been compromised and used from an anonymizing service to evade detection
2. Azure AD Conditional Access policy did not block anonymous IP addresses because no such policy was configured

## Remediation Steps
1. 1. In Microsoft Sentinel, open the incident and review the related Azure AD sign-in logs to confirm the anonymous IP risk detection.
2. 2. Use the Sentinel investigation graph to check for other suspicious activities from the same user or IP.
3. 3. If compromise is confirmed, reset the user's password and revoke all refresh tokens (as documented in 'Respond to a compromised user account').
4. 4. Configure a Conditional Access policy to block access from anonymous IP addresses (see 'Conditional Access: Block access by location').
5. 5. Enable Azure AD Identity Protection to automatically remediate high-risk detections (e.g., force password reset on anonymous IP sign-in).

## Validation
Verify that the user's account no longer shows anonymous IP sign-ins and that the Conditional Access policy is blocking subsequent attempts. Confirm the user can sign in from a known, trusted location.

## Rollback
If the sign-in was legitimate (e.g., user traveling and using a VPN), remove the user from any temporary block policy and update the trusted IP list in Conditional Access.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
- <https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection>
- <https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-location>
