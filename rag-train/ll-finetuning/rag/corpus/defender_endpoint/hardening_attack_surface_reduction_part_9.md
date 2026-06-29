# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block Adobe Reader from creating child processes using ASR rule GUID 7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus with cloud protection level High plus or Zero tolerance for EDR alerts; High, High plus, or Zero tolerance for user notification pop-ups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable ASR rule 'Block Adobe Reader from creating child processes' using GUID 7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c in Microsoft Intune or Microsoft Configuration Manager.
2. Ensure Microsoft Defender Antivirus is active and cloud protection level is set to High plus or Zero tolerance for EDR alerts, or High, High plus, or Zero tolerance for user notification pop-ups in Block or Warn mode.
3. Note: This rule has limited exclusion support; refer to File and folder exclusions for ASR rules for details.

## Validation
1. Verify the ASR rule is enabled: Run 'Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids' in PowerShell to confirm GUID 7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c is present. 2. Check the rule action: Run 'Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions' to ensure the corresponding action is 'Enabled' or '1'. 3. Confirm Microsoft Defender Antivirus is active: Run 'Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled' and verify both are 'True'. 4. Validate cloud protection level: Run 'Get-MpPreference | Select-Object CloudBlockLevel' and confirm it is '2' (High plus) or '6' (Zero tolerance). 5. Test the rule: Attempt to launch Adobe Reader and create a child process (e.g., via script or command) and verify the action is blocked or warned as per the configured mode.

## Rollback
1. Disable the ASR rule: Run 'Set-MpPreference -AttackSurfaceReductionRules_Ids 7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c -AttackSurfaceReductionRules_Actions Disabled' in PowerShell. 2. If cloud protection level was changed, revert to previous setting: Run 'Set-MpPreference -CloudBlockLevel <previous_level>' where <previous_level> is the original value (e.g., 0 for Default, 1 for High, 2 for High plus, 6 for Zero tolerance). 3. If Microsoft Defender Antivirus was disabled, re-enable it: Run 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Set-MpPreference -DisableBehaviorMonitoring $false' as needed. 4. For Intune or Configuration Manager deployments, revert the ASR rule policy to its previous state (e.g., set to 'Not configured' or 'Disabled') and sync devices.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
