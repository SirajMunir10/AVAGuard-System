# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block all Office applications from creating child processes using ASR rule GUID d4f940ab-401b-4efc-aadc-ad5f3c50688a?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Office installed in %ProgramFiles% or %ProgramFiles(x86)% locations (default: C:\Program Files and C:\Program Files (x86))

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable ASR rule 'Block all Office applications from creating child processes' using GUID d4f940ab-401b-4efc-aadc-ad5f3c50688a in Microsoft Intune or Microsoft Configuration Manager.
2. Ensure Office is installed in %ProgramFiles% or %ProgramFiles(x86)% locations for the rule to be enforced.

## Validation
1. Confirm the ASR rule is enabled: Run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids and verify that 'd4f940ab-401b-4efc-aadc-ad5f3c50688a' appears in the list. 2. Check the rule action: Run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions and confirm the corresponding action is '1' (Block). 3. Test the rule: Attempt to launch a child process from an Office application (e.g., from Word, run 'wmic.exe') and verify that the process is blocked and an event (e.g., Event ID 1121) is generated in the Microsoft-Windows-Windows Defender/Operational log.

## Rollback
1. Disable the ASR rule: Run Set-MpPreference -AttackSurfaceReductionRules_Ids d4f940ab-401b-4efc-aadc-ad5f3c50688a -AttackSurfaceReductionRules_Actions Disabled. 2. Verify the rule is disabled: Run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids and confirm the GUID is no longer present, or its action is '0' (Disabled). 3. If the rule was deployed via Intune or Configuration Manager, remove the rule assignment from the policy and sync devices to revert the change.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
