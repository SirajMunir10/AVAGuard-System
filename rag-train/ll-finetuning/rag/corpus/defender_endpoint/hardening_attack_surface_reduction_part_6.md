# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block abuse of exploited vulnerable signed drivers using ASR rule?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** ASR rule GUID: 56a863a9-875e-4185-98a7-b882c64b5ce5

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. Local apps with sufficient privileges can exploit vulnerable signed drivers to gain access to the operating system kernel.
2. Vulnerable signed drivers enable attackers to disable or circumvent security solutions.

## Remediation Steps
1. Enable the ASR rule 'Block abuse of exploited vulnerable signed drivers' (GUID: 56a863a9-875e-4185-98a7-b882c64b5ce5) via Microsoft Intune or Configuration Manager.
2. Use the following URL to submit a driver to Microsoft for analysis: https://www.microsoft.com/wdsi/driversubmission.
3. Implement additional protection methods: Microsoft App Control for Business (Windows 10 or later, Windows Server 2016 or later), Microsoft Windows vulnerable driver block list (Windows 11 or later, Windows Server 2019 (1809) or later), or Microsoft AppLocker (Windows 8.1 or older, Windows Server 2012 R2 or older).

## Validation
1. Verify the ASR rule is enabled: In Microsoft 365 Defender portal, go to Endpoints > Configuration management > Endpoint security policies > Attack surface reduction. Confirm the rule 'Block abuse of exploited vulnerable signed drivers' (GUID: 56a863a9-875e-4185-98a7-b882c64b5ce5) is set to 'Block' or 'Audit' as intended. 2. On a test device, run PowerShell as administrator: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Confirm the GUID appears in the list. 3. Check event logs: On a test device, open Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. Look for event ID 1121 (blocked) or 5007 (configuration change) related to the ASR rule GUID.

## Rollback
1. In Microsoft 365 Defender portal, navigate to Endpoints > Configuration management > Endpoint security policies > Attack surface reduction. Locate the policy containing the rule 'Block abuse of exploited vulnerable signed drivers' (GUID: 56a863a9-875e-4185-98a7-b882c64b5ce5). Change its action to 'Disabled' or remove the rule from the policy. 2. Alternatively, on a device, run PowerShell as administrator: Set-MpPreference -AttackSurfaceReductionRules_Ids 56a863a9-875e-4185-98a7-b882c64b5ce5 -AttackSurfaceReductionRules_Actions Disabled. 3. If the rule was enabled via Group Policy, edit the corresponding GPO to set the rule to 'Disabled' or 'Not configured' and force a gpupdate.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
