# Hardening: Attack Surface Reduction

**Domain:** Defender XDR
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How can I verify and enforce that all devices in my tenant have the recommended ASR rules enabled to block common malware and ransomware behaviors?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Attack Surface Reduction (ASR) rules are not enforced; some devices have rules disabled or set to Audit mode.

## Symptoms
- High number of malware alerts from devices that should be protected by ASR rules
- ASR rule events show 'Audited' instead of 'Blocked' in Microsoft 365 Defender portal
- Security recommendations in Microsoft Secure Score indicate low ASR rule coverage

## Error Codes
N/A

## Root Causes
1. ASR rules are not configured via Group Policy, Intune, or Microsoft 365 Defender policy
2. Some ASR rules are set to Audit mode instead of Block mode
3. Devices are not receiving the latest ASR rule definitions

## Remediation Steps
1. In the Microsoft 365 Defender portal, go to Endpoints > Configuration management > Endpoint security policies > Attack surface reduction and create a policy with the recommended ASR rules set to 'Block'.
2. Use Microsoft Intune to deploy a device configuration profile for Windows 10/11 with ASR rules enabled under Endpoint protection > Microsoft Defender Exploit Guard > Attack Surface Reduction.
3. Alternatively, use Group Policy: Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction, and set each rule GUID to '1' (Block).
4. After applying the policy, run the PowerShell command Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids to verify the rules are enabled.
5. Monitor ASR rule events in Microsoft 365 Defender using the advanced hunting query: DeviceEvents | where ActionType startswith 'Asr'.

## Validation
Check Microsoft Secure Score for the 'Enable attack surface reduction rules' recommendation and confirm the score has increased. Also verify in the Microsoft 365 Defender portal under Reports > Attack surface reduction rules that the 'Blocked' count is increasing.

## Rollback
Set the ASR rules to 'Not configured' or 'Audit mode' (GUID value '2') in the policy, then force a policy refresh on devices.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-deployment?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
