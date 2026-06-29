# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate a Microsoft Entra threat intelligence risk detection when the sign-in was from a suspicious IP address?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Identity Protection risk detection

## Symptoms
- Sign-in from a suspicious IP address

## Error Codes
N/A

## Root Causes
1. IP address shows suspicious behavior in the environment
2. IP generates a high number of failures for a user or set of users in the directory
3. Traffic from the IP is coming from an unexpected protocol or application, for example Exchange legacy protocols
4. IP address corresponds to a cloud service provider with legitimate enterprise applications running from the same IP

## Remediation Steps
1. Confirm if the IP address shows suspicious behavior in your environment
2. Check if the IP generates a high number of failures for a user or set of users in your directory
3. Check if the traffic of the IP is coming from an unexpected protocol or application, for example Exchange legacy protocols
4. If the IP address corresponds to a cloud service provider, rule out that there are no legitimate enterprise applications running from the same IP

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Locate the sign-in with the suspicious IP address. 4. Review the risk detail 'Sign-in from anonymous IP address' or 'Sign-in from IP address with suspicious activity'. 5. Confirm the IP address is not associated with a known legitimate cloud service provider by checking the IP reputation in the risk details. 6. Verify that the sign-in activity (e.g., protocol, application) matches expected patterns for your environment. 7. Use the 'Confirm sign-in compromised' or 'Dismiss sign-in risk' action as appropriate.

## Rollback
1. If the remediation (e.g., dismissing risk or confirming compromised) was incorrect, navigate to Protection > Identity Protection > Risky sign-ins. 2. Select the sign-in and use the 'Confirm sign-in safe' action if you previously confirmed compromised, or 'Confirm sign-in compromised' if you previously dismissed. 3. Alternatively, use Microsoft Graph API: PATCH /identityProtection/riskySignIns/{riskySignInId} with the appropriate risk state (e.g., 'dismissed', 'confirmedCompromised', 'confirmedSafe'). 4. If the IP was blocked, remove the block by navigating to Conditional Access > Policies and disabling or deleting the policy that blocked the IP. 5. If the user was blocked, unblock the user by navigating to Protection > Identity Protection > Risky users, select the user, and choose 'Dismiss user risk' or 'Confirm user safe'.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
