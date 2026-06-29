# Optimization: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Optimization

## Scenario / Query
A security operations team notices that Attack Surface Reduction (ASR) rules are not generating alerts even though they are enabled. How can the team verify that ASR rules are properly configured and operational in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Attack Surface Reduction rules enabled via Intune or Group Policy

## Symptoms
- No ASR rule alerts appear in Microsoft 365 Defender portal despite rules being enabled
- Event ID 1121 (block) or 1122 (audit) not generated on endpoints

## Error Codes
N/A

## Root Causes
1. ASR rules may be configured in audit mode only, not blocking mode
2. Exclusions may be too broad, preventing rule triggers
3. Group Policy or Intune policy may not have been applied to all devices

## Remediation Steps
1. Verify ASR rule configuration via Microsoft 365 Defender portal: Endpoints > Configuration management > Endpoint security > Attack surface reduction
2. Use the following PowerShell cmdlet on a test device to confirm rule state: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids
3. Ensure rules are set to 'Block' (1) or 'Audit' (2) as needed, and verify no conflicting exclusions
4. Force policy refresh: gpupdate /force (for Group Policy) or sync Intune policy from device management
5. Check Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational for events 1121/1122

## Validation
After remediation, trigger a known ASR rule action (e.g., attempt to run a script from an Office file) and confirm event ID 1121 appears in the Windows Defender Operational log and an alert is generated in the Microsoft 365 Defender portal.

## Rollback
Set ASR rules back to 'Audit' mode (2) or 'Disabled' (0) using the same policy management tool, and remove any test exclusions.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
