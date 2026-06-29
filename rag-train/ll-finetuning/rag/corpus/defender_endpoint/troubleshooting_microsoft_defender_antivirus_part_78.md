# Troubleshooting: Microsoft Defender Antivirus (0x80501102)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501102 (MP_ERROR_CODE_ALREADY_SHUTDOWN) in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501102 displayed
- Message displayed: MP_ERROR_CODE_ALREADY_SHUTDOWN

## Error Codes
- `0x80501102`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Applications and Services Logs' > 'Microsoft' > 'Windows' > 'Windows Defender' > 'Operational'.
3. Verify that no new events with ID 1006, 1007, or 1008 (detection events) or error events with ID 3002 or 3004 (engine failure) appear after remediation.
4. Run the following PowerShell command to confirm Microsoft Defender Antivirus is running and real-time protection is enabled:
   Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled, AntispywareEnabled
   Ensure all properties return 'True'.
5. Run a quick scan to verify functionality:
   Start-MpScan -ScanType QuickScan
   Confirm the scan completes without error code 0x80501102.

## Rollback
1. If the error persists or the service fails to start, restore the default service startup types:
   - Open an elevated Command Prompt and run:
     sc config WinDefend start= auto
     sc config WdNisSvc start= manual
     sc config Sense start= auto
   - Restart the service:
     net start WinDefend
     net start WdNisSvc
     net start Sense
2. If registry modifications were made, restore the default values for Microsoft Defender Antivirus settings by running:
   reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /f
   (Note: This removes all policy settings; reapply necessary policies after.)
3. If the issue is related to a conflicting third-party antivirus, uninstall the third-party product and re-enable Microsoft Defender Antivirus via:
   Set-MpPreference -DisableRealtimeMonitoring $false
4. As a last resort, perform a system restore to a point before the error occurred using:
   rstrui.exe

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
