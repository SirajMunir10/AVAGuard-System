# Hardening: Endpoint Security â€“ Attack Surface Reduction (Event ID 1121 â€“ Microsoft-Windows-Windows Defender/Operational (ASR rule block))

**Domain:** Intune
**Subdomain:** Endpoint Security â€“ Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I verify and enforce Attack Surface Reduction (ASR) rules via Intune to block common malware entry points, and what should I do if an ASR rule is not applying to a device?

## Environment Context
- **Tenant Type:** Microsoft Intune-managed enterprise with Windows 10/11 devices
- **Configuration:** Endpoint Security > Attack Surface Reduction policy assigned to a device group

## Symptoms
- ASR rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25) is not active on a targeted device
- Device reports ASR rule status as 'Not configured' or 'Not enforced' in Microsoft Defender for Endpoint
- Event ID 1121 or 1122 (ASR rule audit/block) is missing for the expected rule

## Error Codes
- `Event ID 1121 â€“ Microsoft-Windows-Windows Defender/Operational (ASR rule block)`
- `Event ID 1122 â€“ Microsoft-Windows-Windows Defender/Operational (ASR rule audit)`

## Root Causes
1. ASR policy not assigned to the correct Azure AD group
2. Device not checked in or synced with Intune
3. Conflicting ASR rules from multiple policies (e.g., built-in vs. custom)
4. Windows Defender Antivirus not in active mode (e.g., in passive mode due to third-party AV)

## Remediation Steps
1. 1. In Microsoft Intune admin center, go to Endpoint Security > Attack Surface Reduction and confirm the policy is assigned to the device's group.
2. 2. On the affected device, open Settings > Accounts > Access work or school and click 'Sync' to force an Intune policy refresh.
3. 3. Verify Windows Defender Antivirus is active: run `Get-MpComputerStatus` in PowerShell and confirm `AMRunningMode` is 'Normal' (not 'Passive').
4. 4. Remove any conflicting ASR policies by reviewing all assigned policies and ensuring only one ASR policy applies per device.
5. 5. Reboot the device and re-check ASR rule status via Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.

## Validation
On the device, confirm the ASR rule GUID appears in `Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids` and that its action is set to '1' (block) or '2' (audit). Also verify Event ID 1121 appears when the rule triggers.

## Rollback
In Intune, change the ASR rule action from 'Block' to 'Audit' or 'Disabled' in the policy, then sync the device. Alternatively, remove the device from the assigned group.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-asr-policy>
