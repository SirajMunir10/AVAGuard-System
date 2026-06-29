# Hardening: Endpoint Security â€“ Attack Surface Reduction (Event ID 1121 â€“ Windows Defender ASR rule triggered (documented by Microsoft))

**Domain:** Intune
**Subdomain:** Endpoint Security â€“ Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I harden Intune-managed Windows devices by enabling Attack Surface Reduction (ASR) rules via an Intune endpoint security policy?

## Environment Context
- **Tenant Type:** Production â€“ Microsoft Intune with Windows 10/11 devices
- **Configuration:** No ASR rules currently configured in Endpoint Security > Attack Surface Reduction policies

## Symptoms
- Devices are not protected by common ASR rules such as blocking Office child processes or blocking credential theft from Windows subsystems
- Security dashboard shows low ASR rule coverage
- Event Viewer logs show ASR rule events (e.g., Event ID 1121) are absent or indicate rules are not enabled

## Error Codes
- `Event ID 1121 â€“ Windows Defender ASR rule triggered (documented by Microsoft)`
- `Event ID 5007 â€“ Windows Defender configuration change (documented by Microsoft)`

## Root Causes
1. No Attack Surface Reduction policy has been assigned to the device group
2. ASR rules are set to 'Not configured' or 'Disabled' in the policy
3. Intune policy deployment has not completed or has failed

## Remediation Steps
1. In Microsoft Intune admin center, navigate to Endpoint Security > Attack Surface Reduction > Create Policy
2. Select platform 'Windows 10 and later' and profile 'Attack Surface Reduction Rules'
3. Configure desired ASR rules (e.g., 'Block Office child processes' = 'Block', 'Block credential theft from Windows subsystem' = 'Block')
4. Assign the policy to the appropriate device group (e.g., 'All Windows devices')
5. Wait for policy sync or manually trigger sync from device (Settings > Accounts > Access work or school > Info > Sync)
6. Verify rule activation using Get-MpPreference on the device (PowerShell command documented by Microsoft)

## Validation
On a target device, run PowerShell as Administrator: Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions. Confirm that the configured rule GUIDs appear with action '1' (Block).

## Rollback
In the Intune admin center, edit the Attack Surface Reduction policy and set the rule to 'Not configured' or 'Disabled', then save and reassign. Alternatively, delete the policy assignment.

## References
- Microsoft Learn: 'Attack surface reduction rules' (URL above)
- Microsoft Learn: 'Event IDs for attack surface reduction' â€“ https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-events?view=o365-worldwide
