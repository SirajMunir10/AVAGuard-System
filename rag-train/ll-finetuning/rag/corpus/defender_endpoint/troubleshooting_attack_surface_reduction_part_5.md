# Troubleshooting: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Troubleshooting

## Scenario / Query
Why does the ASR rule 'Block Office communication application from creating child processes' block processes created through PsExec and WMI, and how to handle this in Microsoft Configuration Manager?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Configuration Manager name: n/a

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. This ASR rule blocks processes created through PsExec and WMI from running.
2. PsExec and WMI can remotely execute code; malware can use them for command and control or to spread network infections.

## Remediation Steps
1. If you use Microsoft Configuration Manager, do not use other available deployment methods to enable this rule on managed devices.
2. The Configuration Manager client relies heavily on WMI, and this rule blocks WMI-based processes.

## Validation
1. Confirm the ASR rule 'Block Office communication application from creating child processes' is enabled by running: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. 2. Verify that the rule GUID (e.g., 26190899-1602-49e8-8b27-eb1d0a1ce869) is present and its state is 1 (enabled). 3. Test that WMI-based processes are blocked by attempting to execute a remote WMI command (e.g., wmic /node:localhost process call create 'calc.exe') and confirm it fails. 4. Check Microsoft Configuration Manager client functionality by running a policy evaluation cycle (e.g., from Configuration Manager console or via wbemtest) and ensure it completes without error.

## Rollback
1. Disable the ASR rule by running: Set-MpPreference -AttackSurfaceReductionRules_Ids 26190899-1602-49e8-8b27-eb1d0a1ce869 -AttackSurfaceReductionRules_Actions Disabled. 2. If the rule was deployed via Group Policy, remove the rule from the ASR policy or set its state to 'Disabled'. 3. If using Microsoft Configuration Manager, remove the rule from the ASR policy in the Endpoint Protection node and redeploy the updated policy. 4. Restart the Configuration Manager client service (SMS Agent Host) to ensure changes take effect: Restart-Service CcmExec.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
