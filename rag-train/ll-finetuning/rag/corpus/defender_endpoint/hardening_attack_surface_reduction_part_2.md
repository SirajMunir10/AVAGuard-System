# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I enable and verify Attack Surface Reduction (ASR) rules using Microsoft Defender for Endpoint to block common malware techniques such as Office macro execution and script-based payloads?

## Environment Context
- **Tenant Type:** Enterprise Microsoft 365 E5
- **Configuration:** Microsoft Defender for Endpoint policies managed via Microsoft Intune or Group Policy

## Symptoms
- Security report shows low ASR rule coverage
- Malware incidents originating from Office macros or scripts are not blocked
- ASR rules are not enforced on endpoints

## Error Codes
N/A

## Root Causes
1. ASR rules not configured or deployed
2. ASR rules set to Audit mode instead of Block mode
3. Exclusions incorrectly defined allowing malicious behavior

## Remediation Steps
1. Identify the appropriate ASR rules for your environment using the Microsoft recommended rules list.
2. Configure ASR rules in Block mode via Microsoft Intune: Devices > Configuration profiles > Create profile > Windows 10 and later > Endpoint protection > Microsoft Defender Exploit Guard > Attack Surface Reduction.
3. Alternatively, deploy ASR rules via Group Policy: Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction.
4. Set each rule GUID to '1' (Block) or '2' (Audit) as needed.
5. Verify deployment by reviewing the ASR rule report in Microsoft 365 Defender portal (Reports > Attack surface reduction rules).

## Validation
Run the following PowerShell command on a test device to confirm ASR rules are active: Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions. Verify that the expected rule GUIDs appear with action '1' (Block).

## Rollback
Set the ASR rule action to '2' (Audit) or remove the rule from the policy to revert to no enforcement.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
