# Implementation: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Implementation

## Scenario / Query
How to configure the ASR rule 'Block Office communication application from creating child processes' to protect against social engineering attacks and Outlook exploits?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869; Advanced hunting action types: AsrOfficeCommAppChildProcessAudited, AsrOfficeCommAppChildProcessBlocked

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable the ASR rule to prevent Outlook from creating child processes while allowing legitimate Outlook functions.
2. This protects against social engineering attacks and prevents exploiting code from abusing vulnerabilities in Outlook.
3. It also protects against Outlook rules and forms exploits that attackers can use when a user's credentials are compromised.

## Validation
1. Confirm the ASR rule is enabled: Run the following PowerShell command as Administrator: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Verify that the GUID '26190899-1602-49e8-8b27-eb1d0a1ce869' appears in the list. 2. Check the rule action: Run: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions. Ensure the corresponding action for the GUID is '1' (Block) or '2' (Audit) as intended. 3. Validate via Advanced Hunting: Run a query in Microsoft 365 Defender Advanced Hunting: DeviceEvents | where ActionType in ('AsrOfficeCommAppChildProcessAudited', 'AsrOfficeCommAppChildProcessBlocked') | where Timestamp > ago(1h). Confirm that events are being generated with the expected action type (Blocked or Audited). 4. Test the rule: Attempt to launch a child process from Outlook (e.g., via a simulated attack or by running a legitimate Outlook function that creates a child process). Verify that the process is blocked (if set to Block) or audited (if set to Audit) and that an alert is generated in Microsoft 365 Defender.

## Rollback
1. Disable the ASR rule: Run the following PowerShell command as Administrator: Remove-MpPreference -AttackSurfaceReductionRules_Ids '26190899-1602-49e8-8b27-eb1d0a1ce869'. 2. Alternatively, set the rule to Audit mode (if Block mode caused issues): Add-MpPreference -AttackSurfaceReductionRules_Ids '26190899-1602-49e8-8b27-eb1d0a1ce869' -AttackSurfaceReductionRules_Actions 2. 3. Verify rollback: Run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids to confirm the GUID is removed or the action is changed. 4. Monitor for any residual blocking: Check Advanced Hunting for any AsrOfficeCommAppChildProcessBlocked events after rollback to ensure no unintended blocks persist.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
