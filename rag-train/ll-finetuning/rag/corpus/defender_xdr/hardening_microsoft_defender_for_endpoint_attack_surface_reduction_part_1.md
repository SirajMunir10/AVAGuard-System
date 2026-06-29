# Hardening: Microsoft Defender for Endpoint â€“ Attack Surface Reduction

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint â€“ Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How can I verify and enforce that all devices in my tenant have Attack Surface Reduction (ASR) rules enabled and in block mode, and that no ASR rules are set to 'Audit only' or 'Disabled'?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Endpoint Plan 2
- **Configuration:** ASR rules configured via Intune or Group Policy; tenant has at least one ASR rule deployed but not all are in block mode

## Symptoms
- Security portal shows ASR rules in 'Audit' or 'Warn' mode on multiple devices
- Microsoft 365 Defender advanced hunting queries return ASR rule events with ActionType = 'Audited' instead of 'Blocked'
- CIS benchmark compliance check fails for ASR rule controls

## Error Codes
N/A

## Root Causes
1. ASR rules were initially deployed in audit mode for testing and never switched to block mode
2. Incomplete or conflicting policy assignments (e.g., Intune profile vs. local GPO) leave some rules in non-blocking state
3. Administrators may not be aware that ASR rules must be explicitly set to 'Block' to provide hardening

## Remediation Steps
1. 1. In Microsoft Intune, navigate to Endpoint Security > Attack Surface Reduction and create or edit a policy for ASR rules. For each rule, set the action to 'Block' (not 'Audit' or 'Warn').
2. 2. Alternatively, use Group Policy: Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction. Enable each rule and set the action to '1' (Block).
3. 3. Use Microsoft 365 Defender advanced hunting to identify devices with ASR rules in non-blocking mode. Example query: DeviceEvents | where ActionType startswith 'Asr' | where ActionType endswith 'Audited' | summarize by DeviceName.
4. 4. After updating policy, allow up to 8 hours for policy refresh; then re-run the advanced hunting query to confirm all events show ActionType = 'Blocked'.

## Validation
Run the following advanced hunting query in Microsoft 365 Defender: DeviceEvents | where ActionType startswith 'Asr' | summarize BlockCount = countif(ActionType endswith 'Blocked'), AuditCount = countif(ActionType endswith 'Audited') by DeviceName. Verify that AuditCount is 0 for all devices.

## Rollback
To revert a rule to audit mode, change the rule action back to 'Audit' in the Intune policy or set the corresponding GPO value to '2' (Audit).

## References
- CIS Microsoft 365 Foundations Benchmark v2.0.0 â€“ Control 8.1: 'Ensure Attack Surface Reduction (ASR) rules are set to Block'
