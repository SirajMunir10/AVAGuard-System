# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to detect and block obfuscated scripts using ASR rules?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** ASR rule for script obfuscation detection

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. This ASR rule detects suspicious properties within an obfuscated script
2. Script obfuscation is a common technique used by malware authors and legitimate applications

## Validation
1. Confirm the ASR rule 'Block execution of potentially obfuscated scripts' (GUID: 5beb7efe-fd9a-4556-801d-275e5ffc04cc) is enabled in Microsoft 365 Defender (https://security.microsoft.com/configuration/attacksimulation/overview).
2. Run a test script with known obfuscation patterns (e.g., base64-encoded PowerShell) from a non-admin account on a monitored device.
3. Verify that the script execution is blocked and an alert appears in Microsoft 365 Defender (https://security.microsoft.com/alerts).
4. Check the device's Event Viewer under 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational' for event ID 1121 (block) or 1122 (audit) related to the ASR rule.

## Rollback
1. In Microsoft 365 Defender, navigate to 'Configuration' > 'Attack surface reduction' (https://security.microsoft.com/configuration/attacksimulation/overview).
2. Locate the rule 'Block execution of potentially obfuscated scripts' (GUID: 5beb7efe-fd9a-4556-801d-275e5ffc04cc).
3. Change its state from 'Block' to 'Audit' or 'Off' to allow obfuscated scripts temporarily.
4. If the rule was deployed via Group Policy or Intune, revert the corresponding policy setting to 'Not configured' or 'Audit mode'.
5. Confirm the change by running a previously blocked obfuscated script and verifying it executes without alert.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
