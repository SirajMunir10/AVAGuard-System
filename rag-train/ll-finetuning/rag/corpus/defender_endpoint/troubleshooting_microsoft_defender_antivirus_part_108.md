# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to address high CPU utilization when Microsoft Defender Antivirus scans HTA, CHM, or complex file formats used as databases?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender Antivirus scanning of complex file formats

## Symptoms
- Higher CPU utilization by Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. Microsoft Defender Antivirus must extract and/or scan complex file formats such as HTA, CHM, and files used as databases

## Remediation Steps
1. Consider switching to using actual databases if you need to save info and query it
2. As a workaround: Add Antivirus exclusions (process+path)

## Validation
1. Open Task Manager and verify that the CPU usage by Microsoft Defender Antivirus (MsMpEng.exe) has dropped below 10% during idle periods.
2. Run the PowerShell command: Get-MpPreference | Select-Object -ExpandProperty ExclusionPath to confirm the added exclusion paths are listed.
3. Run the PowerShell command: Get-MpPreference | Select-Object -ExpandProperty ExclusionProcess to confirm the added exclusion processes are listed.
4. Trigger a scan of the previously problematic file types (e.g., HTA, CHM) and monitor CPU usage to ensure it remains low.

## Rollback
1. Remove the added exclusion paths by running: Remove-MpPreference -ExclusionPath "<path>" for each path added.
2. Remove the added exclusion processes by running: Remove-MpPreference -ExclusionProcess "<process>" for each process added.
3. Restart the Microsoft Defender Antivirus service by running: Restart-Service -Name WinDefend.
4. Re-run the validation steps to confirm CPU usage returns to previous levels.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
