# Troubleshooting: Microsoft Defender Antivirus (3002)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to determine if a real-time protection failure in Microsoft Defender Antivirus is temporary?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 3002 followed by Event ID 3007

## Error Codes
- `3002`
- `3007`

## Root Causes
1. The failure was temporary and the antimalware client recovered from the failure

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Applications and Services Logs' > 'Microsoft' > 'Windows' > 'Windows Defender' > 'Operational'.
3. Look for Event ID 3002 (real-time protection failure) followed by Event ID 3007 (recovery from failure) within a short time window.
4. Confirm that Event ID 3007 appears after Event ID 3002, indicating the antimalware client recovered automatically.
5. Run the PowerShell command: Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled, RealTimeProtectionRunning, AntivirusEnabled, AMServiceEnabled, AMServiceVersion
6. Verify that RealTimeProtectionEnabled and RealTimeProtectionRunning are both True, and AntivirusEnabled and AMServiceEnabled are True.
7. Check for any subsequent Event ID 3002 without a corresponding Event ID 3007, which would indicate a persistent failure.

## Rollback
1. If the failure persists (no Event ID 3007 after Event ID 3002), run the following PowerShell command to restart the Microsoft Defender Antivirus service: Restart-Service -Name WinDefend
2. If the service fails to restart, run: Set-MpPreference -DisableRealtimeMonitoring $false
3. Verify the service status: Get-Service -Name WinDefend | Select-Object Status, StartType
4. If the issue continues, run the Microsoft Support and Recovery Assistant for Microsoft Defender Antivirus: https://aka.ms/MDATroubleshooter
5. As a last resort, run the Windows Update Troubleshooter: Start-Process ms-settings:troubleshoot
6. If all else fails, contact Microsoft Support with the Event IDs and any error codes.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
