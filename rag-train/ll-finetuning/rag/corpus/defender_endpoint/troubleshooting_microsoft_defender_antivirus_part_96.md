# Troubleshooting: Microsoft Defender Antivirus (0x80508019)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot error code 0x80508019 with message ERR_MP_NOT_FOUND in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508019
- Message displayed: ERR_MP_NOT_FOUND

## Error Codes
- `0x80508019`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Windows Logs' > 'System'.
3. Look for events from source 'Microsoft Antimalware' or 'Microsoft Defender Antivirus' with Event ID 1001 or 1002 that indicate successful start or no errors.
4. Run the following PowerShell command to check the status of Microsoft Defender Antivirus:
   Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled
   Confirm that AntivirusEnabled, RealTimeProtectionEnabled, and AMServiceEnabled are all True.
5. Run a quick scan using:
   Start-MpScan -ScanType QuickScan
   Verify the scan completes without error code 0x80508019.
6. Check the Microsoft Defender Antivirus client version by running:
   Get-MpComputerStatus | Select-Object AMProductVersion
   Ensure the version is current and matches the latest available from Microsoft.

## Rollback
1. If the remediation involved modifying registry keys, restore the original values from a backup or revert to the default configuration using:
   Remove-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows Defender' -Name 'DisableAntiSpyware' -ErrorAction SilentlyContinue
   (Note: This is an example; actual rollback depends on the specific changes made.)
2. If services were stopped or disabled, re-enable them:
   Set-Service -Name WinDefend -StartupType Automatic
   Start-Service -Name WinDefend
   Set-Service -Name WdNisSvc -StartupType Manual
   Start-Service -Name WdNisSvc
3. If the remediation involved uninstalling or reinstalling Microsoft Defender Antivirus, reinstall it using the 'Turn Windows features on or off' control panel or via DISM:
   dism /online /Enable-Feature /FeatureName:Windows-Defender-ApplicationGuard /All
   (Note: This is an example; actual rollback depends on the specific changes made.)
4. Restart the system to ensure all changes take effect and services start correctly.
5. Re-run the validation steps to confirm the error code 0x80508019 returns or the original issue persists.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
