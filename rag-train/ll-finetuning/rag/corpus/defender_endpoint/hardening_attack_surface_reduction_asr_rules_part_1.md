# Hardening: Attack Surface Reduction (ASR) Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction (ASR) Rules
**Incident Type:** Hardening

## Scenario / Query
How do I verify and enable the 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' ASR rule in Microsoft Defender for Endpoint to harden endpoints against untrusted executables?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Attack Surface Reduction rules are enabled via Group Policy, Intune, or Microsoft 365 Defender portal. The specific rule GUID is 01443614-cd74-433a-b99e-2ecdc07bfc25.

## Symptoms
- Security team identifies a high volume of unknown or unsigned executables being launched on endpoints.
- Microsoft 365 Defender portal shows ASR rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' is not enabled or is in Audit mode.

## Error Codes
N/A

## Root Causes
1. ASR rule 01443614-cd74-433a-b99e-2ecdc07bfc25 is not configured to Block mode.
2. Group Policy or Intune policy does not include this rule or is set to Audit only.

## Remediation Steps
1. 1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a Global Administrator or Security Administrator.
2. 2. Navigate to Endpoints > Configuration management > Attack surface reduction rules.
3. 3. Locate the rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25).
4. 4. Set the rule to 'Block' mode and apply to all devices.
5. 5. Alternatively, deploy via Group Policy: Set the rule GUID to 1 (Block) using the 'Configure Attack Surface Reduction rules' policy under Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction.
6. 6. For Intune: Create or modify a device configuration profile (Endpoint protection profile) and set the ASR rule to 'Block'.
7. 7. Monitor the rule's impact using the Microsoft 365 Defender portal or Microsoft Defender for Endpoint advanced hunting.

## Validation
Run the following PowerShell command as Administrator on a test device to confirm the rule is enabled and in Block mode: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Verify the GUID 01443614-cd74-433a-b99e-2ecdc07bfc25 is present and its corresponding value in AttackSurfaceReductionRules_Actions is 1 (Block).

## Rollback
Set the rule to 'Audit' mode or 'Disabled' via the same management tool (Microsoft 365 Defender portal, Group Policy, or Intune). For Group Policy, set the rule GUID to 2 (Audit) or remove the rule from the policy. For Intune, change the setting to 'Audit' or 'Not configured'.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
