# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to address performance issues from Behavior Monitoring and Network Real-time Inspection even after adding path exclusions?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender Antivirus Behavior Monitoring (BM) and Network Real-time Inspection (NRI)

## Symptoms
- Higher CPU utilization by Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. Path exclusions work for scanning flows but not for Behavior Monitoring (BM) and Network Real-time Inspection (NRI)

## Remediation Steps
1. (Preferred) For .exe's and dll's use Indicators – File hash - allow or Indicators – Certificate - allow
2. (Alternative) Add Antivirus exclusions (process+path)

## Validation
1. Open PowerShell as Administrator and run: Get-MpPreference | Select-Object -Property ExclusionProcess, ExclusionPath, ExclusionExtension. Verify that the process and path exclusions are listed. 2. Check the current CPU usage of MsMpEng.exe via Task Manager or PowerShell: Get-Process MsMpEng | Select-Object CPU, WorkingSet. 3. Reproduce the workload that previously caused high CPU and confirm that CPU utilization remains below the acceptable baseline. 4. Review the Microsoft Defender Antivirus operational log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 5007 (configuration change) and any performance-related events.

## Rollback
1. Remove the added process and path exclusions: Remove-MpPreference -ExclusionProcess "<process.exe>" and Remove-MpPreference -ExclusionPath "<path>". 2. If Indicators were used, remove them via the Microsoft 365 Defender portal (Settings > Endpoints > Indicators > select the indicator and choose Remove). 3. Restart the Microsoft Defender Antivirus service: Stop-Service WinDefend; Start-Service WinDefend. 4. Re-enable Behavior Monitoring and Network Real-time Inspection if they were temporarily disabled: Set-MpPreference -DisableBehaviorMonitoring $false; Set-MpPreference -DisableNetworkProtection $false. 5. Verify that the original performance issue returns (as expected) and that no other system functionality is impacted.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
