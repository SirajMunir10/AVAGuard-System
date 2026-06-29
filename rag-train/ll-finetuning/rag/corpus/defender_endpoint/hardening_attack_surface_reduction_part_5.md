# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How can I verify and enforce that all Windows devices in my tenant have the Attack Surface Reduction (ASR) rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' enabled in block mode?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** ASR rules configured via Intune or Group Policy; devices running Windows 10/11

## Symptoms
- High number of low-prevalence executable files executing on endpoints
- ASR rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' is not in block mode on some devices

## Error Codes
N/A

## Root Causes
1. ASR rule GUID 01443614-cd74-433a-b99e-2ecdc07bfc25 is not deployed or is set to audit mode instead of block mode
2. Devices are not receiving the latest ASR policy from Intune or Group Policy

## Remediation Steps
1. 1. In Microsoft 365 Defender portal, go to Endpoints > Configuration management > Endpoint security policies > Attack surface reduction.
2. 2. Create or edit a policy and add the rule with GUID 01443614-cd74-433a-b99e-2ecdc07bfc25 set to 'Block'.
3. 3. Assign the policy to the appropriate device groups.
4. 4. Alternatively, use Group Policy: Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction > 'Configure Attack Surface Reduction rules'. Set the rule GUID to '1' (block).
5. 5. Verify deployment using the ASR report in Microsoft 365 Defender or by running Get-MpPreference on endpoints.

## Validation
Run the following PowerShell command on a test device as Administrator: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Confirm GUID 01443614-cd74-433a-b99e-2ecdc07bfc25 appears and its corresponding value in AttackSurfaceReductionRules_Actions is 1 (block).

## Rollback
Set the ASR rule to 'Audit mode' (value 2) or remove the rule from the policy assignment.

## References
- Microsoft Learn: 'Use attack surface reduction rules to prevent malware infection' - https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction?view=o365-worldwide
- Microsoft Learn: 'Enable attack surface reduction rules' - https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-attack-surface-reduction?view=o365-worldwide
