# Incident Response: Microsoft Sentinel

**Domain:** Azure
**Subdomain:** Microsoft Sentinel
**Incident Type:** Incident Response

## Scenario / Query
You are the security operations lead for Contoso. Microsoft Sentinel has generated an incident indicating that a user account was used to sign in from an anonymous IP address and then performed an unusual bulk download from Azure Storage. How do you investigate and respond using Microsoft Sentinel and Azure Active Directory (Azure AD) audit logs?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD Premium P2, Microsoft Sentinel enabled)
- **Configuration:** Microsoft Sentinel data connectors for Azure AD (sign-in logs and audit logs) and Azure Activity logs are enabled. An analytics rule for 'Anonymous IP sign-in followed by unusual download' is active.

## Symptoms
- Microsoft Sentinel incident created with severity High
- Sign-in log shows user 'jdoe@contoso.com' from IP address 203.0.113.5 (classified as anonymous proxy)
- Azure Activity log shows multiple 'Download Blob' operations from the same user within a short time window
- User reports they did not perform the download

## Error Codes
N/A

## Root Causes
1. User credentials may be compromised
2. Anonymous IP address used to evade detection
3. No Azure AD Conditional Access policy blocking anonymous IP sign-ins

## Remediation Steps
1. 1. In Microsoft Sentinel, open the incident and review the entities (user, IP address, storage account).
2. 2. Use the Azure AD sign-in logs (via Sentinel or Azure portal) to confirm the sign-in from the anonymous IP.
3. 3. Immediately disable the user account in Azure AD (Azure AD portal > Users > select user > Revoke sessions and Block sign-in).
4. 4. Reset the user's password and require MFA re-registration.
5. 5. Review Azure Storage diagnostic logs to assess data exfiltration scope.
6. 6. Create a Conditional Access policy to block sign-ins from anonymous IP addresses (Azure AD > Security > Conditional Access > New policy > Assignments: All users, Conditions: Locations > Include any location > Select 'Anonymous IP address' > Access controls: Block access).
7. 7. Enable Azure AD Identity Protection to automatically detect and respond to risky sign-ins.

## Validation
Verify the user account is blocked and cannot sign in. Confirm that the Conditional Access policy is in 'Report-only' mode initially, then test with a known anonymous IP before enabling 'On'. Check Microsoft Sentinel for any new related incidents.

## Rollback
If the account was disabled in error, re-enable it in Azure AD and revoke the session reset. If the Conditional Access policy causes false positives, switch it to 'Report-only' or adjust the exclusion list.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
- <https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-location>
