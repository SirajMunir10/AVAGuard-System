# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
What is triggering and causing higher CPU utilization in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Higher CPU utilization in Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Collect Microsoft Defender Antivirus diagnostic data
2. Use Performance analyzer for Microsoft Defender Antivirus to run data collection and parse the data
3. If Performance analyzer does not provide enough details, use Process Monitor (ProcMon) to collect data for 5-10 minutes
4. For more advanced troubleshooting, use Windows Performance Recorder UI (WPRUI) or Windows Performance Recorder (WPR) for a maximum of 3 to 5 minutes

## Validation
1. Run the Microsoft Defender Antivirus Performance analyzer: Start-MpPerformanceRecording -RecordTo <path_to_output_file> -Duration 60. 2. Parse the generated ETL file using Get-MpPerformanceReport -Path <path_to_etl_file> -TopFiles 10. 3. Verify that the report shows no single process or file causing >10% CPU usage. 4. If using Process Monitor, confirm that ProcMon logs show no sustained high CPU activity from MsMpEng.exe or related processes. 5. If using WPRUI/WPR, ensure the recorded trace (WPR file) shows CPU usage within baseline (<30% total for Antimalware Service Executable).

## Rollback
1. Stop any active performance recording: Stop-MpPerformanceRecording. 2. Delete the generated ETL, ProcMon, or WPR trace files from the collection directory. 3. If Process Monitor was used, unload the ProcMon driver via ProcMon.exe /Terminate. 4. If WPR was used, stop the recording via WPR.exe -cancel or WPRUI 'Cancel' button. 5. Restart the Microsoft Defender Antivirus service: Stop-Service WinDefend; Start-Service WinDefend. 6. Revert any temporary exclusions added during troubleshooting by removing them from Group Policy or registry: Remove-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender\Exclusions' -Name 'TempExclusionPath' -ErrorAction SilentlyContinue.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
