# Hardening: Endpoint Security â€“ Attack Surface Reduction (Event ID 1121 â€“ Windows Defender ASR rule blocked an operation (documented by Microsoft))

**Domain:** Intune
**Subdomain:** Endpoint Security â€“ Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I harden Intune-managed Windows devices by enabling Attack Surface Reduction (ASR) rules via a policy, and what are the documented steps to verify and roll back the configuration?

## Environment Context
- **Tenant Type:** Production â€“ Microsoft Intune (Endpoint Manager)
- **Configuration:** Devices are enrolled in Intune and targeted by an endpoint security policy for Attack Surface Reduction rules.

## Symptoms
- Security team identifies that ASR rules are not enforced on managed Windows devices
- Event Viewer shows Event ID 1121 (ASR rule blocked) is absent, indicating rules are not active
- Intune reports 'Not applicable' or 'Pending' for ASR rule assignments

## Error Codes
- `Event ID 1121 â€“ Windows Defender ASR rule blocked an operation (documented by Microsoft)`
- `Event ID 5007 â€“ Windows Defender configuration change (documented by Microsoft)`

## Root Causes
1. No ASR policy assigned to the device or user group
2. ASR policy is configured with 'Audit' mode instead of 'Block' mode
3. Conflicting policies (e.g., from Microsoft Defender for Endpoint) override Intune settings

## Remediation Steps
1. 1. Sign in to Microsoft Intune admin center (https://intune.microsoft.com) and navigate to 'Endpoint security' > 'Attack surface reduction'.
2. 2. Click 'Create policy' and select platform 'Windows 10 and later' with profile 'Attack Surface Reduction Rules'.
3. 3. Configure each ASR rule to 'Block' (or 'Audit' for testing) as documented in 'Attack surface reduction rules reference'.
4. 4. Assign the policy to the appropriate Azure AD group containing the target devices.
5. 5. Monitor deployment status in 'Endpoint security' > 'Attack surface reduction' > select the policy > 'Device status'.
6. 6. Verify enforcement by checking Event ID 1121 on a client device (see 'Review attack surface reduction events').

## Validation
On a targeted Windows device, open Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. Confirm Event ID 1121 appears with rule GUID and 'Blocked' action. Alternatively, run Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions in PowerShell as Administrator.

## Rollback
To roll back, either delete the ASR policy assignment from the group, or change the policy rules to 'Not configured' and save. Devices will revert to default behavior (no ASR enforcement) after the next policy sync (typically within 60 minutes or manually triggered via Settings > Accounts > Access work or school > Sync).

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/event-views>
