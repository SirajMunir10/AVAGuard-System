# Troubleshooting: Microsoft Defender Antivirus (0x80508030)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508030 indicating an offline scan is required in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508030
- Message: ERROR_MP_CALLISTO_REQUIRED ERROR_MP_CALLISTO_REQUIRED

## Error Codes
- `0x80508030`

## Root Causes
1. This error indicates that an offline scan is required.

## Remediation Steps
1. Run offline Microsoft Defender Antivirus.

## Validation
1. Open Windows Security app (Windows Security).
2. Go to Virus & threat protection > Scan options.
3. Select 'Microsoft Defender Antivirus (Offline scan)' and click 'Scan now'.
4. After the system restarts and completes the offline scan, verify that the error code 0x80508030 no longer appears in the Windows Security app or in Event Viewer under 'Microsoft-Windows-Windows Defender/Operational'.
5. Run a quick scan and confirm it completes without errors.

## Rollback
1. If the offline scan fails to start or causes boot issues, restart the device normally.
2. Open an elevated PowerShell prompt and run: Set-MpPreference -DisableRealtimeMonitoring $true (temporarily disable real-time monitoring).
3. Run a manual quick scan using: Start-MpScan -ScanType QuickScan.
4. If the error persists, re-enable real-time monitoring: Set-MpPreference -DisableRealtimeMonitoring $false.
5. If the system is unbootable, boot into Safe Mode with Networking and run: Start-MpScan -ScanType FullScan.
6. As a last resort, reset Microsoft Defender Antivirus settings via PowerShell: Set-MpPreference -Force.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
