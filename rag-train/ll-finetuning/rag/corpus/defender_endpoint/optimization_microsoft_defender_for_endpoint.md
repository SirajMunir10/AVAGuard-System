# Optimization: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Optimization

## Scenario / Query
How to safely configure attack surface reduction rules to avoid interrupting legitimate business processes?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Attack surface reduction rules

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure all available attack surface reduction rules to Audit.
2. Identify which rules are safe to turn on based on audit results.
3. Enable those settings on endpoints which do not have false positive detections.

## Validation
1. Verify that all attack surface reduction rules are set to Audit mode by running the following PowerShell command on a test endpoint: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions. Confirm each rule shows '1' (Audit).
2. Check the Microsoft 365 Defender portal (https://security.microsoft.com) under 'Endpoints' > 'Attack surface reduction rules' to ensure the rules are deployed with 'Audit' action.
3. Review audit events in Event Viewer under 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational' for Event ID 5007 (rule triggered) to confirm no false positives are blocking legitimate processes.
4. After enabling selected rules, run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions to confirm the enabled rules show '1' (Block) and others remain '1' (Audit) or are disabled.

## Rollback
1. If audit reveals false positives or business disruption, revert all rules to Audit mode by setting each rule's action to '1' using Set-MpPreference -AttackSurfaceReductionRules_Ids <RuleID> -AttackSurfaceReductionRules_Actions 1.
2. Alternatively, disable all attack surface reduction rules by running Set-MpPreference -DisableAttackSurfaceReductionRules $true on affected endpoints.
3. In the Microsoft 365 Defender portal, navigate to 'Endpoints' > 'Attack surface reduction rules' and change the action for any problematic rule back to 'Audit' or 'Off'.
4. Monitor Event ID 5007 to confirm rollback is effective and no further blocks occur.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
