# Governance: Device Configuration â€“ Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Device Configuration â€“ Attack Surface Reduction
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that Attack Surface Reduction (ASR) rules are not being enforced on a subset of Windows 10 devices that are onboarded to Microsoft Defender for Endpoint. The devices show as 'Active' in the device inventory but the ASR rule status remains 'Not configured' in the Microsoft 365 Defender portal. What configuration or policy gap is causing this behavior, and how should it be corrected?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Devices are managed by Microsoft Intune and have the Windows 10 Security Baseline applied. ASR rules are configured via an Intune device configuration profile targeting 'All Devices'.

## Symptoms
- ASR rules show 'Not configured' on some devices in the Microsoft 365 Defender portal under Endpoints > Configuration management > Attack surface reduction rules.
- Affected devices are listed as 'Active' in the device inventory and report sensor health as 'Active'.
- No ASR rule events are generated from the affected devices in the Advanced Hunting ASR table.

## Error Codes
N/A

## Root Causes
1. The Intune device configuration profile for ASR rules is not applied to the affected devices because they are not in the assigned group, or the profile has a filter that excludes them.
2. The devices may be running a Windows edition or build that does not support the specific ASR rules configured (e.g., Windows 10 Pro without the required licensing).
3. A conflicting Group Policy Object (GPO) is overriding the Intune ASR policy, setting the rules to 'Disabled' or 'Not configured'.

## Remediation Steps
1. Verify that the affected devices are members of the Azure AD group targeted by the ASR rule policy in Intune. Use the Intune console to check group membership and policy assignment.
2. Ensure the devices meet the minimum Windows version requirement: Windows 10 version 1709 (RS3) or later, and are licensed for Defender for Endpoint (Windows 10 Enterprise E5 or equivalent).
3. Check for conflicting GPOs by running the following PowerShell command on an affected device as documented by Microsoft: Get-MpPreference. Look for the AttackSurfaceReductionRules property. If the rules are set to '0' (disabled) or are absent, a GPO may be overriding the Intune policy.
4. If a GPO conflict is found, remove the conflicting ASR rule settings from the GPO or set the GPO to 'Not configured' to allow Intune to manage the rules.
5. After resolving the conflict, trigger a policy sync on the affected devices from Intune or wait for the next scheduled sync (every 90 minutes by default).

## Validation
After remediation, verify in the Microsoft 365 Defender portal that the affected devices now show the ASR rules as 'Enabled' or 'Audit only' as configured. Additionally, run the following command on a remediated device to confirm the local policy: Get-MpPreference | Select-Object AttackSurfaceReductionRules. The output should list the rule GUIDs with the expected action (1=Block, 2=Audit).

## Rollback
If the remediation causes unintended behavior, reapply the original GPO that was removed, or remove the affected devices from the Intune ASR policy assignment. The devices will revert to the previous configuration within one policy sync cycle.

## References
- Microsoft Learn, 'Manage attack surface reduction rules with Microsoft Intune' â€“ https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/manage-asr-rules?view=o365-worldwide
- Microsoft Learn, 'Troubleshoot attack surface reduction rules' â€“ https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-asr-rules?view=o365-worldwide
