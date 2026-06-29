# Optimization: Performance and Sensor Health

**Domain:** Defender for Endpoint
**Subdomain:** Performance and Sensor Health
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Microsoft Defender for Endpoint performance on Windows Server 2019 when the MsSense.exe process consumes more than 10% CPU continuously?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Windows Server 2019 with Microsoft Defender for Endpoint installed, default sensor configuration

## Symptoms
- MsSense.exe process consistently uses >10% CPU on Windows Server 2019
- System responsiveness degrades during peak hours
- Event ID 5007 appears in Microsoft-Windows-Windows Defender/Operational log indicating configuration changes

## Error Codes
N/A

## Root Causes
1. Sensor is running with default performance settings that may not be optimal for server workloads
2. High number of file scans or network events being processed without performance tuning

## Remediation Steps
1. Review the Microsoft Defender for Endpoint performance analyzer report to identify high-impact processes or paths: run Get-MpPerformanceReport from an elevated PowerShell session
2. Configure exclusions for trusted processes and file paths that are known to be safe, following the guidance in 'Configure and validate exclusions for Microsoft Defender for Endpoint'
3. Adjust the real-time protection scan settings using Set-MpPreference -DisableRealtimeMonitoring $false -ScanAvgCPULoadFactor 50 (adjust value based on workload)
4. Ensure the sensor is updated to the latest version via Microsoft Defender for Endpoint update channel

## Validation
After applying exclusions and adjusting CPU load factor, monitor MsSense.exe CPU usage over 24 hours; it should remain below 5% under normal load. Use Performance Monitor or Task Manager to verify.

## Rollback
To revert CPU load factor, run Set-MpPreference -ScanAvgCPULoadFactor 50 (default). Remove any added exclusions via Set-MpPreference -ExclusionPath @() or through the Microsoft 365 Defender portal.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-exclusions-microsoft-defender-antivirus>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/performance-analyzer>
