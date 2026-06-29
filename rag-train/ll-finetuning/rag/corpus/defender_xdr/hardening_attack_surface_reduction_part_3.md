# Hardening: Attack Surface Reduction

**Domain:** Defender XDR
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that the 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' ASR rule is not enabled on any devices. How should the administrator enable this rule using Microsoft Intune or Group Policy to reduce the risk of untrusted executables?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Attack surface reduction rules are not configured; devices run Windows 10/11 and are managed via Intune and Group Policy.

## Symptoms
- No devices show the ASR rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' as enabled in the Microsoft 365 Defender portal.
- Security recommendations in Microsoft Defender for Endpoint indicate this rule is missing.

## Error Codes
N/A

## Root Causes
1. Attack surface reduction rules have not been deployed via Group Policy or Intune.
2. The specific ASR rule GUID (01443614-cd74-433a-b99e-2ecdc07bfc25) is not configured in any policy.

## Remediation Steps
1. 1. In Microsoft Intune, navigate to Endpoint security > Attack surface reduction > Create policy > Windows 10 and later > Attack surface reduction rules.
2. 2. Set the rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' to 'Block' (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25).
3. 3. Assign the policy to the appropriate device groups.
4. 4. Alternatively, in Group Policy, go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction > 'Configure Attack Surface Reduction rules' and enable the rule with the GUID and action '1' (Block).
5. 5. Verify deployment by running Get-MpPreference on a client device and checking the AttackSurfaceReductionRules_Ids and AttackSurfaceReductionRules_Actions values.

## Validation
On a test device, run 'Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions' and confirm the GUID 01443614-cd74-433a-b99e-2ecdc07bfc25 appears with action 1 (Block).

## Rollback
In Intune, change the rule setting to 'Not configured' or 'Audit only'. In Group Policy, set the rule to 'Disabled' or remove the GUID from the configured list.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
