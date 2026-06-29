# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to prevent performance issues when sealing a VDI image with Microsoft Defender Antivirus cache not completed?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Non-persistent VDI image creation

## Symptoms
- Higher CPU utilization by Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. Cache maintenance not completed before the image is sealed

## Remediation Steps
1. Make sure that cache maintenance completes before the image is sealed
2. For more information, see Configure Microsoft Defender Antivirus on a remote desktop or virtual desktop infrastructure environment

## Validation
1. On the sealed VDI image, run 'Get-MpPreference' in PowerShell as Administrator and verify that 'DisableRealtimeMonitoring' is set to False. 2. Check the 'C:\ProgramData\Microsoft\Windows Defender\Scans\mpcache-*.bin' file timestamp to confirm it is recent (within the last 24 hours). 3. Use Performance Monitor to verify that the average CPU usage of 'MsMpEng.exe' is below 10% during idle periods. 4. Run 'Get-MpComputerStatus' and confirm 'AMServiceEnabled' is True and 'AntivirusEnabled' is True.

## Rollback
1. If cache maintenance did not complete, re-deploy the VDI image without sealing, run 'Update-MpSignature' to force signature update, then run 'Start-MpScan -ScanType QuickScan' to trigger cache creation. 2. After cache is created, seal the image again. 3. If performance issues persist, temporarily disable real-time protection by running 'Set-MpPreference -DisableRealtimeMonitoring $true' on the affected VDI session, then investigate further using the guidance at https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
