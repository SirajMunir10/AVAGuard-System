# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot high CPU usage or performance issues related to Microsoft Defender Antivirus (Anti-malware Service Executable, MsMpEng.exe)?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- High CPU usage
- Performance issues related to Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Check if other software is causing the issue.
2. Read Check with the vendor for known issues with antivirus exclusions.

## Validation
1. Open Task Manager and verify that CPU usage by MsMpEng.exe has returned to normal levels (typically <10% during idle).
2. Run the PowerShell command: Get-MpPerformanceReport -Path $env:TEMP\MpPerfReport.csv and confirm the report shows no excessive scans or high resource consumption.
3. Check the Microsoft Defender Antivirus event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for any error events related to performance.
4. If exclusions were added, verify they are applied by running: Get-MpPreference | Select-Object -ExpandProperty ExclusionPath

## Rollback
1. Remove any exclusions added during remediation by running: Remove-MpPreference -ExclusionPath "<path>" for each exclusion.
2. If performance issues persist, restore the default Microsoft Defender Antivirus configuration by running: Set-MpPreference -DisableRealtimeMonitoring $false (if it was disabled) and then run: Update-MpSignature.
3. Reboot the machine if instructed by the vendor or if changes were made to services.
4. If the issue is caused by conflicting software, re-enable that software's real-time protection or reinstall it after confirming with the vendor.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
