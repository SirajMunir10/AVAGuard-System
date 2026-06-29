# Troubleshooting: Microsoft Defender Antivirus (0x80508012)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508012 with message ERR_MP_BAD_SCANID in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508012 displayed
- Message displayed: ERR_MP_BAD_SCANID

## Error Codes
- `0x80508012`
- `ERR_MP_BAD_SCANID`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
Run the following PowerShell command as Administrator to verify Microsoft Defender Antivirus is functioning: Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled. Then initiate a quick scan: Start-MpScan -ScanType QuickScan. Check for any error output. Finally, review the latest event logs: Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; ID=1001} | Select-Object -First 1 TimeCreated, Message.

## Rollback
If the remediation fails or causes issues, restore the default Microsoft Defender Antivirus configuration by running: Set-MpPreference -DisableRealtimeMonitoring $false; Set-MpPreference -DisableBehaviorMonitoring $false; Set-MpPreference -DisableBlockAtFirstSeen $false. Then restart the service: Restart-Service WinDefend. Finally, re-run the validation steps to confirm the system returns to its previous state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
