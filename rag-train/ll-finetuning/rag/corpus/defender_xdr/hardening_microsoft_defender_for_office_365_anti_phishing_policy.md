# Hardening: Microsoft Defender for Office 365 â€“ Anti-Phishing Policy

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365 â€“ Anti-Phishing Policy
**Incident Type:** Hardening

## Scenario / Query
How can I harden my Microsoft 365 tenant against advanced phishing attacks by configuring anti-phishing policies to protect impersonated users and domains, and what are the recommended settings according to Microsoft documentation?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Anti-phishing policies are currently using default settings; no custom impersonation protection is enabled.

## Symptoms
- Users report receiving emails that appear to come from the CEO or other executives but contain suspicious links.
- Security team observes an increase in phishing simulation failures involving impersonated internal domains.

## Error Codes
N/A

## Root Causes
1. Anti-phishing policy does not include protected users or domains for impersonation detection.
2. Default policy settings do not apply advanced impersonation protection.

## Remediation Steps
1. Navigate to Microsoft 365 Defender portal > Email & collaboration > Policies & rules > Threat policies > Anti-phishing.
2. Select the default anti-phishing policy (or create a new one) and click Edit protection settings.
3. Under Impersonation, toggle 'Protect users you specify' to On and add the CEO, CFO, and other key executives as protected users.
4. Toggle 'Protect domains you own' to On to automatically protect your custom domain.
5. Toggle 'Protect domains you specify' to On and add partner domains that are frequently impersonated.
6. Under Mailbox intelligence, ensure 'Enable mailbox intelligence' and 'Enable intelligence for impersonation protection' are both turned On.
7. Under Actions, set 'If email is detected as an impersonation attempt' to 'Quarantine the email' for both impersonated users and domains.
8. Under Phishing threshold, select 'Aggressive' to increase detection sensitivity.
9. Click Save to apply the policy.

## Validation
Use the Microsoft 365 Defender portal to run a simulated phishing attack targeting an impersonated user; verify the email is quarantined. Alternatively, use the Threat Explorer to confirm that impersonation detections are occurring.

## Rollback
Edit the anti-phishing policy and revert actions to 'Move the message to the recipients' Junk Email folder' or disable impersonation protection for specific users/domains.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-mdo-configure-and-learn>
