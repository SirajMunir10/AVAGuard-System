# Troubleshooting: Microsoft Defender Antivirus (3007)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 3007 indicating real-time protection recovered from a failure in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Real-time protection recovered from a failure
- Event ID 3007 with symbolic name MALWAREPROTECTION_RTP_FEATURE_RECOVERED

## Error Codes
- `3007`

## Root Causes
1. Microsoft Defender Antivirus Real-time Protection restarted a feature

## Remediation Steps
1. Run a full system scan to detect any items that might have been missed while this agent was down

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 3007 is no longer appearing after the remediation.
4. Run a full scan: Start-MpScan -ScanType FullScan.
5. Confirm scan completed successfully with no threats found: Get-MpThreatDetection.
6. Check real-time protection status: Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled.

## Rollback
1. If the full scan causes performance issues, stop the scan: Stop-MpScan.
2. If real-time protection fails after remediation, restart the service: Restart-Service WinDefend.
3. If issues persist, reset Defender settings: Set-MpPreference -DisableRealtimeMonitoring $false.
4. Re-run the full scan in safe mode if needed: bcdedit /set {current} safeboot minimal, restart, run scan, then bcdedit /deletevalue {current} safeboot.
5. Review Event ID 3007 details again to confirm recovery.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
