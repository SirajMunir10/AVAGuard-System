# Incident Response: Incident Response

**Domain:** Defender XDR
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security operations analyst receives a high-severity incident in Microsoft 365 Defender titled 'Possible password spray attack' affecting multiple user accounts. The analyst needs to investigate the incident, identify affected users and source IPs, and contain the attack by disabling compromised accounts and blocking malicious IPs. What steps should the analyst take using Microsoft 365 Defender and Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Identity and Azure AD Premium P2
- **Configuration:** Microsoft 365 Defender incident queue enabled; Defender for Identity sensor deployed on domain controllers; Azure AD Identity Protection enabled

## Symptoms
- Multiple failed sign-in attempts from different IP addresses across several user accounts
- Incident alert in Microsoft 365 Defender with title 'Possible password spray attack'
- User accounts showing 'Compromised' or 'High risk' in Azure AD Identity Protection

## Error Codes
N/A

## Root Causes
1. Attacker performing password spray attack using a common password against multiple accounts
2. No conditional access policy blocking suspicious sign-ins from untrusted IPs
3. Legacy authentication protocols enabled, allowing brute-force attempts

## Remediation Steps
1. Open the incident in Microsoft 365 Defender portal (https://security.microsoft.com) and review the alert details, affected users, and evidence timeline.
2. Use the 'Investigate' tab to view related alerts and entities (IPs, user accounts, devices).
3. For each compromised user account, navigate to Azure AD > Users > select the user > 'Revoke sessions' and 'Reset password' to force reauthentication.
4. Block the identified malicious source IPs using Azure AD Conditional Access: Create a policy to block sign-ins from those IPs (Azure AD > Security > Conditional Access > New policy > Assignments > Conditions > Locations > Include selected IPs > Block access).
5. Disable legacy authentication protocols by enabling a Conditional Access policy that blocks legacy authentication (Azure AD > Security > Conditional Access > New policy > Assign to all users > Cloud apps > All cloud apps > Conditions > Client apps > Exchange ActiveSync clients and other clients > Block).
6. Enable Azure AD Identity Protection to automatically detect and remediate password spray attacks (Azure AD > Security > Identity Protection > MFA registration policy and User risk policy).
7. Review and update incident response playbook to include password spray containment steps.

## Validation
Verify that all compromised user accounts have had their passwords reset and sessions revoked. Confirm that the malicious IPs are blocked by attempting a sign-in from a test IP (if safe) or reviewing Conditional Access logs. Ensure no further failed sign-in alerts appear for the same IPs.

## Rollback
If blocking an IP was an error, remove the IP from the Conditional Access location list. If a user account was incorrectly disabled, re-enable it via Azure AD admin center and reset the password again if needed.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/investigate-password-spray?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/security/compass/incident-response-playbook-password-spray>
