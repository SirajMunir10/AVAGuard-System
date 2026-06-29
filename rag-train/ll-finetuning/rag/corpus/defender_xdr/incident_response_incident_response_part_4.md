# Incident Response: Incident Response

**Domain:** Defender XDR
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A user reports receiving multiple suspicious emails with attachments that appear to be invoices. Microsoft Defender for Office 365 has flagged them as phishing attempts, but the user clicked a link in one of the emails. How do I investigate and remediate this incident using Microsoft 365 Defender?

## Environment Context
- **Tenant Type:** Enterprise E5
- **Configuration:** Microsoft 365 Defender portal enabled, Defender for Office 365 Plan 2, audit logging enabled

## Symptoms
- User received multiple phishing emails with malicious attachments
- User clicked a link in one of the phishing emails
- Defender for Office 365 flagged the emails as phishing but did not block the link click

## Error Codes
N/A

## Root Causes
1. User interaction with a malicious link bypassed automated protection
2. Phishing email was delivered to inbox due to policy configuration or delay in detection

## Remediation Steps
1. In Microsoft 365 Defender portal, go to Incidents & alerts > Incidents and locate the incident related to the phishing emails.
2. Review the incident timeline and affected assets (user, device, email).
3. Use the email entity page to identify the specific email messages and their delivery status.
4. If malicious, delete the email from the user's mailbox using Threat Explorer or the 'Delete email' action in the email entity page.
5. Run an antivirus scan on the user's device using Microsoft Defender for Endpoint.
6. If the user entered credentials on the phishing site, force a password reset and require MFA re-enrollment.
7. Enable Safe Links and Safe Attachments policies to block similar threats in the future.
8. Submit the email as a sample to Microsoft for analysis if needed.

## Validation
Confirm that the phishing email is no longer in the user's mailbox and that no further suspicious activity is detected on the user's device or account.

## Rollback
If the email was deleted by mistake, recover it from the Deleted Items folder or use eDiscovery to restore it.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/investigate-incidents?view=o365-worldwide>
