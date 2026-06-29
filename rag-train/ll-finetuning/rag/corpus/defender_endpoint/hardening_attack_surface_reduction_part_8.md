# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block persistence through WMI event subscription using ASR rule GUID e6db77e5-3df2-4cf1-b95a-636979351e5b?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus, RPC dependency

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable ASR rule 'Block persistence through WMI event subscription' with GUID e6db77e5-3df2-4cf1-b95a-636979351e5b in Audit mode before proceeding to Block mode when using Microsoft Configuration Manager.
2. Test extensively in Audit mode before enabling Block mode if using Microsoft Configuration Manager.
3. Use limited exclusion support as described in File and folder exclusions for ASR rules.

## Validation
1. Confirm the ASR rule is enabled in Block mode by running the following PowerShell command as Administrator: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Verify that the GUID 'e6db77e5-3df2-4cf1-b95a-636979351e5b' appears in the list. 2. Check the corresponding action by running: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions. Ensure the action for that GUID is set to '1' (Block). 3. Review the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for event ID 1121, which indicates the rule blocked a WMI persistence attempt. 4. If using Microsoft Configuration Manager, verify the rule deployment status in the console under 'Endpoint Protection' > 'Attack Surface Reduction Policies' and confirm the rule is enabled with action 'Block'.

## Rollback
1. Set the ASR rule to Audit mode by running the following PowerShell command as Administrator: Set-MpPreference -AttackSurfaceReductionRules_Ids e6db77e5-3df2-4cf1-b95a-636979351e5b -AttackSurfaceReductionRules_Actions 2. 2. If the rule was deployed via Microsoft Configuration Manager, update the policy to set the rule action to 'Audit' and redeploy to affected devices. 3. Remove any file or folder exclusions that were added specifically for this rule by running: Remove-MpPreference -ExclusionPath '<path>'. 4. Monitor event ID 1121 (Block) and 1120 (Audit) in the Microsoft Defender Antivirus operational log to confirm the rule is no longer blocking.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
