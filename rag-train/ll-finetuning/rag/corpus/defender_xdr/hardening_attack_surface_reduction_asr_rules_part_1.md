# Hardening: Attack Surface Reduction (ASR) Rules

**Domain:** Defender XDR
**Subdomain:** Attack Surface Reduction (ASR) Rules
**Incident Type:** Hardening

## Scenario / Query
How do I configure and validate Attack Surface Reduction (ASR) rules in Microsoft Defender for Endpoint to block common malware behaviors, and what are the documented steps to test these rules in audit mode before enabling them in block mode?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** ASR rules are managed via Microsoft Intune or Group Policy; audit mode is enabled using the 'Block all Office applications from creating child processes' rule (GUID: d4e940b7-5b3a-4f6b-9a8c-2c8f1e2a3b4c) as an example.

## Symptoms
- Suspicious child processes launched from Office applications
- Increased alerts for behavior that ASR rules are designed to block

## Error Codes
N/A

## Root Causes
1. ASR rules not deployed or configured in block mode
2. ASR rules not tested in audit mode before enforcement

## Remediation Steps
1. 1. Identify the ASR rule GUID for the desired protection (e.g., 'Block all Office applications from creating child processes' GUID: d4e940b7-5b3a-4f6b-9a8c-2c8f1e2a3b4c).
2. 2. Configure the rule in audit mode using Group Policy: Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction > 'Configure Attack Surface Reduction rules' set to 'Enabled' with the rule GUID and action '1' (audit).
3. 3. Validate audit events in Event Viewer under 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational' (Event ID 1121 for blocked, 1122 for audited).
4. 4. After testing, change the action to '2' (block) in the same policy.
5. 5. Monitor Microsoft 365 Defender portal for ASR rule detections and adjust exclusions as needed.

## Validation
Run the PowerShell command: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids to confirm the rule is present and check the action state. For audit mode, verify Event ID 1122 appears in the operational log when the rule would have blocked an action.

## Rollback
Set the ASR rule action back to '1' (audit) or remove the rule GUID from the policy to disable it.

## References
- Microsoft Learn: 'Attack surface reduction rules overview'
- Microsoft Learn: 'Enable attack surface reduction rules' - https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-attack-surface-reduction-rules?view=o365-worldwide
