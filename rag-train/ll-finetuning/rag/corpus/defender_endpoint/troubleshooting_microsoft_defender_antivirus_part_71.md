# Troubleshooting: Microsoft Defender Antivirus (0x80501004)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501004 (ERROR_MP_NO_INTERNET_CONN) when running a Microsoft Defender Antivirus scan?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501004 displayed
- Message displayed: ERROR_MP_NO_INTERNET_CONN

## Error Codes
- `0x80501004`
- `ERROR_MP_NO_INTERNET_CONN`

## Root Causes
1. No Internet connection

## Remediation Steps
1. Check your Internet connection, then run the scan again.

## Validation
1. Open Command Prompt as Administrator and run: ping 8.8.8.8 -n 1. If successful, Internet connectivity is confirmed.
2. Run: powershell -Command "Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled, AntivirusEnabled". Verify AMRunningMode is 'Normal' and both services are True.
3. Initiate a quick scan: Start-MpScan -ScanType QuickScan. Check for error code 0x80501004 in the output or Event Viewer under Microsoft-Windows-Windows Defender/Operational.

## Rollback
1. If validation fails, restore previous network settings: netsh int ip reset, then netsh winsock reset. Reboot.
2. If the scan still fails, re-register Defender: "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24080.9-0\MpCmdRun.exe" -RemoveDefinitions -All, then run "MpCmdRun.exe" -SignatureUpdate.
3. As a last resort, run: Dism /Online /Cleanup-Image /RestoreHealth and sfc /scannow to repair system files.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
