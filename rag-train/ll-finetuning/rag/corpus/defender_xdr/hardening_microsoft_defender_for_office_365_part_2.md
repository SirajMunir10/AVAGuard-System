# Hardening: Microsoft Defender for Office 365

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365
**Incident Type:** Hardening

## Scenario / Query
How can I harden my Microsoft 365 tenant against common phishing and malware attacks by configuring anti-phishing and anti-malware policies in Microsoft Defender for Office 365?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Default anti-phishing and anti-malware policies are in place, but no custom policies have been created.

## Symptoms
- Users report receiving phishing emails that bypass default protection
- Malware attachments are delivered to inboxes despite default filtering

## Error Codes
N/A

## Root Causes
1. Default anti-phishing policy does not include impersonation protection for key users and domains
2. Default anti-malware policy uses only the common attachments filter and does not enable zero-hour auto purge (ZAP) for malware

## Remediation Steps
1. Create a custom anti-phishing policy that includes impersonation protection for your CEO, CFO, and other high-profile users, as well as your own domain and partner domains. Set the policy to apply to all users.
2. Create a custom anti-malware policy that enables the common attachments filter, enables zero-hour auto purge (ZAP) for malware, and sets the malware alert notification to notify admins. Apply the policy to all users.
3. Verify that the policies are applied by checking the policy list in the Microsoft 365 Defender portal under Email & collaboration > Policies & rules > Threat policies.

## Validation
Send a test phishing email using the Attack Simulator in Microsoft 365 Defender to confirm that the custom anti-phishing policy blocks the simulated attack. Send a test malware attachment (e.g., EICAR test file) to confirm that the custom anti-malware policy quarantines the message.

## Rollback
Delete or disable the custom anti-phishing and anti-malware policies in the Microsoft 365 Defender portal to revert to default protection.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about>
- <https://learn.microsoft.com/en-us/defender-office-365/anti-malware-protection-about>
