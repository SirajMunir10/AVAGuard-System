# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to configure the CPU load factor for Microsoft Defender Antivirus scans triggered via Defender for Endpoint response actions?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** ScanAvgCPULoadFactor

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If ScanAvgCPULoadFactor is not configured, the default value is a limit of 50% maximum CPU load during a scan.
2. Configure ScanAvgCPULoadFactor to adjust CPU impact. For more information, see configure-advanced-scan-types-microsoft-defender-antivirus.

## Validation
1. Open PowerShell as Administrator on the target device.
2. Run: Get-MpPreference | Select-Object ScanAvgCPULoadFactor
3. Confirm the output shows the configured value (e.g., 50 for 50%).
4. If the value is not set, verify the default is 50 by checking the registry: Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Microsoft Antimalware\Scan' -Name AvgCPULoadFactor (if present).
5. Trigger a test scan via Defender for Endpoint response action and monitor CPU usage in Task Manager to ensure it does not exceed the configured load factor.

## Rollback
1. Open PowerShell as Administrator on the target device.
2. To reset to default (50%), run: Set-MpPreference -ScanAvgCPULoadFactor 50
3. Alternatively, remove the custom value: Remove-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Microsoft Antimalware\Scan' -Name AvgCPULoadFactor -Force
4. Verify the change: Get-MpPreference | Select-Object ScanAvgCPULoadFactor
5. If issues persist, restart the Microsoft Defender Antivirus service: Restart-Service -Name WinDefend

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
