# Optimization: Performance Optimization

**Domain:** Defender for Endpoint
**Subdomain:** Performance Optimization
**Incident Type:** Optimization

## Scenario / Query
How can I reduce the CPU and disk usage of Microsoft Defender for Endpoint on Windows Server 2019 without compromising security?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Windows Server 2019 running Microsoft Defender for Endpoint with default real-time protection settings

## Symptoms
- High CPU usage by MsMpEng.exe during peak hours
- Increased disk I/O due to frequent scans
- User complaints about system slowness during file operations

## Error Codes
N/A

## Root Causes
1. Default scan schedule may conflict with business operations
2. Real-time protection scanning all file types without exclusions for trusted locations
3. Cloud-delivered protection timeout settings not optimized for server workloads

## Remediation Steps
1. Configure exclusions for trusted server roles (e.g., SQL Server data files, Exchange databases) using Group Policy or PowerShell: Set-MpPreference -ExclusionPath
2. Adjust the scan schedule to off-peak hours using Set-MpPreference -ScanScheduleDay and -ScanScheduleTime
3. Enable cloud-delivered protection with a shorter timeout: Set-MpPreference -CloudTimeout 50
4. Set the real-time protection to scan only incoming and outgoing files (not all files): Set-MpPreference -DisableRealtimeMonitoring $false -RealTimeScanDirection Incoming

## Validation
Run Get-MpPreference to verify the new settings. Monitor Task Manager for MsMpEng.exe CPU usage under 20% during normal operations.

## Rollback
Restore default settings using Set-MpPreference -ExclusionPath @() and Set-MpPreference -ScanScheduleDay 0 -ScanScheduleTime 02:00. Remove any custom exclusions via Group Policy.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-server-exclusions-microsoft-defender-antivirus>
