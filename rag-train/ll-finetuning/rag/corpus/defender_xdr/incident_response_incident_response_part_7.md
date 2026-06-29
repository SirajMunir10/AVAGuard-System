# Incident Response: Incident Response

**Domain:** Defender XDR
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security operations analyst receives a high-severity incident in Microsoft 365 Defender indicating that a user account was compromised via a phishing link. The incident shows that the attacker used the compromised account to access sensitive SharePoint files and then attempted to exfiltrate data via an external email. How should the analyst triage, contain, and remediate this incident using Microsoft Defender XDR capabilities?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Office 365 Plan 2, Microsoft Defender for Identity, and Microsoft Defender for Cloud Apps
- **Configuration:** Alert policies for phishing and malware are enabled; automatic investigation and response (AIR) is turned on; user and entity behavior analytics (UEBA) is active.

## Symptoms
- High-severity incident generated in Microsoft 365 Defender portal
- User reported receiving a suspicious email and clicking a link
- Multiple alerts for 'Phish delivered due to tenant or user override' and 'Mailbox accessed by suspicious application'
- Unusual external email forwarding rule created on the compromised mailbox
- Access to SharePoint files from an unfamiliar IP address
- Data exfiltration alert from Microsoft Defender for Cloud Apps

## Error Codes
N/A

## Root Causes
1. User clicked a malicious link in a phishing email that bypassed initial filtering due to a user-level allow override
2. Attacker used the compromised credentials to sign in and establish persistence via an email forwarding rule
3. Lack of conditional access policies to block sign-ins from untrusted locations

## Remediation Steps
1. 1. In the Microsoft 365 Defender portal, open the incident and review the alert timeline to understand the attack chain.
2. 2. Use the 'Account' page to disable the compromised user account immediately to stop further access.
3. 3. Reset the user's password and revoke all active sessions and tokens (Microsoft 365 Defender > User > Reset password and Revoke sessions).
4. 4. Remove any suspicious email forwarding rules from the mailbox using the Exchange admin center or PowerShell (Remove-MailboxFolderPermission -Identity user@contoso.com -User ExternalUser).
5. 5. Run a manual investigation on the affected SharePoint sites to identify and remove any malicious files or sharing links.
6. 6. Review and update anti-phishing policies to remove any user allow overrides that permitted the phishing email.
7. 7. Create a conditional access policy to block sign-ins from untrusted IP ranges and require multifactor authentication for all users.
8. 8. Submit the phishing email to Microsoft for analysis using the Submissions page in Microsoft 365 Defender.

## Validation
Verify that the user account is disabled, password reset is complete, no unauthorized forwarding rules remain, and no further suspicious sign-ins are detected from the compromised account. Confirm that the incident is resolved in the Microsoft 365 Defender portal.

## Rollback
If remediation steps cause unintended lockout, re-enable the user account temporarily from the Microsoft 365 admin center, but ensure multifactor authentication is enforced and a new password is set immediately.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/respond-to-compromised-email-account>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/incident-response-overview>
