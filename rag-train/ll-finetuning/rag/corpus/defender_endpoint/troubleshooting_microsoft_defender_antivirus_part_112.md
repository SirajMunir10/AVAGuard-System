# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and reduce high CPU utilization caused by Microsoft Defender Antivirus real-time protection or scheduled scans?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Tamper Protection enabled, scheduled scan settings, CPU priority settings

## Symptoms
- Higher CPU utilization by Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. Real-time protection (RTP) scanning contributing to higher CPU utilization
2. Scheduled scans running with default CPU priority
3. Scans after security intelligence updates

## Remediation Steps
1. Use Troubleshooting mode to turn off Tamper Protection
2. Once Tamper Protection is turned off, turn off Real-time protection temporarily to rule it out
3. Configure low CPU priority for scheduled scans (Use low CPU priority for scheduled scans) - lowers thread priority from 9 to 8
4. Specify the maximum percentage of CPU utilization during a scan (CPU usage limit per scan) - default 50, can lower to 20 or 30
5. Set ScanOnlyIfIdle to Not configured (enabled by default) - requires CPU usage overall below 80%
6. Set Specify the interval to run quick scans per day to Not configured
7. Set Specify the time for a daily quick scan (Run daily quick scan at) to 12 PM
8. Set Specify the scan type to use for a scheduled scan to Not configured
9. Set Day of week to run scheduled scan to Not configured
10. Set Time of day to run a scheduled scan to Not configured
11. In Group Policy or MDM, go to Computer Configuration > Administrative Templates > Microsoft Defender Antivirus > Security Intelligence Updates, and set Turn on scan after security intelligence update to Disabled

## Validation
1. Verify Tamper Protection is off: Get-MpComputerStatus | Select TamperProtection. 2. Confirm real-time protection is off: Get-MpComputerStatus | Select RealTimeProtectionEnabled. 3. Check scheduled scan CPU priority: Get-MpPreference | Select LowCpuPriority. 4. Verify CPU usage limit per scan: Get-MpPreference | Select ScanAvgCPULoadFactor. 5. Confirm ScanOnlyIfIdle is not configured: Get-MpPreference | Select ScanOnlyIfIdle. 6. Check quick scan interval: Get-MpPreference | Select QuickScanInterval. 7. Verify daily quick scan time: Get-MpPreference | Select ScheduleQuickScanTime. 8. Confirm scheduled scan type: Get-MpPreference | Select ScanScheduleQuickScanTime. 9. Check scheduled scan day: Get-MpPreference | Select ScanScheduleDay. 10. Verify scheduled scan time: Get-MpPreference | Select ScanScheduleTime. 11. Confirm scan after security intelligence update is disabled: Get-MpPreference | Select DisableScanAfterUpdate. 12. Monitor CPU usage via Task Manager or Performance Monitor for Microsoft Defender Antivirus processes (MsMpEng.exe, NisSrv.exe) to ensure utilization is reduced.

## Rollback
1. Re-enable Tamper Protection: Set-MpPreference -DisableTamperProtection $false. 2. Turn on real-time protection: Set-MpPreference -DisableRealtimeMonitoring $false. 3. Restore default CPU priority for scheduled scans: Set-MpPreference -LowCpuPriority $false. 4. Reset CPU usage limit per scan to default (50): Set-MpPreference -ScanAvgCPULoadFactor 50. 5. Re-enable ScanOnlyIfIdle: Set-MpPreference -ScanOnlyIfIdle $true. 6. Restore default quick scan interval (e.g., 1): Set-MpPreference -QuickScanInterval 1. 7. Reset daily quick scan time to default (e.g., 2:00 AM): Set-MpPreference -ScheduleQuickScanTime 02:00:00. 8. Restore default scheduled scan type (e.g., 2 for quick scan): Set-MpPreference -ScanScheduleQuickScanTime 2. 9. Restore default scheduled scan day (e.g., 0 for daily): Set-MpPreference -ScanScheduleDay 0. 10. Restore default scheduled scan time (e.g., 2:00 AM): Set-MpPreference -ScanScheduleTime 02:00:00. 11. Re-enable scan after security intelligence update: Set-MpPreference -DisableScanAfterUpdate $false. 12. If performance issues persist, consider excluding specific file types or processes via Set-MpPreference -ExclusionExtension or -ExclusionProcess.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
