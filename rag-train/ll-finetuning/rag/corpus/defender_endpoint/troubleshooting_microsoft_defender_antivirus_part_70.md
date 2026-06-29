# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve internal error codes in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Internal error codes appear during testing of Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Update definitions
2. Force a rescan directly on the endpoint

## Validation
1. Run 'Get-MpComputerStatus' in PowerShell and verify that 'AntivirusEnabled' is True and 'AMProductVersion' is the latest version. 2. Check the 'AntivirusSignatureVersion' field to confirm definitions are up to date. 3. Initiate a scan with 'Start-MpScan -ScanType QuickScan' and verify no errors are returned. 4. Review the latest event logs under 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational' for Event ID 1000 (scan started) and Event ID 1001 (scan completed) without error codes.

## Rollback
1. If definition update fails, restore previous definitions by running 'Update-MpSignature -Rollback' in PowerShell. 2. If forced rescan causes performance issues, stop the scan with 'Stop-MpScan' in PowerShell. 3. If the endpoint becomes unresponsive, restart the Microsoft Defender Antivirus service using 'Restart-Service WinDefend' in PowerShell. 4. As a last resort, disable real-time protection temporarily with 'Set-MpPreference -DisableRealtimeMonitoring $true' and re-enable after recovery.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
