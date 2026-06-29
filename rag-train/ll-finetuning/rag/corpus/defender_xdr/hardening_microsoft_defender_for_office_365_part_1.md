# Hardening: Microsoft Defender for Office 365

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365
**Incident Type:** Hardening

## Scenario / Query
How do I configure Safe Attachments and Safe Links policies in Microsoft Defender for Office 365 to block malicious content and prevent users from clicking through warnings?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Default Safe Attachments and Safe Links policies are in use; no custom policies have been created.

## Symptoms
- Users receive phishing emails with malicious attachments that are not blocked.
- Users can click through warning pages when accessing malicious URLs.
- No custom Safe Attachments or Safe Links policies are visible in the Defender portal.

## Error Codes
N/A

## Root Causes
1. Default Safe Attachments policy does not apply to all users and does not enable dynamic delivery or automatic block.
2. Default Safe Links policy does not block URLs at time of click and allows users to proceed to the original URL after a warning.

## Remediation Steps
1. Create a new Safe Attachments policy in the Microsoft 365 Defender portal (https://security.microsoft.com) under Email & collaboration > Policies & rules > Threat policies > Safe Attachments.
2. Set the policy to 'Block' mode for unknown malware and enable 'Redirect attachments' with a quarantine mailbox.
3. Apply the policy to all recipients (or a specific domain/group) and set the priority to 0 (highest).
4. Create a new Safe Links policy under Threat policies > Safe Links.
5. Enable 'Scan URLs in email messages' and 'Apply real-time URL scanning for suspicious links and links that point to files'.
6. Enable 'Do not let users click through to the original URL' and 'Do not track when users click Safe Links'.
7. Apply the Safe Links policy to all recipients and set priority to 0.

## Validation
Send a test phishing email with a known malicious attachment and URL to a user covered by the new policies. Verify the attachment is blocked and the URL is not accessible after clicking the link in the email.

## Rollback
Delete the custom Safe Attachments and Safe Links policies, or set their priority to a lower value (e.g., 100) so the default policies take precedence.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-policies>
- <https://learn.microsoft.com/en-us/defender-office-365/safe-links-policies>
