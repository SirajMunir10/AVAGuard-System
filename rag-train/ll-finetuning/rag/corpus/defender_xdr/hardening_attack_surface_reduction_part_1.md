# Hardening: Attack Surface Reduction

**Domain:** Defender XDR
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How can I verify and enforce that Attack Surface Reduction (ASR) rules are enabled and blocking high-severity behaviors in Microsoft Defender for Endpoint, and what specific ASR rule GUIDs should be configured to block Office communication apps from creating child processes and block executable content from email and webmail clients?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** ASR rules are managed via Intune or Group Policy; default audit mode may be set instead of block mode

## Symptoms
- Security operations center (SOC) analysts observe that suspicious child processes originating from Office communication applications (e.g., Outlook, Teams) are not being blocked
- Executable content such as .exe or .js files embedded in email or webmail clients are being allowed to run without ASR intervention
- ASR rules are deployed but appear to be in audit-only mode, generating events but not blocking threats

## Error Codes
N/A

## Root Causes
1. ASR rules are configured in audit mode rather than block mode
2. Specific rule GUIDs for blocking Office communication apps from creating child processes and blocking executable content from email and webmail clients are not enabled
3. ASR rules may be overridden by exclusion policies or not applied to all devices in the tenant

## Remediation Steps
1. Use Microsoft Endpoint Manager (Intune) to create a device configuration profile for ASR rules, setting the following two rules to 'Block' (1):
  - Block Office communication application from creating child processes (GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869)
  - Block executable content from email client and webmail (GUID: be9ba2d9-53ea-4cdc-84e5-9b1eeee46550)
  For each rule, set the value to '1' (block) or '6' (warn) as appropriate.
2. Alternatively, use Group Policy: navigate to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction, configure the desired rules, and set the action to 'Block'.
3. Verify ASR rule status by running the following PowerShell cmdlet on a test device as documented by Microsoft: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Ensure the GUIDs above appear and their corresponding actions are set to 1 (block).
4. Monitor ASR events in Microsoft 365 Defender portal under 'Incidents & alerts' or via advanced hunting using the DeviceEvents table with ActionType = 'Asr*'.

## Validation
Run the following PowerShell command on a representative device: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Confirm that the GUIDs 26190899-1602-49e8-8b27-eb1d0a1ce869 and be9ba2d9-53ea-4cdc-84e5-9b1eeee46550 are present and that their corresponding AttackSurfaceReductionRules_Actions values are 1 (block). Additionally, in Microsoft 365 Defender, use advanced hunting to query DeviceEvents | where ActionType startswith 'Asr' and confirm that events show 'Blocked' rather than 'Audited'.

## Rollback
Set the ASR rule action to 0 (disable) or 2 (audit) via Intune or Group Policy. Remove the rule GUIDs from the ASR rules list if they were added. Re-run Get-MpPreference to confirm the change.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-attack-surface-reduction?view=o365-worldwide>
