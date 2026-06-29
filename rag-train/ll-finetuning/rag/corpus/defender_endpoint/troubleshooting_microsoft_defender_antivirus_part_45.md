# Troubleshooting: Microsoft Defender Antivirus (Error Code: Error code Result code associated with threat status. Standard HRESULT values.)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 2031 where the antimalware engine was unable to download and configure an offline scan?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2031 with symbolic name MALWAREPROTECTION_OFFLINE_SCAN_INSTALL_FAILED
- Message: The antimalware engine was unable to download and configure an offline scan

## Error Codes
- `Error Code: Error code Result code associated with threat status. Standard HRESULT values.`
- `Error Description: Error description Description of the error.`

## Root Causes
1. Microsoft Defender Antivirus encountered an error trying to download and configure offline antivirus.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational'. Verify that no new Event ID 2031 (MALWAREPROTECTION_OFFLINE_SCAN_INSTALL_FAILED) appears after remediation. 2. Run 'Get-MpComputerStatus | Select-Object AntivirusEnabled, AMEngineVersion, AMProductVersion' in PowerShell to confirm the antimalware engine is running and up to date. 3. Check the 'OfflineScanEnabled' property: 'Get-MpPreference | Select-Object OfflineScanEnabled' should return True. 4. Initiate a test offline scan using 'Start-MpWDOScan' and confirm no error is returned.

## Rollback
1. If the remediation introduced issues, restore the previous antimalware engine version by running 'Uninstall-WindowsFeature -Name Windows-Defender' (if applicable) or reinstall via 'Add-WindowsFeature -Name Windows-Defender'. 2. Reset Defender preferences to default: 'Set-MpPreference -Force'. 3. Clear any corrupted offline scan files by deleting contents of 'C:\ProgramData\Microsoft\Windows Defender\Scans\OfflineScan' after stopping the service: 'Stop-Service WinDefend; Remove-Item -Path "C:\ProgramData\Microsoft\Windows Defender\Scans\OfflineScan\*" -Force; Start-Service WinDefend'. 4. Reapply any custom policies from Group Policy or Intune that were modified during remediation.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
