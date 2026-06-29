# Hardening: Alert Tuning

**Domain:** Defender for Endpoint
**Subdomain:** Alert Tuning
**Incident Type:** Hardening

## Scenario / Query
How do I review and manage built-in alert tuning rules in Microsoft Defender XDR to reduce noise from benign activity?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Alert tuning rules

## Symptoms
- Alerts from common benign activity appear in the Microsoft Defender portal
- AIR investigations and email notifications are affected by alert suppression

## Error Codes
N/A

## Root Causes
1. Built-in alert tuning rules suppress alerts without affecting other features like AIR investigations and email notifications

## Remediation Steps
1. Go to System > Settings > Microsoft Defender XDR > Rules section > Alert tuning in the Microsoft Defender portal
2. Alternatively, navigate directly to the Alert tuning page at https://security.microsoft.com/securitysettings/defender/alert_suppression
3. Review the built-in rules to understand how they might affect which alerts appear in the Microsoft Defender portal
4. Disable the Auto-Resolve - Email reported by user as malware or phish built-in alert tuning rule and any custom tuning rules that suppress this alert if using Microsoft Security Copilot Phishing Triage Agent

## Validation
1. Navigate to the Alert tuning page at https://security.microsoft.com/securitysettings/defender/alert_suppression. 2. Confirm that the built-in rule 'Auto-Resolve - Email reported by user as malware or phish' is listed and its status is 'Disabled'. 3. Verify that any custom tuning rules previously suppressing the same alert are also disabled. 4. In the Microsoft Defender portal, go to Incidents & alerts > Alerts and search for alerts related to 'Email reported by user as malware or phish' to confirm they now appear. 5. Check that AIR investigations and email notifications for this alert type are no longer suppressed by reviewing recent investigation history and notification logs.

## Rollback
1. Navigate to the Alert tuning page at https://security.microsoft.com/securitysettings/defender/alert_suppression. 2. Re-enable the built-in rule 'Auto-Resolve - Email reported by user as malware or phish' by toggling it back to 'Enabled'. 3. Re-enable any custom tuning rules that were disabled during remediation. 4. Confirm that alerts for this type are again suppressed in the Microsoft Defender portal. 5. Verify that AIR investigations and email notifications are once again affected by the suppression rules.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
