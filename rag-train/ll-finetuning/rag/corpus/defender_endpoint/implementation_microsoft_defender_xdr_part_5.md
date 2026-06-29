# Implementation: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Implementation

## Scenario / Query
How does Microsoft Defender XDR detect and remediate a common cyber-attack starting with a phishing email?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Defender for Office 365, Defender for Endpoint, Defender for Identity, Defender for Cloud Apps

## Symptoms
- Phishing email arrives at Inbox
- User opens email attachment
- Attachment installs malware
- Chain of attack attempts leads to theft of sensitive data

## Error Codes
N/A

## Root Causes
1. Phishing email with malicious attachment

## Remediation Steps
1. Use built-in security features for all cloud mailboxes (part of Defender for Office 365) to detect phishing email
2. Use Exchange mail flow rules (transport rules) to prevent phishing email from arriving in user's Inbox
3. Use Safe Attachments to test attachment and determine it's harmful
4. Use policies to prevent harmful mail from arriving at all
5. Use Defender for Endpoint to detect device and network vulnerabilities
6. Use Defender for Identity to detect sudden on-premises user account changes like privilege escalation or high-risk lateral movement
7. Use Defender for Identity to report on easily exploited identity issues like unconstrained Kerberos delegation for correction by security team
8. Use Defender for Cloud Apps to detect anomalous behavior such as impossible-travel, credential access, and unusual downloading, file sharing, or mail forwarding activity

## Validation
1. Verify that Defender for Office 365 is enabled and configured: In the Microsoft 365 Defender portal, go to Policies & rules > Threat policies > Anti-phishing. Confirm that the policy is applied to all users and that spoof intelligence and impersonation protection are turned on. 2. Check that Safe Attachments policies are active: Navigate to Policies & rules > Threat policies > Safe Attachments. Ensure a policy is in place that scans all messages and attachments. 3. Confirm mail flow rules (transport rules) are set: In Exchange admin center, go to Mail flow > Rules. Verify a rule exists to block or quarantine emails with known phishing indicators. 4. Validate Defender for Endpoint detection: On a test device, run 'Get-MpThreatDetection' in PowerShell to confirm recent malware detections. 5. Check Defender for Identity alerts: In Microsoft 365 Defender, go to Incidents & alerts > Alerts. Filter by source 'Microsoft Defender for Identity' and confirm alerts for privilege escalation or lateral movement are present. 6. Review Defender for Cloud Apps activity logs: In the Cloud Apps portal, go to Activity log. Look for anomalous behaviors like impossible-travel or mass download events.

## Rollback
1. Disable or remove the mail flow rule: In Exchange admin center, go to Mail flow > Rules, select the rule, and click 'Delete' or set its state to 'Disabled'. 2. Turn off Safe Attachments policy: In Microsoft 365 Defender, go to Policies & rules > Threat policies > Safe Attachments, select the policy, and click 'Turn off policy'. 3. Disable anti-phishing policy: Navigate to Policies & rules > Threat policies > Anti-phishing, select the policy, and click 'Turn off policy'. 4. If Defender for Endpoint detection caused false positives, submit the file for analysis and add an exclusion: In Microsoft 365 Defender, go to Settings > Endpoints > Indicators, add a file hash or path exclusion. 5. For Defender for Identity, if alerts are noisy, adjust sensitivity: In Microsoft 365 Defender, go to Settings > Identities > Alert tuning, and modify the relevant alert rule. 6. For Defender for Cloud Apps, if anomalous behavior detection is too aggressive, reduce sensitivity: In Cloud Apps portal, go to Policies, edit the policy, and lower the risk score threshold.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
