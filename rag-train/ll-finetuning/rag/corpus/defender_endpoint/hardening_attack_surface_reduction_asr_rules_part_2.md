# Hardening: Attack Surface Reduction (ASR) Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction (ASR) Rules
**Incident Type:** Hardening

## Scenario / Query
How do I enable and monitor Attack Surface Reduction (ASR) rules in Microsoft Defender for Endpoint to block common malware techniques, and what are the documented audit and block modes?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** ASR rules not yet deployed; devices running Windows 10/11 with Microsoft Defender Antivirus as the primary AV

## Symptoms
- Security team identifies that common malware persistence techniques (e.g., Office macro execution, script obfuscation) are not being blocked
- Microsoft 365 Defender portal shows no ASR rule events in the past 30 days
- Security baseline assessment indicates ASR rules are not configured

## Error Codes
N/A

## Root Causes
1. ASR rules have not been enabled via Group Policy, Intune, or Microsoft 365 Defender configuration
2. No ASR rule policies are assigned to the device group

## Remediation Steps
1. 1. In the Microsoft 365 Defender portal, go to Settings > Endpoints > Attack surface reduction > Attack surface reduction rules.
2. 2. Click 'Create policy' and select a device group (e.g., 'All devices').
3. 3. For each ASR rule you want to enable, set the action to 'Block' or 'Audit' based on your testing requirements. Documented rules include: Block Office communication applications from creating child processes (GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869), Block executable files from running unless they meet a prevalence, age, or trusted list criterion (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25), and others listed in the official documentation.
4. 4. Configure exclusions for legitimate software that may be blocked.
5. 5. Assign the policy to the target device group and save.
6. 6. Monitor ASR events in the Microsoft 365 Defender portal under Reports > Attack surface reduction rules.

## Validation
Confirm that ASR rule events appear in the Microsoft 365 Defender portal (e.g., event ID 1121 for blocked, 1122 for audited). Use Get-MpPreference in PowerShell to verify local ASR rule state on a test device.

## Rollback
In the Microsoft 365 Defender portal, edit the ASR rule policy and set each rule to 'Not configured' or 'Audit' mode, then remove the policy assignment. Alternatively, delete the policy entirely.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
