# Hardening: Attack Surface Reduction (ASR)

**Domain:** Defender XDR
**Subdomain:** Attack Surface Reduction (ASR)
**Incident Type:** Hardening

## Scenario / Query
How can I verify and enforce that all Windows 10/11 devices in my tenant have the ASR rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25) enabled in 'Block' mode via Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Attack surface reduction rules are managed via Microsoft Intune or Group Policy; verification uses Microsoft 365 Defender portal > Reports > Attack surface reduction rules.

## Symptoms
- Security team cannot confirm whether the ASR rule is enabled across all endpoints
- High number of alerts for executable files that should have been blocked by the rule
- Compliance reports show devices with ASR rule in 'Audit' mode instead of 'Block' mode

## Error Codes
N/A

## Root Causes
1. ASR rule not deployed via Intune or Group Policy
2. Rule configured in Audit mode instead of Block mode
3. Devices not receiving updated policy due to connectivity or configuration drift

## Remediation Steps
1. In the Microsoft 365 Defender portal, go to Reports > Attack surface reduction rules to identify devices where the rule is not enabled or is in Audit mode.
2. For Intune-managed devices: Navigate to Endpoint security > Attack surface reduction > Create policy > Platform: Windows 10 and later > Profile: Attack surface reduction rules. Set rule GUID 01443614-cd74-433a-b99e-2ecdc07bfc25 to 'Block' and assign to target groups.
3. For Group Policy-managed devices: Use the Group Policy Management Console to configure the ASR rule under Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction. Set the rule to '1' (Block).
4. After policy deployment, run the PowerShell cmdlet Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids to verify the rule is present and enabled on individual devices.

## Validation
Run the following PowerShell command on a test device: Get-MpPreference | Where-Object { $_.AttackSurfaceReductionRules_Ids -contains '01443614-cd74-433a-b99e-2ecdc07bfc25' } | Select-Object AttackSurfaceReductionRules_Actions. Confirm the action value is '1' (Block).

## Rollback
Set the ASR rule action to '2' (Audit) or remove the rule assignment from the Intune policy or Group Policy object.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-attack-surface-reduction?view=o365-worldwide>
