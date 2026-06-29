# Hardening: Endpoint Security - Attack Surface Reduction (Event ID 1121 (Windows Defender ASR audit event))

**Domain:** Intune
**Subdomain:** Endpoint Security - Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I verify and remediate Intune-managed Windows devices that are missing the CIS Benchmark control 18.9.10.1.1 (Block Office communication applications from creating child processes) Attack Surface Reduction rule?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Intune Endpoint Security > Attack Surface Reduction policy with ASR rule GUID '26190899-1602-49e8-8b27-eb1d0a1ce869' set to 'Block' mode

## Symptoms
- Security Operations reports that Office applications (Word, Excel, PowerPoint) are spawning child processes like cmd.exe or powershell.exe on managed devices
- Intune reports show devices in 'Not compliant' status for the ASR rule 'Block Office communication applications from creating child processes'
- Event ID 1121 is logged in Microsoft-Windows-Windows Defender/Operational with RuleId 26190899-1602-49e8-8b27-eb1d0a1ce869 and Action 'Audit' instead of 'Block'

## Error Codes
- `Event ID 1121 (Windows Defender ASR audit event)`
- `Event ID 5007 (Windows Defender configuration change event)`

## Root Causes
1. Attack Surface Reduction rule 'Block Office communication applications from creating child processes' is not enabled in Intune Endpoint Security policy
2. Devices are targeted by a conflicting policy that sets the rule to 'Audit' mode instead of 'Block' mode
3. The ASR rule GUID 26190899-1602-49e8-8b27-eb1d0a1ce869 is missing from the assigned Intune ASR policy

## Remediation Steps
1. In Microsoft Intune admin center, navigate to Endpoint Security > Attack Surface Reduction
2. Create or edit a policy with platform 'Windows 10 and later' and profile 'Attack Surface Reduction Rules'
3. Set the rule 'Block Office communication applications from creating child processes' to 'Block' (GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869)
4. Assign the policy to the affected device groups and save
5. On each device, verify the rule is active by running the PowerShell command: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids (documented in Microsoft Defender for Endpoint ASR reference)
6. If the rule ID is not present, force a sync from Intune by going to Settings > Accounts > Access work or school > Info > Sync

## Validation
On a test device, run the PowerShell command: Get-MpPreference | Where-Object {$_.AttackSurfaceReductionRules_Ids -contains '26190899-1602-49e8-8b27-eb1d0a1ce869'} | Select-Object AttackSurfaceReductionRules_Actions. Confirm the action is '1' (Block). Also verify Event ID 1121 shows Action 'Block' when an Office app attempts to create a child process.

## Rollback
Set the rule to 'Audit' mode (action value 2) in the Intune ASR policy, or remove the rule from the policy entirely. Reassign the policy to the affected groups.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-asr-policy>
- CIS Microsoft Windows 10 Enterprise Benchmark v2.0.0, Section 18.9.10.1.1
