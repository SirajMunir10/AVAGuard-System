# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I verify and enable the 'Block all Office applications from creating child processes' ASR rule using Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5 / Defender for Endpoint Plan 2)
- **Configuration:** Attack Surface Reduction rules configured via Intune or Group Policy

## Symptoms
- Office applications (e.g., Word, Excel) are observed spawning child processes such as cmd.exe or powershell.exe
- ASR rule GUID 'd4f940ab-401b-4efc-aadc-ad5f3c50688a' is not in audit or block mode in the tenant's ASR policy
- Security operations center (SOC) alerts indicate potential Office-based living-off-the-land binary (LOLBIN) attacks

## Error Codes
N/A

## Root Causes
1. The ASR rule 'Block all Office applications from creating child processes' is either not deployed or is set to 'Not configured'
2. Organizational Group Policy or Intune security baseline does not include this rule in block mode

## Remediation Steps
1. 1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com) > Endpoints > Attack surface management > Attack surface reduction rules.
2. 2. Identify the rule with GUID d4f940ab-401b-4efc-aadc-ad5f3c50688a and set it to 'Block' mode.
3. 3. If using Intune, create or modify a device configuration profile for 'Endpoint Protection' > 'Attack Surface Reduction' and set the rule to 'Block'.
4. 4. If using Group Policy, configure the rule under Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction.
5. 5. Deploy the policy to target devices and monitor compliance via the Defender for Endpoint reports.

## Validation
Run the following PowerShell command as Administrator on a test device: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Confirm that GUID d4f940ab-401b-4efc-aadc-ad5f3c50688a appears with a value of 1 (block).

## Rollback
Set the rule to 'Audit mode' (value 2) or 'Disabled' (value 0) via the same policy channel used for deployment, then reapply the policy.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-all-office-applications-from-creating-child-processes>
