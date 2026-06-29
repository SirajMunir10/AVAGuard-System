# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block JavaScript or VBScript from launching downloaded executable content using ASR rule d3e037e1-3eb8-44c8-a917-57927947596d?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Not supported via Intune to Windows Server 2012 R2 or Windows Server 2016 using modern unified solution; Block/Warn mode requires cloud protection level High plus or Zero tolerance for EDR alerts, High/High plus/Zero tolerance for user notifications

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure Microsoft Defender Antivirus and AMSI are active
2. Set cloud protection level to High plus or Zero tolerance for EDR alerts, or High/High plus/Zero tolerance for user notifications
3. Deploy ASR rule with GUID d3e037e1-3eb8-44c8-a917-57927947596d via Intune or Configuration Manager
4. Monitor advanced hunting action types: AsrScriptExecutableDownloadAudited, AsrScriptExecutableDownloadBlocked

## Validation
1. Verify Microsoft Defender Antivirus is active: Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled
2. Confirm AMSI is enabled: Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\AMSI' -Name 'Enable' (value should be 1)
3. Check cloud protection level: Get-MpPreference | Select-Object CloudBlockLevel, CloudTimeout
   - CloudBlockLevel should be 6 (High plus) or 2 (Zero tolerance for EDR alerts) or 4 (High) / 5 (High plus) / 6 (Zero tolerance for user notifications)
4. Validate ASR rule deployment: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids | Where-Object {$_ -eq 'd3e037e1-3eb8-44c8-a917-57927947596d'}
   - Also check rule state: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions
5. Test rule enforcement: Attempt to download and execute a .js or .vbs file from the internet; confirm block event in Windows Event Viewer under Microsoft-Windows-Windows Defender/Operational (Event ID 1121)
6. Query advanced hunting in Microsoft 365 Defender: 
   DeviceEvents | where ActionType in ('AsrScriptExecutableDownloadAudited', 'AsrScriptExecutableDownloadBlocked') | take 10

## Rollback
1. Remove the ASR rule from Intune: Navigate to Endpoint Security > Attack Surface Reduction > select policy containing rule d3e037e1-3eb8-44c8-a917-57927947596d, set action to 'Not configured' or 'Disabled' and save
2. If using Configuration Manager, remove the rule from the ASR policy assigned to the device collection
3. Reset cloud protection level to default: Set-MpPreference -CloudBlockLevel 0 (or previous value)
4. Verify rollback: Get-MpPreference | Select-Object CloudBlockLevel, AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions
5. Confirm no blocking events: Check Event ID 1121 for rule d3e037e1-3eb8-44c8-a917-57927947596d is no longer generated

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
