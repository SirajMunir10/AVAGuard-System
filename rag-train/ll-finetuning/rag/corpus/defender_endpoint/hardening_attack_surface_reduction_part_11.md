# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block executable content from email client and webmail using ASR rule be9ba2d9-53ea-4cdc-84e5-9b1eeee46550?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Cloud protection level must be High plus or Zero tolerance for EDR alerts; High, High plus, or Zero tolerance for user notification pop-ups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable ASR rule with GUID be9ba2d9-53ea-4cdc-84e5-9b1eeee46550 in Block or Warn mode
2. Ensure Microsoft Defender Antivirus is the active antimalware solution
3. Set cloud protection level to High plus or Zero tolerance for EDR alerts, or High/High plus/Zero tolerance for user notification pop-ups

## Validation
1. Confirm ASR rule is enabled: Run 'Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids' and verify GUID be9ba2d9-53ea-4cdc-84e5-9b1eeee46550 is listed. Then run 'Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions' to confirm the corresponding action is 1 (Block) or 2 (Audit/Warn).
2. Verify Microsoft Defender Antivirus is active: Run 'Get-MpComputerStatus | Select-Object AMRunningMode' and confirm value is 'Normal' or 'Passive' (if in a managed environment).
3. Check cloud protection level: Run 'Get-MpPreference | Select-Object CloudBlockLevel' and confirm value is '6' (High plus) or '0' (Zero tolerance) for EDR alerts; or '4' (High), '6' (High plus), or '0' (Zero tolerance) for user notification pop-ups.
4. Test rule effectiveness: Attempt to open an executable file (e.g., .exe) from a simulated email client or webmail and verify it is blocked or warned as per the configured mode.

## Rollback
1. Disable the ASR rule: Run 'Set-MpPreference -AttackSurfaceReductionRules_Ids be9ba2d9-53ea-4cdc-84e5-9b1eeee46550 -AttackSurfaceReductionRules_Actions 0' to set the rule to Disabled.
2. If Microsoft Defender Antivirus was not the active solution, re-enable the previous antimalware solution and disable Defender Antivirus as needed.
3. Restore previous cloud protection level: Run 'Set-MpPreference -CloudBlockLevel <previous_value>' where <previous_value> is the original setting (e.g., 2 for Moderate, 4 for High, etc.).
4. Verify rollback: Repeat validation steps to confirm the rule is disabled and cloud protection level is restored.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
