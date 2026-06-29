# Incident Response: Incident Response

**Domain:** Defender XDR
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A user reports receiving multiple suspicious emails with attachments. The security team suspects a phishing campaign targeting credential harvesting. How should the incident response team use Microsoft Defender XDR to investigate, contain, and remediate this incident?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Office 365 Plan 2
- **Configuration:** Anti-phishing policies enabled; Safe Attachments and Safe Links policies configured; audit logging enabled

## Symptoms
- User reports receiving emails with unusual sender addresses and urgent language
- Multiple users in the same department report similar emails
- Some users clicked links in the emails and entered credentials on a fake login page

## Error Codes
N/A

## Root Causes
1. Phishing campaign targeting the organization
2. Users were not sufficiently trained to identify phishing attempts
3. Some anti-phishing policies may not cover all email scenarios

## Remediation Steps
1. Use the Microsoft 365 Defender portal to investigate the incident: navigate to Incidents & alerts > Incidents and select the relevant incident
2. Review the email entity details to identify the sender, subject, and any attachments or URLs
3. Use Threat Explorer in Microsoft Defender for Office 365 to search for similar emails and identify the full scope of the campaign
4. Submit the phishing emails to Microsoft for analysis using the Submissions page in the Microsoft 365 Defender portal
5. Block the sender and URLs using Tenant Allow/Block Lists
6. Remove any malicious emails from user mailboxes using the Threat Explorer 'Take action' feature (e.g., soft delete or move to junk)
7. Reset passwords for any users who entered credentials on the phishing site and enforce multi-factor authentication
8. Review and update anti-phishing policies to increase protection

## Validation
Verify that the malicious emails are no longer present in user mailboxes and that no further users have reported similar emails. Confirm that blocked senders and URLs are enforced.

## Rollback
If a legitimate sender was incorrectly blocked, remove the entry from the Tenant Allow/Block Lists. If emails were incorrectly deleted, use the Recoverable Items folder or eDiscovery to restore them.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/investigate-incidents>
- <https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/responding-to-a-compromised-email-account>
