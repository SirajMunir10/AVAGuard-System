# Optimization: Microsoft Defender for Office 365 â€“ Mailbox Intelligence

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365 â€“ Mailbox Intelligence
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Microsoft Defender for Office 365 mailbox intelligence to reduce false positive user-reported phishing incidents?

## Environment Context
- **Tenant Type:** Enterprise E5
- **Configuration:** Mailbox Intelligence enabled in Microsoft 365 Defender portal under Email & collaboration > Policies & rules > Threat policies > Anti-phishing > Spoof & mailbox intelligence

## Symptoms
- Users report legitimate emails as phishing, causing unnecessary investigation workload
- Mailbox intelligence action recommendations are not being applied automatically
- High volume of user-reported messages in the Quarantine or Admin Review queues

## Error Codes
N/A

## Root Causes
1. Mailbox intelligence is enabled but not configured to automatically apply recommended actions
2. Mailbox intelligence impersonation protection is not tuned to the organization's trusted sender list
3. User training on reporting legitimate vs. malicious emails is insufficient

## Remediation Steps
1. In the Microsoft 365 Defender portal, navigate to Email & collaboration > Policies & rules > Threat policies > Anti-phishing.
2. Select the anti-phishing policy that applies to your users and edit the Mailbox intelligence section.
3. Enable 'Mailbox intelligence' and set 'Mailbox intelligence protection' to 'On' with the action 'Move message to the recipients' Junk Email folder' for impersonated users.
4. Under 'Mailbox intelligence impersonation protection', add trusted senders and domains to the 'Allow' list to reduce false positives.
5. Consider enabling 'User reported settings' to route user-reported messages to a designated mailbox for review and tuning.

## Validation
Verify that mailbox intelligence is enabled and set to automatically apply recommended actions. Check the Mailbox intelligence report in the Microsoft 365 Defender portal to confirm reduction in false positive user-reported phishing.

## Rollback
Set 'Mailbox intelligence protection' back to 'Off' or change the action to 'Do not apply any action' in the anti-phishing policy.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/configure-mailbox-intelligence>
