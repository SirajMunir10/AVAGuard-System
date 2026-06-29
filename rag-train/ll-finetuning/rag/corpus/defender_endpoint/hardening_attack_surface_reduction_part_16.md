# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to implement the ASR rule 'Block Office communication application from creating child processes' (GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869) in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Intune name: Block Office communication application from creating child processes; GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869; Advanced hunting action types: AsrOfficeCommAppChildProcessAudited, AsrOfficeCommAppChildProcessBlocked; Dependencies: Microsoft Defender Antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Microsoft Intune to enable the ASR rule with the name 'Block Office communication application from creating child processes'.
2. Ensure Office is installed in %ProgramFiles% or %ProgramFiles(x86)% locations (default: C:\Program Files and C:\Program Files (x86)).
3. Note: This rule has limited exclusion support; refer to File and folder exclusions for ASR rules.
4. Do not use Microsoft Configuration Manager to enable this rule on managed devices if using Configuration Manager, as it blocks processes created through PsExec and WMI.

## Validation
1. In Microsoft Intune, navigate to Endpoint Security > Attack Surface Reduction > Policies and confirm the ASR rule 'Block Office communication application from creating child processes' (GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869) is configured with action 'Block' and assigned to the target device group.
2. On a target device, run the following PowerShell command as Administrator to verify the rule is active: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids | Where-Object {$_ -eq '{26190899-1602-49e8-8b27-eb1d0a1ce869}'}.
3. Confirm the rule's action is set to 1 (Block) by running: (Get-MpPreference).AttackSurfaceReductionRules_Actions[(Get-MpPreference).AttackSurfaceReductionRules_Ids.IndexOf('{26190899-1602-49e8-8b27-eb1d0a1ce869}')].
4. Use Advanced Hunting in Microsoft 365 Defender to search for events with ActionType 'AsrOfficeCommAppChildProcessBlocked' from the target device to confirm the rule is blocking child processes.
5. Verify that Office applications are installed in %ProgramFiles% or %ProgramFiles(x86)% (default locations) to ensure the rule applies correctly.

## Rollback
1. In Microsoft Intune, navigate to Endpoint Security > Attack Surface Reduction > Policies, select the policy containing the ASR rule, and change the action for rule GUID 26190899-1602-49e8-8b27-eb1d0a1ce869 to 'Audit' or 'Disabled'.
2. Alternatively, remove the rule from the policy assignment or delete the policy if no other rules are needed.
3. On a target device, run the following PowerShell command as Administrator to disable the rule: Add-MpPreference -AttackSurfaceReductionRules_Ids '{26190899-1602-49e8-8b27-eb1d0a1ce869}' -AttackSurfaceReductionRules_Actions Disabled.
4. To revert to a previous state, use: Remove-MpPreference -AttackSurfaceReductionRules_Ids '{26190899-1602-49e8-8b27-eb1d0a1ce869}'.
5. Use Advanced Hunting to search for events with ActionType 'AsrOfficeCommAppChildProcessAudited' to confirm the rule is no longer blocking.
6. If the rule was enabled via Configuration Manager, ensure no conflicting policies are applied and remove the rule from Configuration Manager baselines.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
