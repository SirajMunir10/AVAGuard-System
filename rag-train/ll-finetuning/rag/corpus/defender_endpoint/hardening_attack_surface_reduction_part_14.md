# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block execution of potentially obfuscated scripts using ASR rule 5beb7efe-fd9a-4556-801d-275e5ffc04cc?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Cloud-delivered protection must be enabled; supports PowerShell scripts

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable cloud-delivered protection in Microsoft Defender Antivirus
2. Deploy ASR rule with GUID 5beb7efe-fd9a-4556-801d-275e5ffc04cc via Intune or Configuration Manager
3. Monitor advanced hunting action types: AsrObfuscatedScriptAudited, AsrObfuscatedScriptBlocked

## Validation
1. Confirm cloud-delivered protection is enabled: Run 'Get-MpPreference | Select-Object CloudBlockLevel, CloudTimeout' on endpoints; verify CloudBlockLevel is not 0 and CloudTimeout is set appropriately. 2. Verify ASR rule deployment: In Microsoft Intune, navigate to Endpoint Security > Attack Surface Reduction, select the policy containing rule 5beb7efe-fd9a-4556-801d-275e5ffc04cc, and confirm the rule is set to 'Block' or 'Audit' as intended. 3. Check rule status on a test device: Run 'Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids' and confirm the GUID appears; also run 'Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions' to verify the action. 4. Validate blocking behavior: Execute a test obfuscated PowerShell script (e.g., using Invoke-Expression with encoded command) and confirm it is blocked; check Microsoft 365 Defender > Advanced Hunting for AsrObfuscatedScriptBlocked events within the last 24 hours.

## Rollback
1. Disable cloud-delivered protection temporarily: On affected endpoints, run 'Set-MpPreference -CloudBlockLevel 0' to disable cloud blocking; re-enable later with 'Set-MpPreference -CloudBlockLevel 2' (default). 2. Remove or change ASR rule action: In Intune, edit the ASR policy, set rule 5beb7efe-fd9a-4556-801d-275e5ffc04cc to 'Audit' or 'Disabled', then sync devices. 3. For immediate rollback on a single device: Run 'Add-MpPreference -AttackSurfaceReductionRules_Ids 5beb7efe-fd9a-4556-801d-275e5ffc04cc -AttackSurfaceReductionRules_Actions 1' (1 = Audit) or 'Remove-MpPreference -AttackSurfaceReductionRules_Ids 5beb7efe-fd9a-4556-801d-275e5ffc04cc' to remove the rule. 4. Monitor for AsrObfuscatedScriptAudited events in Advanced Hunting to confirm the rule is no longer blocking.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
