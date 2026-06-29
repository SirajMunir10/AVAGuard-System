# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block process creations originating from PSExec and WMI commands using ASR rules?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable ASR rule with GUID d1e49aac-8f56-4280-b9ba-993a6d77406c via Intune or Configuration Manager.
2. Use Microsoft Intune name: Block process creations originating from PSExec and WMI commands.
3. Note: This rule has limited exclusion support.

## Validation
1. Confirm the ASR rule GUID d1e49aac-8f56-4280-b9ba-993a6d77406c is enabled by running the following PowerShell command on a managed device: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Verify the GUID appears in the list. 2. Check the rule state by running: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions. Ensure the corresponding action is 'Enabled' or '1'. 3. In Microsoft 365 Defender portal, navigate to Endpoints > Configuration management > Endpoint security > Attack surface reduction and confirm the rule 'Block process creations originating from PSExec and WMI commands' is listed with status 'Enabled' for the target device groups. 4. Test the rule by attempting to execute PSExec or WMI commands from a non-admin context; the action should be blocked and an event with ID 1121 should appear in Microsoft Defender Antivirus operational logs.

## Rollback
1. Disable the ASR rule by setting its state to 'Disabled' (0) via Intune: In the Attack surface reduction policy, set the rule 'Block process creations originating from PSExec and WMI commands' to 'Not configured' or 'Disabled'. 2. Alternatively, use PowerShell on a managed device: Set-MpPreference -AttackSurfaceReductionRules_Ids d1e49aac-8f56-4280-b9ba-993a6d77406c -AttackSurfaceReductionRules_Actions Disabled. 3. Verify the rule is disabled by running: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids and confirm the GUID is no longer present or its action is 'Disabled'. 4. If the rule was deployed via Configuration Manager, remove it from the applicable policy or set the rule to 'Not configured' and redeploy the policy to affected devices.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
