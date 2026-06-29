# Troubleshooting: Microsoft Defender Antivirus (0x80508010)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508010 with message ERR_MP_NO_MORE_ITEMS in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508010 displayed
- Message displayed: ERR_MP_NO_MORE_ITEMS

## Error Codes
- `0x80508010`
- `ERR_MP_NO_MORE_ITEMS`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Look for event ID 1006 or 1007 to confirm no new detections are being blocked. 2. Run 'Get-MpThreatDetection' in PowerShell to verify no active threats are reported. 3. Run 'Start-MpScan -ScanType QuickScan' and confirm the scan completes without error code 0x80508010. 4. Check the Microsoft Defender Antivirus client version with 'Get-MpComputerStatus | Select-Object AMProductVersion' and ensure it is up to date.

## Rollback
1. If the error persists after remediation, restore the default Microsoft Defender Antivirus configuration by running 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Set-MpPreference -DisableBehaviorMonitoring $false'. 2. Reset the Microsoft Defender Antivirus engine by running 'MpCmdRun -RemoveDefinitions -All' followed by 'MpCmdRun -SignatureUpdate'. 3. If the issue continues, re-register the Microsoft Defender Antivirus service by running 'Uninstall-WindowsFeature -Name Windows-Defender' and then 'Install-WindowsFeature -Name Windows-Defender' in an elevated PowerShell session. 4. As a last resort, perform a system restore to a point before the error first appeared.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
