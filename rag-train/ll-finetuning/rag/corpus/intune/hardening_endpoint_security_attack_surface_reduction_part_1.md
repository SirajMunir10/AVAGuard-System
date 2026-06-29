# Hardening: Endpoint Security â€“ Attack Surface Reduction

**Domain:** Intune
**Subdomain:** Endpoint Security â€“ Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I configure and verify that Attack Surface Reduction (ASR) rules are enabled and enforced for all Windows 10/11 devices managed by Intune, and what are the documented steps to block common malware behaviors using ASR rules?

## Environment Context
- **Tenant Type:** Microsoft Intune standalone (no Configuration Manager co-management)
- **Configuration:** Endpoint Security > Attack Surface Reduction policy targeting Windows 10/11 devices

## Symptoms
- Devices are not blocking common malware behaviors such as Office macro execution or script downloads
- Security administrators cannot confirm which ASR rules are active across the device fleet
- Event Viewer shows Event ID 1121 for blocked actions but no corresponding policy enforcement in Intune reports

## Error Codes
N/A

## Root Causes
1. ASR rules are not configured in an Intune Endpoint Security policy
2. The policy is assigned to the wrong Azure AD group or not assigned at all
3. Devices are not receiving the policy due to network or enrollment issues

## Remediation Steps
1. 1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. 2. Navigate to Endpoint Security > Attack Surface Reduction.
3. 3. Click 'Create Policy' and select platform 'Windows 10 and later' with profile 'Attack Surface Reduction Rules'.
4. 4. Configure each ASR rule to 'Block' or 'Audit' as needed. For example, set 'Block Office communication application from creating child processes' to 'Block'.
5. 5. Assign the policy to the appropriate Azure AD group containing target devices.
6. 6. On a target device, verify enforcement by opening Windows Security > App & browser control > Exploit protection settings, or by checking Event ID 1121 in Event Viewer under Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
7. 7. Use the Intune reports (Endpoint Security > Antivirus > Windows Defender AV status) to confirm policy delivery.

## Validation
On a managed device, run the PowerShell cmdlet Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids to list all configured ASR rule GUIDs and their states. Compare against the policy settings in Intune. Also confirm that Event ID 1121 appears for blocked actions when a known test file (e.g., a macro-enabled Office document) is executed.

## Rollback
In the Intune admin center, navigate to Endpoint Security > Attack Surface Reduction, select the policy, and change the assignment to 'Not assigned' or delete the policy. Alternatively, set each ASR rule to 'Not configured' or 'Audit only' to stop blocking without removing the policy.

## References
- Microsoft Learn: 'Attack surface reduction rules reference' â€“ https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide
