# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block untrusted and unsigned processes that run from USB using ASR rules?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable ASR rule with GUID b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4 via Intune or Configuration Manager.
2. Use Microsoft Intune name: Block untrusted and unsigned processes that run from USB.
3. Note: This rule blocks execution from USB removable drives (including SD cards) but does not block copying files from USB to disk.

## Validation
1. Confirm the ASR rule is enabled: Run PowerShell as Administrator and execute: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Verify that the GUID 'b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4' appears in the list. 2. Check the rule action: Run: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions. Ensure the corresponding action for the GUID is '1' (Enabled) or '2' (Audit). 3. Test the rule: Insert a USB drive containing an unsigned executable. Attempt to run the executable. Confirm that execution is blocked and an event (e.g., Event ID 1121) is logged in Windows Event Viewer under Microsoft-Windows-Windows Defender/Operational.

## Rollback
1. Disable the ASR rule: Run PowerShell as Administrator and execute: Set-MpPreference -AttackSurfaceReductionRules_Ids 'b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4' -AttackSurfaceReductionRules_Actions 0. 2. If configured via Intune, navigate to Endpoint Security > Attack Surface Reduction, locate the rule 'Block untrusted and unsigned processes that run from USB', and set it to 'Not configured' or 'Disabled'. 3. If configured via Configuration Manager, remove the rule from the ASR policy assigned to the affected devices. 4. Verify removal: Run Get-MpPreference and confirm the GUID is no longer present in AttackSurfaceReductionRules_Ids, or its action is set to 0.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
